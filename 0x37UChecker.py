# https://t.me/clean_tools_net
import requests
from colorama import Fore,init
import os
init(autoreset=True)

G = Fore.GREEN
R = Fore.RED
Y = Fore.LIGHTYELLOW_EX
C = Fore.LIGHTCYAN_EX
S = requests.session()
try:
    os.system("cls")
    os.system("title [~] PHP Mailers Checker By 0x37U [~]")
except:
    os.system("clear")
def banner():
    print(Fore.LIGHTRED_EX+"\t\t ██████╗ ██╗  ██╗██████╗ ███████╗██╗   ██╗")
    print(Fore.LIGHTRED_EX+"\t\t██╔═████╗╚██╗██╔╝╚════██╗╚════██║██║   ██║")
    print(Fore.LIGHTRED_EX+"\t\t██║██╔██║ ╚███╔╝  █████╔╝    ██╔╝██║   ██║")
    print(Fore.LIGHTRED_EX+"\t\t████╔╝██║ ██╔██╗  ╚═══██╗   ██╔╝ ██║   ██║")
    print(Fore.LIGHTRED_EX+"\t\t╚██████╔╝██╔╝ ██╗██████╔╝   ██║  ╚██████╔╝")
    print(Fore.LIGHTRED_EX+"\t\t ╚═════╝ ╚═╝  ╚═╝╚═════╝    ╚═╝   ╚═════╝ ")
    print("\t\t\t\tgithub.com/0x37U")
    print("\t\t\t\tTelegram : @x0x37U")

banner()
Email = str(input("Your Mail : ").strip())

File = open(input("Mailers List >").strip(),"r").read().split("\n")


header = {
    'User-Agent':'Mozilla/5.0(WindowsNT6.3;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/93.0.4577.63Safari/537.36',
    "Cookie": ""
}
def send(Url):
    data = {
            "action": "score",
            "senderEmail": "no-reply@0x37U.com",
            "senderName": "=?UTF-8?B?MHgzN1U=",  
            "attachment[]": "(binary)",
            "replyTo": "",
            "subject": "=?UTF-8?B?TWFpbGVyIElzIFdvcms=",
            "messageLetter": f"<h1>Working</h1><br><h4>Mailer : {Url}</h4>",
            "emailList": Email,
            "messageType": "1",
            "charset": "UTF-8",
            "encode": "8bit",
            "action": "send",
        }
    try:
        response = S.post(Url,data=data,headers=header)
        if "Ok" in response.text:
            print( G + "[Success] " +Fore.RESET + f"{Url}"+G+ " Check Your Inbox/Spam")
        else:
            print(R +"[Falid] " +Fore.RESET + f"{Url}")
    except:
        pass
for List in File:
    send(List)