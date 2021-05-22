title: Intrusion Report (Forums)
date: 2017-07-28 9:03
category: news

This is a post to notify everyone of a possible intrusion relating to the forum. I have provided a full report in an effort to be as transparent as possible.

## Report

### Tuesday, 25th July 2017

Momo noticed that the forums were down. I was asleep at the time, and did not get the message until the morning - it was late at night.

### Wednesday, 26th July 2017

I got Momo's message, and investigated the problem. I assumed that Redis was down, so I restarted it and updated and restarted the forums, and everything appeared to be working just fine. I noticed that the plugins we had installed were removed, and so I reinstalled them. No configuration data was lost. I also noticed that a couple of posts I had made a day or two before that were missing.

### Thursday, 27th July 2017

I noticed that a Nextcloud install on a different VM (my personal install) was using the same database server as a memory cache, despite being configured not to. I reconfigured Nextcloud and removed all of its cached data from the database. Nextcloud did not touch any actual NodeBB data, so that wasn't the cause of the issue.

At this point, we realised that data going back around a month and a half had been lost. Fearing further data loss, I set up some cron tasks to force Redis to save its data and save a backup every hour. I checked the Redis logs and there was nothing abnormal in them, so I assumed the problem was with NodeBB and continued investigating with Momo.

After reading over NodeBB logs, events and errors, we found nothing of interest.

### Friday, 28th July 2017

At around 4AM BST, Momo became available again and continued his investigation. He discovered two things:

- Redis was accessible (without a password) from outside of the network
- Redis was failing to save any data due to an error, thus disabling the forums

At around 8:30AM BST, I came online and restarted my investigation.

Due to an issue with Proxmox (the hypervisor I use to manage containers and VMs and keep things compartmentalised), it turned out that the firewall I had configured was not doing its job - instead of dropping all disallowed traffic as it was meant to, it was simply allowing everything. I fixed this problem by setting up a firewall directly on the storage container and this secured it from the outside.

I noticed that Redis was attempting to save data to `/var/spool/cron`, which is not its usual location. It did not have permission to write there - which is why it was failing to save data. Upon further investigation, I noticed that it was able to overwrite the crontab I had set up earlier - and had done so with the entire contents of the database. At this point, I took down both Redis and NodeBB so that I could fix things up.

I wiped all of the cron storage directories and reinstalled cron. I double-checked the Redis configuration and found nothing unusual, so I restarted that as well. It started up correctly and did not attempt to write to `/var/spool/cron` again.

I used a GUI tool to inspect the Redis data, and I noticed that the data I had removed previously (from Nextcloud) was still present. I removed it again, and I noticed an extra key that I hadn't seen earlier: It was a randomized key, containing a crontab entry. This crontab was configured to download a shell script from an IP address and execute it.

I grabbed a copy of the script myself and took a look at it, and it simply downloaded a cryptocurrency miner and ran it. Upon investigation, it was clear that this crontab had never been run, and that the attack was supposed to play out as follows:

- Search for compromisable Redis servers
- Add a key with a crontab entry to run the script
- Use the `CONFIG SET` command to overwrite the crontab with the database
- Wait for the cryptocurrency miner to start

The cron daemon I'm using performs very strict syntax checks and did not run the crontab - as soon as it realised there were invalid "entries" in the file, it errored out.

I removed the key from the database and made sure the forum was running correctly.

### Exposure

While there was absolutely no evidence that this attack targetted NodeBB or even Glowstone specifically, precautions should always be taken. As NodeBB stores its entire database in Redis, all of the data therein was exposed. It's impossible to say what the attackers may have taken - if anything - but as always, users should take all of the necessary precautions.

NodeBB stores passwords using `bcrypt`. This is an industry standard and currently considered very secure, but we still advise users to change their passwords - both on the forums, and on any accounts they own elsewhere that may be using the same password as their forum account. Note that any other data provided during registration and profile modification will have been accessible as well - for example, email addresses.

I have revoked all the user tokens from GitHub OAuth, and reset the client secret, to protect users' GitHub accounts.

---

I'd like to apologise for this intrusion personally - it definitely shouldn't have happened, and while I'm amazed that it did, it is my responsibility. Please don't attack or bug any of the other staff members - they don't have direct access to any of this stuff.

As far as I am aware, everything is now secure and in working order, but I'm going to continue monitoring and testing throughout the day. Feel free to contact me if you have any questions.
