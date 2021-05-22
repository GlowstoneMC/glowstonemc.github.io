title: This Week in Glowstone - 1
date: 2016-07-31 12:00
category: updates

Yep. We are now going to have one of those weekly blog posts where we spew a bunch of numbers at you: 33 commits. 809 additions. 304 deletions. But we have one special number to throw at you this week: 1.10.2. That's the latest version of Minecraft and now it's also the latest version of Minecraft we support, thanks to the hard work and patience of momo. This PR was actually practically ready a month ago but due to good reasons it was delayed until 2 days ago.
And here's another milestone/meaningless number: with all the commit spam we've done over the years, Glowstone has reached 1,999 commits. Finally!
You might be wondering why 1999 is such a huge milestone. And that's because this is our last commit. We're too scared of Y2K to go any further.
But seriously, I, mastercoms, have been working on a very special feature that will be revealed to you next week in the next "This Week in Glowstone" post, or ~~tomorrow, in the commit log~~ *it's going to take a bit longer*. But that's no fun.
Anyway, please pardon the rather long introduction/rambling, and let's get into week one of This Week in Glowstone:

**Discussion**

* Addition of the "Story" label to distinguish tasks from bug reports, along with a general revamp of all of our labels
* Planning done to expose nms and obc features (and more) in Glowkit, and to provide these features with Linkstone, a clean room rewrite of these packages

**Notable changes**

* 1.10.2
* New dev tools for rapid iteration and testing
* Removed error logs from shutdown thread, as they were not actually errors and just served to confuse people
* Summon command
* Documentation changes and additions

**Fixes**

* Fixes to CircleCI related to Glowkit changes
* A fix to invalid chunk lengths caused by flowing water
* A fix to block types when being modified from one type to another by the client
* Remove unnecessary check in shutdown thread
