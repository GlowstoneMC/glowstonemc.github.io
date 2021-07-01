import itertools
import re

from pelican import signals


ISSUE_REGEX = re.compile(r"([\s(])(#[\d]+)([\s)])")
ISSUE_URL = "https://github.com/GlowstoneMC/Glowstone/issues/{}"
ISSUE_HTML = """{}<a href="{}">{}</a>{}"""


def process_content(article):
    done_tags = set()

    for start, tag, end in ISSUE_REGEX.findall(article._content):
        if tag in done_tags:
            continue

        done_tags.add(tag)
        num = tag[1:]
        article._content = article._content.replace(
            "{}{}{}".format(start, tag, end),
            ISSUE_HTML.format(start, ISSUE_URL.format(num), tag, end),
        )


def get_issue_links(generator):
    blog = itertools.chain(generator.articles, generator.drafts)
    for article in blog:
        process_content(article)


def register():
    signals.article_generator_finalized.connect(get_issue_links)
