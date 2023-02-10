QBittorrent Discord Webhook and Rclone command wrapper
Version: 1.0

This script will send a notification to Discord via webhook when your downloads are finished.

After that it 4executes a copy command from rclone to back it up to cloud storage.

This script might or might not works with other torrent clients.

:param name: The torrent name that will be sent

:param size: Torrent sizes in bytes.

:param hash: Torrent hash

:param path: Full path to the downloaded file or folder


If you're in linux, chown this file to the user that runs the torrent client and don't forget to add the rclone.conf file `~/.config/rclone/rclone.conf` then chown the `rclone` folder and the config file in `~/.config`
