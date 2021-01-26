title: About Sponge...
date: 2017-01-31 21:06

EDIT: A lot has changed since this blog post, both in the goals of Glowstone, and Sponge's API in version 8. We aren't completely ruling out the possibility of using Sponge, and this post's strong language does not reflect the sentiment of the team.

So over time, we've found a lot of people asking us about Sponge. Now that its hype has died down quite a bit, I think it's time to clarify a few things about Glowstone and Sponge, including a few misconceptions:

**Cool, it's Glowstone, that Sponge server I've been hearing about!**

https://twitter.com/SpongePowered/status/537748767286784002

Glowstone does not use Sponge at all in its code. We do not support Sponge natively, and the plugin we made, Bukkit2Sponge, currently targets Sponge 2.0 (they're on 6.0 now), and it barely even implements anything from 2.0 anyway. We aren't interested in developing it further at this time.

**Well, I'm at least glad Glowstone teamed up with Sponge!**

https://www.reddit.com/r/admincraft/comments/2foll6/weve_gotten_together_developers_from_spout_forge/

**\*Edit (May 28, 2017)**: This reddit post has been deleted by its original poster. Here is an archived [snapshot](https://web.archive.org/web/20161210172443/https://www.reddit.com/r/admincraft/comments/2foll6/weve_gotten_together_developers_from_spout_forge/) of this post from December 2016. -Momo\*

I'm not aware of any Glowstone partnership with Sponge. If there is/was one, Sponge has done a poor job maintaining it, as we haven't been contacted by them at all.

**Hm, but you're working on Sponge support?**

Nope. And with our current plans, we will never work on Sponge support for Glowstone. It's just too much work for us for little to no benefit.

**Well alright then, Sponge is still the future... right?**

Well no. Now that the hype has died down, its plugin dev community is quite small.

Also, personally, I think Sponge isn't very well designed. [This line](https://github.com/SpongePowered/SpongeAPI/blob/stable-7/src/main/java/org/spongepowered/api/data/value/mutable/CompositeValueStore.java#L49) explains it best. Of course, there are numerous other design flaws, like other problems in the data API, confusing naming patterns, and avoidance of simpler Java constructs, but all of that is out of the scope of this post.

Well, thanks for reading this post. I hope it clarified some things about Sponge and how it relates to Glowstone. If you want to learn more, I would be happy to expand on anything, if asked.
