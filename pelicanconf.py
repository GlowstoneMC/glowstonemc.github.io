#!/usr/bin/env python
# -*- coding: utf-8 -*- #

from pelican.plugins import alias, issues

AUTHOR = 'Glowstone Organization'
SITENAME = 'Glowstone'
SITESUBTITLE = 'Minecraft\'s future is bright'
SITEURL = ''

PATH = 'content'

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

# Skip generation of some pages
AUTHOR_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
TAG_SAVE_AS = ''

ARTICLE_URL = 'news/{slug}/'
ARTICLE_SAVE_AS = 'news/{slug}/index.html'

STATIC_PATHS = ['images', 'extra/favicon.ico']
EXTRA_PATH_METADATA = {'extra/favicon.ico': {'path': 'favicon.ico'},}
IGNORE_FILES = ['.#*', 'jd']

TIMEZONE = 'UTC'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DIRECT_TEMPLATES = ['index', '404', 'news/index']
PAGINATED_TEMPLATES = {'news/index': None, 'tag': None, 'category': None, 'author': None}

THEME = "theme"

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),)

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/GlowstoneMC'),
          ('Discord', 'https://discord.gg/TFJqhsC'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
