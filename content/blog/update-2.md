title: This Week In Glowstone - 2
date: 2016-08-08 12:00
category: news
tags: updates
author: mastercoms
email: mastercoms@tuta.io

So this week was [quiet, too quiet](https://www.youtube.com/watch?v=6rH55V_hp1Q), with only 127 additions and 4 deletions and 8 changed files. But that doesn't mean we weren't busy, nor does it mean that there's a trap. There have been some nice fixes here and there and legacy ping support, with more features and bug fixes being worked on that unfortunately did not make it into master this week.

Discussion

* Decided on how to organize the protocol API for Glowstone/Linkstone

Notable changes

* Added support for legacy pings/queries

Fixes

* Fixed containers not dropping their contents when broken by a player in creative mode
* Changed the fast-util repo to the correct URL, which fixes dependency errors
* Fix ghost players on death

Coming up

* Hoppers and tile tick format
* Readding block cache with less bugs
* Fix items that can be placed as blocks placing the wrong block
* Internationalization support
