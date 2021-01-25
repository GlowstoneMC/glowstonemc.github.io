What comes after 2? 8, because we're bad at counting, except when it comes to commits. In this month (which is roughly a week), we've had [86 commits](https://github.com/GlowstoneMC/Glowstone/compare/14569fae2a5122af730c90985adb3e1c171c02c7...master) on master. Those commits added 1,901 lines and removed 794. You can read through all of those lines, or you can read these lines:

Discussion
* Shine, our plugin downloads website and compatibility database
* GitHub is awful
* Where is the weekly blog post???

Notable changes
* Lots of documentation changes/additions, a version independent JAR download and maven adjustments
* Native transport (epoll)
* Support for particle spawning
* Shovel path block creation
* Sound effects for buttons, levers, entity death, and entity hurt
* Hoppers
* More complete scoreboard support
* Sound category support
* Some work on the anvil inventory and custom item names
* Support for statistics with type array (i.e. Adventuring Time)
* Tile tick support
* Item frames (rewritten to work again)

Fixes
* Optimizations and fixes to entity detection for explosions
* Fix player data trying to save data on an unloaded world during shutdown
* No more weird things happening when y > 256
* Fixed and cleaned up entity spawn code
* Cleaned up effect playing
* Optimizations and refactoring of block tick system
* Slab fixes (and purpur slab support)
* Block placement sound only plays once now
* Fixes to replacing a double plant with a block placement
* Removed debug output from fence gate
* Enchantment table now uses tile entity
* Optimizations and fixes to redstone
* Chunk errors related to ticking blocks that were not loaded
* Better rail placement that takes into account facing direction
* You can no longer place blocks where an entity is (plus definitions for entity bounding boxes)
* Place the block an item represents rather than the item (ex. cauldron)
* Don't try to check if a block can absorb a placement if it doesn't exist
* Optimizations/fixes to furnaces
* Durability now works with right click tools
* Fixed stop sound command and moved to Glowkit
* Fixed changed blocks desync
* Food level now resets on death
* Players do not become "ghosts" on deaths anymore
* Fixed null in UUID json lists (ops.json, etc)
* Some optimization work to player UUID fetching
* Fix NullPointerException if a tameable doesn't have an owner
* SignChangeEvent is now called
* Checks for unknown interacted blocks
* Elytra now properly uses durability
* Optimized HttpClient

Coming up
*  1.11 support
* Entity AI
* Packet API
* LivingEntity drops
* net.glowstone.block refactor
* Better world customization
* Internationalization support
* New website ([preview](https://momothereal.github.io/glowstone-website/index.html))

Phew, that's a lot of stuff. I wish every week could take 42 days.