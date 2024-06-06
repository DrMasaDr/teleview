import requests, re
from multiprocessing.dummy import Pool
from os import system
from user_agent import generate_user_agent


system("title " + f"TeleView By @program_masa")
print('''

         By: [  @Dr_Masa_Dr / @program_masa ]                         

''')
link = input(' \033[1;36m [/] Enter your url: ').strip().replace('https://', '').replace('http://', '')

main_url = f'https://{link}?embed=1'
views_url = 'https://t.me/v/?views='

sent, bad_proxy, done, next_proxy = 0, 0, 0, 0





def send_views(proxy):
    global sent, bad_proxy, done, next_proxy
    while True:
        try:
            session = requests.session()
            session.proxies.update({'http': f'http://{proxy}', 'https': f'http://{proxy}'})
            session.headers.update({
            'accept-language': 'en-US,en;q=0.9',
            'user-agent': generate_user_agent(),
            'x-requested-with': 'XMLHttpRequest'
            })
            main_res = session.get(main_url).text
            _token = re.search('data-view="([^"]+)', main_res).group(1)
            views_req = session.get(views_url + _token,timeout=3)
            print(' \033[1;32m [+] View Sent ' + 'Stats Code: '+str(views_req.status_code))
            sent += 1
            done += 1
            tit()

        except:
            print('\033[1;31m [x] Bad Proxy: ' + proxy)
            bad_proxy += 1
            done += 1
            tit()


prx=[]
r=requests.get('https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all').text
for i in r.splitlines():
    prx.append(i)
rr=requests.get('https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout=10000&country=all').text
for i in rr.splitlines():
    prx.append(i)
rrr=requests.get('https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all').text
for i in rrr.splitlines():
    prx.append(i)

bedwbara=[]
bekeshahamui=[]
for ii in prx:
    if str(ii) in bedwbara:pass
    else:
        bekeshahamui.append(ii)
        bedwbara.append(ii)
def tit(): system("title " + f" /  -- Sent: {sent} --  Bad proxies: {bad_proxy}")
proxy = [items.strip() for items in bekeshahamui]
pool = Pool(int(200))
pool.map(send_views,proxy)
pool.close()
pool.join()
