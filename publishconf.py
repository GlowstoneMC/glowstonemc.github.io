#!/usr/bin/env python
# -*- coding: utf-8 -*- #

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL = 'https://glowstone.net'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/atom/news'
FEED_RSS  = 'feeds/rss/news'

DELETE_OUTPUT_DIRECTORY = True

STATIC_PATHS = ['images', 'jd', 'extra/favicon.ico', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/favicon.ico': {'path': 'favicon.ico'}, 'extra/CNAME': {'path': 'CNAME'},}

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""
