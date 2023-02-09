import argparse
import subprocess

from discord_webhook import DiscordWebhook, DiscordEmbed

# Python Version: 3.6+
# Requirements: `pip3 install discord-webhook``
# Help: `python3.6 qbitWebhook.py -h``

#################################################
WEBHOOK_URL = 'DISCORD WEBHOOK URL'
RCLONE_UPLOAD_DESTINATION = 'UPLOAD DESTINATION WITHOUT QUOTATION MARK'
DISCORD_ID = 'YOUR DISCORD USER ID'
#################################################

def sizeof_fmt(num, suffix='B'):
    num = int(num)
    for unit in ['','Ki','Mi','Gi','Ti','Pi','Ei','Zi']:
        if abs(num) < 1024.0:
            return "%3.1f %s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f %s%s" % (num, 'Yi', suffix)

parser = argparse.ArgumentParser(description='QBittorrent Discord Notifier and Rclone wrapper')
parser.add_argument('--name', required=True, help="Torrent name")
parser.add_argument('--size', required=True, help="Torrent size")
parser.add_argument('--hash', required=True, help="Torrent hash")
parser.add_argument('--path', required=True, help="Torrent fullpath")

args = parser.parse_args()

print('@@ Sending First Webhook Notifier')
hook = DiscordWebhook(url=WEBHOOK_URL, content="File will be uploaded\n<@!{}>".format(DISCORD_ID))
embed = DiscordEmbed(title="Torrent Downloaded", color=0xf8c1b8)
embed.add_embed_field(name='Torrent', value=args.name)
embed.add_embed_field(name='Ukuran', value=sizeof_fmt(args.size))
embed.set_footer(text=args.hash)
embed.set_timestamp()
hook.add_embed(embed)
hook.execute()

dummy_args = ['rclone', 'copy', args.path, RCLONE_UPLOAD_DESTINATION]
print('@@ Executing rclone command')
try:
    with subprocess.Popen(dummy_args, stdout=subprocess.PIPE, stderr=subprocess.PIPE) as proc:
        print('@@ Communicating resutls')
        out, err = proc.communicate()
        if int(proc.returncode) == 0:
            print('Return Code Zero: Sending success message')
            hook = DiscordWebhook(WEBHOOK_URL, content="Torrent `{}` uploaded to your cloud storage\n<@!{}>".format(args.name, DISCORD_ID))
            hook.execute()
            print('@@ All process executed, exiting...')
            exit(0)
        print('@@ Non-Zero Code Returned: Sending failed message')
        hook = DiscordWebhook(WEBHOOK_URL, content="Failed when trying to upload `{}` torrent to cloud storage!\n<@!{}>".format(args.name, DISCORD_ID))
        hook.execute()
except Exception as e:
    print('An Exception Occured: ' + e)
    print('Sending failed message')
    hook = DiscordWebhook(WEBHOOK_URL, content="Failed when trying to upload `{}` torrent to cloud storage!\n<@!{}>".format(args.name, DISCORD_ID))
    hook.execute()
