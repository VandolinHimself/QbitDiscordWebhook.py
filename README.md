"""
QBittorrent Discord Webhook and Rclone command wrapper
Version: 1.0
This script will send a notification to Discord via webhook, that your download are finished.
After that, it execute a "copy" command from rclone to back it up to cloud storage
This script might or not might works with other torrent client.
:param name: The torrent name that will be sended
:param size: Torrent sizes in bytes.
:param hash: Torrent hash
:param path: Full path to the downloaded file or folder
If you're in linux, chown this file to the user that run torrent client and
don't forget to put the rclone.conf file to `~/.config/rclone/rclone.conf` then
chown the `rclone` folder and the config file in `~/.config`
"""
