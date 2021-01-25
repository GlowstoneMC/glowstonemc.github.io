title: My Little Glowkit: Patching Is Magic

As some of you may know, recently, [Glowkit](https://github.com/GlowstoneMC/Glowkit) has moved to a patch-based system. We feel that it's going to be far easier to work with Glowkit on a development and compilation basis by adopting this method, and it also allows us to base upon much more recent Bukkit forks - such as the one maintained as part of PaperSpigot.

If you're just a Glowstone user, this has no immediate effect on your experience. Contributors and maintainers, though, should bear the following steps in mind:

* Clone the repository recursively, to include the submodules (`git clone --recursive`)
* Run `applyPatches.sh` (Windows users can use Git Bash, or Bash for Windows 10)
* Make your changes in the `Glowkit-Patched` directory
* Compile, test, and so on
* Commit your changes
* Run `rebuildPatches.sh`
* Commit your changes and push them
