On Sunday, we updated Archiva (our Maven repository) to a more recent version. During the upgrade, we unfortunately lost all our artifacts stored on the server. There was a major downtime in which we attempted to fix storage and deployment, but the artifacts could not be recovered.

Because we did not have backups for the Maven repository, (that would take a lot of space, considering each snapshot is ~19MB) we had to re-deploy the latest snapshots manually.
Deployment now works and further builds will be added to the repository. Note that any artifact older than `2018.0.0-SNAPSHOT` (including the latest release, 2017.11) will cause 404 errors in your builds.
Furthermore, only the latest Glowkit version (`1.12.2-R0.1-SNAPSHOT`) is on the repository, and older artifacts will also 404.

Due to an issue with how Archiva indexes the Browse tool, you will still see metadata version about all previous artifacts that were on the repository prior to the upgrade. We have contacted Archiva for a fix to reset the search indexing to what we have now.

We are very sorry for the inconvenience the downtime and artifact loss may have caused. If there are more issues, please contact us on [Discord](https://discord.gg/TFJqhsC).
