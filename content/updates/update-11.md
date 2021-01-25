title: Glowstone Update - 11

Hello, welcome back to one of these updates on what we've been up to with the Glowstone project!

One of our developers, @momothereal, is giving the update this time around:

We haven't done one of these in the past weeks so I thought I would share what has been completed and what we are hoping to achieve in the future.
Since the last monthly update in October, we have pushed 64 [commits](https://github.com/GlowstoneMC/Glowstone/compare/3f1bb341372cc19dad01f3e16c5eb921476f55f1...master) onto master, counting 7,309 additions and 1,764 deletions from 8 contributors. Fifteen pull requests were merged and 4 more have been opened.

These changes mainly consisted of:
 - Updating to 1.11 and 1.11.2
 - Various adjustments and improvements to the network server
 - Official support for registering custom entities
 - RegionFile performance improvements
 - Implementation of the Fortune enchantment
 - Animal world decoration (spawning);
 - Entity loot and loot tables;
 - Observer block implementation;
 - Armor bar and attribute manager overhaul;
 - Basic async AI tasking for animals;
 - BossBar API implementation;
 - Various optimizations and fixes.

In other news, we have also changed our Maven repository manager to Apache Archiva (say goodbye to Nexus!). 

We have also changed Glowstone's version scheme to a Minecraft-independent system. As such, our versions will no longer be tagged with the latest supported Minecraft version. Our current version as of writing this post is 2017.0.1.2, as described with the following format: {year}.{major}.{minor}.{trivial}. We might expand on this format later on.

In the future, we hope to achieve more customizability to our server platform. We have started this goal by supporting custom entities and the beginning of AI tasking. As always, we will pursue our objective to keep up with Minecraft updates (1.12 coming in the future) as well as implementing more features from the vanilla server software and the Bukkit API.

Also note that development might slow down in the upcoming weeks, some of us are quite busy with other projects and/or personal endeavors.

Thanks momo for the update! And now, I would like to give an update on these updates. :)

We hope to release these posts more frequently and more on time, but we can't really commit to a set time schedule like we've tried in the past (hint: it doesn't work). However, we are really sorry for not keeping up these past few months.

Thanks for stopping by and we hope to see you soon in the next update, which hopefully won't be released too far away!