# A simple lookup python script for discord, using the api: discord-lookup-api
# https://github.com/mesalytic/discord-lookup-api

import requests
import os
from colorama import Fore
from datetime import datetime
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-id", type=str, help="Add user id.")
parser.add_argument("-raw", action="store_true", help="Display raw JSON data")
args = parser.parse_args()

logo = f"""{Fore.LIGHTBLUE_EX}
╔═╗┬┌┬┐┌─┐┬  ┌─┐  ╔╦╗┬┌─┐┌─┐┌─┐┬─┐┌┬┐  
╚═╗││││├─┘│  ├┤    ║║│└─┐│  │ │├┬┘ ││  
╚═╝┴┴ ┴┴  ┴─┘└─┘  ═╩╝┴└─┘└─┘└─┘┴└──┴┘
       ╦  ┌─┐┌─┐┬┌─┬ ┬┌─┐                     
       ║  │ ││ │├┴┐│ │├─┘                     
       ╩═╝└─┘└─┘┴ ┴└─┘┴
       {Fore.RED}|By: Euronymou5|
"""

def user():
    id = args.id
    if os.name == "nt":
       os.system("cls")
    else:
       os.system("clear")
    print(logo)

    r = requests.get(f'https://discordlookup.mesalytic.moe/v1/user/{id}')
    var = r.json()

    if var.get('message') == 'Unknown User':
       print(f'\n{Fore.RED}[!] ERROR: The id is not correct.')
       exit()
    if args.raw:
      print(Fore.GREEN, var)
    else:
      print(f'{Fore.GREEN}\n[-] User: {var["username"]}')
      fecha_dt = datetime.strptime(var["created_at"], "%Y-%m-%dT%H:%M:%S.%fZ")
      fecha_n = fecha_dt.strftime("%d de %B de %Y, %H:%M:%S")
      print(f'[-] Created at: {fecha_n}')
      print(f'[-] Avatar: {var["avatar"]["link"]}')
      print(f'[-] Global Name: {var["global_name"]}')
      print(f'[-] Badges: {var["badges"]}')
      print(f'[-] Banner: {var["banner"]["link"]}. Color: {var["banner"]["color"]}')

if args.id:
   user()
else:
    print(f'{Fore.RED}[!] ERROR: You must enter an ID.\n[~] Example: python3 main.py -id <id>')
    exit()