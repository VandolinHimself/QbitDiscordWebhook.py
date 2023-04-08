QBittorrent Discord Webhook and Rclone command wrapper


This script will send a notification to Discord via webhook when your downloads are finished.  After that it executes a copy command from rclone to back it up to cloud storage.  This script might or might not work with other torrent clients...  I haven't tested it with an extensive list of options but I've realized some do and some don't.


:param name: The torrent name that will be sent

:param size: Torrent sizes in bytes.

:param hash: Torrent hash

:param path: Full path to the downloaded file or folder


If you're in linux, chown this file to the user that runs the torrent client and don't forget to add the rclone.conf file `~/.config/rclone/rclone.conf` then chown the `rclone` folder and the config file in `~/.config`
