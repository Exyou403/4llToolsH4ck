#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author imamwawe
# https://t.me/clean_tools_net
import os
import re
import sys
import time
import json
import hashlib
import random
import requests
import subprocess
from colorama import *
import concurrent.futures
from socket import *
from bs4 import BeautifulSoup as bs
init(autoreset=True);R = Fore.LIGHTRED_EX;G = Fore.LIGHTGREEN_EX;C = Fore.LIGHTCYAN_EX;W = Fore.LIGHTWHITE_EX;reset = Fore.RESET
requests.urllib3.disable_warnings()
class Filter:
        def __init__(self):
                self.loop = 0
                self.results = []
        def main(self):
                while True:
                        try:
                                file = open(input("[*] Input file : "), errors="ignore").read().splitlines()
                                break
                        except FileNotFoundError:
                                print (f"[{R}!{W}] File not found")
                                continue
                filter = set(file)
                with open(f"results/filtered.txt", "a+") as output:
                        for target in filter:
                                output.write(f"{target}\n")
                print (f"[ Filtering ] {len(file)} filtered: {len(filter)}", end="")
                input(f"\n[{R}!{W}] Enter back to menu");Wawe().main()

class Ext:
        def __init__(self):
                self.loop = 0
                self.results = []
        def main(self):
                while True:
                        try:
                                file = open(input("[*] Input file : "), errors="ignore").read()
                                break
                        except FileNotFoundError:
                                print (f"[{R}!{W}] File not found")
                                continue
                with open(f"results/domain_extractor.txt", "a+") as output:
                        for site in re.findall(r'(?:[a-zA-Z0-9](?:[a-zA-Z0-9\-]{,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6}', file):
                                if site not in self.results:
                                        self.loop += 1
                                        output.write(f"{site}\n")
                                        self.results.append(site)
                                print (f"\r[ DOMAIN EXTRACTOR ] results: {self.loop}", end="")
                input(f"\n[{R}!{W}] Enter back to menu");Wawe().main()

class Alexa:
        def __init__(self):
                self.bad = 0
                self.loop = 0
        def wawe(self, site):
                try:
                        self.loop+= 1
                        site = re.findall(r"(?:[a-zA-Z0-9](?:[a-zA-Z0-9\-]{,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6}", site)[0]
                        da = re.findall("<td>(.*?)</td>", requests.get(f"https://seo.london/domains-authority-checker/?domain={site}", headers={"user-agent":"Mozilla/5.0 (Linux; Android 10; M2004J19C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Mobile Safari/537.36"}).text)
                        alexa = re.findall("Rank: <oren>(.*?)</oren>", requests.post("https://v1.exploits.my.id/?tools=alexa", data={"url": site,"go":"Check+Rank"}, headers={"user-agent":"Mozilla/5.0 (Linux; Android 10; M2004J19C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Mobile Safari/537.36"}).text)[0]
                        print (f"""\n{W}[{G}*{W}] Website : {site}\n[{G}*{W}] Alexa   : {alexa}\n[{G}*{W}] DA      : {da[1]}\n[{G}*{W}] PA      : {da[2]}""")
                        open(f"results/alexa_da_pa.txt","a+").write(f"{site} alexa : {alexa} da : {da[1]} pa : {da[2]}\n")
                except:pass
        def main(self):
                while True:
                        try:
                                file = open(input("[*] Input file : "), errors="ignore").read().splitlines()
                                break
                        except FileNotFoundError:
                                print (f"[{R}!{W}] File not found")
                                continue
                for site in file:
                        self.wawe(site)
                input(f"\n[{R}!{W}] Enter back to menu");Wawe().main()

class DomtoIP:
        def __init__(self):
                self.ok = 0
                self.bad = 0
                self.loop = 0
                self.list = 0
                self.duplicate = []
        def wawe(self, site):
                try:
                        self.loop+= 1
                        site=re.findall(r"(?:[a-zA-Z0-9](?:[a-zA-Z0-9\-]{,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6}", site)[0]
                        ip=gethostbyname(site)
                        if ip not in self.duplicate:
                                self.ok+=1
                                self.duplicate.append(ip)
                                open(f"results/{self.save}","a+").write(f"{ip}\n")
                except:self.bad+=1;pass
                print (f"\r[DOMAIN TO IP] {self.loop}/{self.list}  {self.ok} IPs", end="")
        def main(self):
                while True:
                        try:
                                file = open(input("[*] Input file : "), errors="ignore").read().splitlines()
                                break
                        except FileNotFoundError:
                                print (f"[{R}!{W}] File not found")
                                continue
                thread = int(input(f"[{R}*{W}] Input thread : "))
                self.save=input(f"[{G}*{W}] Save : ")
                self.list = len(file)
                with concurrent.futures.ThreadPoolExecutor(max_workers=thread) as th:
                        for site in file:
                                th.submit(self.wawe, site)
                print (f"\n[{G}*{W}] Done saved in {self.save}")
                input(f"\n[{R}!{W}] Enter back to menu");Wawe().main()

class Checker:
        def __init__(self, file, saved):
                self.file = file
                self.saved = saved
                self.live = 0
                self.die = 0
                self.loop = 0
        def checker(self, url):
                self.loop += 1
                try:
                        regex = re.findall(r"(?:[a-zA-Z0-9](?:[a-zA-Z0-9\-]{,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6}", url)[0]
                        url = f"http://{regex}"
                        url = requests.get(url, headers={"user-agent":"Mozilla/5.0 (Linux; Android 10; M2004J19C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Mobile Safari/537.36"}, stream=True, verify=False, timeout=4).url
                        url = url.replace('//','/').split('/')
                        url = (f"{url[0]}//{url[1]}")
                        open(f"{self.saved}", "a+").write(f"{url}\n")
                        self.live += 1
                except:self.die += 1;pass
                print (f"\r[ CHECKER ] {self.loop}/{len(self.ekse)}  LIVE : {self.live}, DIE : {self.die}", end="")
        def main(self):
                self.ekse = open(self.file, errors="ignore").read().splitlines()
                thread = int(input("[*] Input thread : "))
                with concurrent.futures.ThreadPoolExecutor(max_workers=thread) as th:
                        [th.submit(self.checker, url) for url in self.ekse]
                input(f"\n[{R}!{W}] Enter back to menu");Wawe().main()

class IPrange:
        def __init__(self):
                self.ips = 0
                self.loop = 0
                self.duplicate = []
        def range(self, ip, type):
                self.loop += 1
                if ip not in self.duplicate:
                        self.duplicate.append(ip)
                        for result in range(1,254+1):
                                self.ips += 1
                                if "1" in type:ip_range = (f"{str(result)}.{ip.split('.')[1]}.{ip.split('.')[2]}.{ip.split('.')[3]}")
                                elif "2" in type:ip_range = (f"{ip.split('.')[0]}.{ip.split('.')[1]}.{ip.split('.')[2]}.{str(result)}")
                                open("results/ip_range.txt","a+").write(f"{ip_range}\n")
                                print (f"\r[IP RANGE] {self.loop}/{self.list}  {self.ips} IPS", end="")
        def main(self):
                print ("""%s
┌─ Mini tools
│  ├── {%s01%s} IP range awalan
│  └── {%s02%s} IP range akhiran
│"""%(W,G,W,G,W))
                type = input("└─ Choice > ")
                file = open(input("[*] Input file : "), errors="ignore").read().splitlines()
                self.list=len(file)
                for ip in file:
                        self.range(ip, type)
                print ("\nDone saved in results/ip_range.txt")
                input(f"\n[{R}!{W}] Enter back to menu");Wawe().main()

class CheckerIP:
        def __init__(self):
                self.good = 0
                self.loop = 0
                self.list = 0
        def wawe(self, ip, port):
                self.loop += 1
                with socket(AF_INET, SOCK_STREAM) as sock:
                        sock.settimeout(3)
                        try:
                                sock.connect((ip, port))
                                self.good += 1
                                open(f"results/GoodIps.txt","a+").write(f"{ip}\n")
                        except:pass
                print (f"\r[CHECKER IPs] {self.loop}/{self.list}  {self.good} IPs", end="")
        def main(self):
                while True:
                        try:
                                file = open(input("[*] Input file : "), errors="ignore").read().splitlines()
                                break
                        except FileNotFoundError:
                                print (f"[{R}!{W}] File not found")
                                continue
                thread = int(input(f"[{R}*{W}] Input thread : "))
                port = int(input(f"[{R}*{W}] Input port, 80 or 443 : "))
                self.list = len(file)
                with concurrent.futures.ThreadPoolExecutor(max_workers=thread) as th:
                        for ip in file:
                                th.submit(self.wawe, ip, port)
                print (f"\n[{G}*{W}] Done saved in GoodIps.txt")
                input(f"\n[{R}!{W}] Enter back to menu");Wawe().main()

class Wawe:
        def __init__(self):
                pass

        def logo(self):
                os.system("cls" if os.name == "nt" else "clear")
                print (f"""{C}
___       ___________       ___________
__ |     / /__    |_ |     / /__  ____/  {W}MINI TOOLS V1.1{C}
__ | /| / /__  /| |_ | /| / /__  __/     {W}© Imamwawe{C}
__ |/ |/ / _  ___ |_ |/ |/ / _  /___     {W}By https://wa.me/628996604524{C}
____/|__/  /_/  |_|___/|__/  /_____/     {W}By t.me/Imamwawe
                                         """)

        def main(self):
                self.logo()
                print ("""%s
┌─ Mini tools
│  ├── {%s01%s} Domain to IP (auto remove duplicate)
│  ├── {%s02%s} IP range
│  ├── {%s03%s} Checker http/s (live or die)
│  ├── {%s04%s} Checker Alexa + DA + PA
│  ├── {%s05%s} Checker IP
│  ├── {%s06%s} Domain Extractor
│  └── {%s07%s} List filter (remove duplicate)
│"""%(W,G,W,G,W,G,W,G,W,G,W,G,W,G,W))
                choice=input("└─ Choice > ")
                if choice =="1" or choice =="01":
                        self.logo();DomtoIP().main()
                elif choice =="2" or choice =="02":
                        self.logo();IPrange().main()
                elif choice =="3" or choice =="03":
                        self.logo()
                        while True:
                                try:
                                        file = input("[*] Input file : ")
                                        open(file)
                                        break
                                except FileNotFoundError:
                                        print (f"[{R}!{W}] File not found")
                                        continue
                        Checker(file,"results/live.txt").main()
                elif choice =="4" or choice =="04":
                        self.logo();Alexa().main()
                elif choice =="5" or choice =="05":
                        self.logo();CheckerIP().main()
                elif choice =="6" or choice =="06":
                        self.logo();Ext().main()
                elif choice =="7" or choice =="07":
                        self.logo();Filter().main()
                else:
                        input(f"[!] Lol, enter back to menu")
                        Wawe().main()
if __name__=="__main__":
        Wawe().main()