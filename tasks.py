# -*- coding: utf-8 -*-

import os
import shlex
import shutil
import sys
import datetime
import pathlib
import sass
import logging

from invoke import task
from invoke.main import program
from invoke.util import cd
from pelican import main as pelican_main
from pelican.server import ComplexHTTPRequestHandler, RootedHTTPServer
from pelican.settings import DEFAULT_CONFIG, get_settings_from_file

OPEN_BROWSER_ON_SERVE = True
SETTINGS_FILE_BASE = 'pelicanconf.py'
SETTINGS = {}
SETTINGS.update(DEFAULT_CONFIG)
LOCAL_SETTINGS = get_settings_from_file(SETTINGS_FILE_BASE)
SETTINGS.update(LOCAL_SETTINGS)

CONFIG = {
    'settings_base': SETTINGS_FILE_BASE,
    'settings_publish': 'publishconf.py',
    # Output path. Can be absolute or relative to tasks.py. Default: 'output'
    'deploy_path': SETTINGS['OUTPUT_PATH'],
    # Github Pages configuration
    'github_pages_branch': 'gh-pages',
    'commit_message': "'Publish site on {}'".format(datetime.date.today().isoformat()),
    # Host and port for `serve`
    'host': 'localhost',
    'port': 8000,
}

@task
def clean(c):
    """Remove generated files"""
    if os.path.isdir(CONFIG['deploy_path']):
        shutil.rmtree(CONFIG['deploy_path'])
        os.makedirs(CONFIG['deploy_path'])

@task
def build(c):
    """Build local version of site"""
    pelican_run('-s {settings_base}'.format(**CONFIG))

@task
def rebuild(c):
    """`build` with the delete switch"""
    pelican_run('-d -s {settings_base}'.format(**CONFIG))

@task
def regenerate(c):
    """Automatically regenerate site upon file modification"""
    pelican_run('-r -s {settings_base}'.format(**CONFIG))

@task
def serve(c):
    """Serve site at http://$HOST:$PORT/ (default is localhost:8000)"""

    class AddressReuseTCPServer(RootedHTTPServer):
        allow_reuse_address = True

    server = AddressReuseTCPServer(
        CONFIG['deploy_path'],
        (CONFIG['host'], CONFIG['port']),
        ComplexHTTPRequestHandler)

    if OPEN_BROWSER_ON_SERVE:
        # Open site in default browser
        import webbrowser
        webbrowser.open("http://{host}:{port}".format(**CONFIG))

    sys.stderr.write('Serving at {host}:{port} ...\n'.format(**CONFIG))
    server.serve_forever()

@task
def reserve(c):
    """`build`, then `serve`"""
    build(c)
    serve(c)

@task
def preview(c):
    """Build production version of site"""
    pelican_run('-s {settings_publish}'.format(**CONFIG))

@task
def livereload(c):
    logger = logging.getLogger('livereload')
    """Automatically reload browser tab upon file modification."""
    from livereload import Server

    theme_path = SETTINGS['THEME']

    def sass_build(changed=None):
        if changed:
            for path in changed:
                stem = pathlib.Path(path).stem
                try:
                    css_str = sass.compile(filename=path, output_style='compressed')
                    if css_str:
                        with open(f'{theme_path}/static/css/{stem}.css', 'w') as f:
                            f.write(css_str)
                    else:
                        logger.error(f'Unable to compile {path}')
                except sass.CompileError as e:
                    logger.error(str(e))
        else:
            sass.compile(dirname=(f'{theme_path}/static/sass', f'{theme_path}/static/css'), output_style='compressed')

    def cached_build():
        cmd = '-s {settings_base} -e CACHE_CONTENT=True LOAD_CONTENT_CACHE=True'
        pelican_run(cmd.format(**CONFIG))

    sass_build()
    cached_build()
    server = Server()

    sass_file_extensions = ['.scss']
    for extension in sass_file_extensions:
        sass_glob = f'{theme_path}/static/**/*{extension}'
        server.watch(sass_glob, sass_build)

    watched_globs = [
        CONFIG['settings_base'],
        '{}/templates/**/*.html'.format(theme_path),
        'content/pages/*.html'
    ]

    content_file_extensions = ['.md', '.rst']
    for extension in content_file_extensions:
        content_glob = '{0}/**/*{1}'.format(SETTINGS['PATH'], extension)
        watched_globs.append(content_glob)

    static_file_extensions = ['.css', '.js']
    for extension in static_file_extensions:
        static_file_glob = '{0}/static/**/*{1}'.format(theme_path, extension)
        watched_globs.append(static_file_glob)

    for glob in watched_globs:
        server.watch(glob, cached_build)

    if OPEN_BROWSER_ON_SERVE:
        # Open site in default browser
        import webbrowser
        webbrowser.open("http://{host}:{port}".format(**CONFIG))

    server.serve(host=CONFIG['host'], port=CONFIG['port'], root=CONFIG['deploy_path'])

@task
def gh_pages(c):
    """Publish to GitHub Pages"""
    preview(c)
    c.run('ghp-import -nfpb {github_pages_branch} '
          '-m {commit_message} '
          '{deploy_path}'.format(**CONFIG))

def pelican_run(cmd):
    cmd += ' ' + program.core.remainder  # allows to pass-through args to pelican
    pelican_main(shlex.split(cmd))
