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
rrrr=requests.get('https://www.proxyscan.io/download?type=socks4').text
for i in rrrr.splitlines():
    prx.append(i)
rrrrr=requests.get('https://www.proxyscan.io/download?type=http').text
for i in rrrrr.splitlines():
    prx.append(i)    
rrrrrr=requests.get('https://www.proxyscan.io/download?type=https').text
for i in rrrrrr.splitlines():
    prx.append(i)    
rrrrrrr=requests.get('https://www.proxyscan.io/download?type=socks5').text
for i in rrrrrrr.splitlines():
    prx.append(i)    
rrrrrrrr=requests.get('https://www.sslproxies.org/').text
for i in rrrrrrrr.splitlines():
    prx.append(i)    
rrrrrrrrr=requests.get('https://spys.one/en/https-ssl-proxy/').text
for i in rrrrrrrrr.splitlines():
    prx.append(i)    
rrrrrrrrrr=requests.get('https://spys.one/en/socks-proxy-list/').text
for i in rrrrrrrrrr.splitlines():
    prx.append(i)    
rrrrrrrrrrr=requests.get('https://www.proxy-list.download/HTTPS').text
for i in rrrrrrrrrrr.splitlines():
    prx.append(i)    
rrrrrrrrrrrr=requests.get('https://www.proxy-list.download/SOCKS4').text
for i in rrrrrrrrrrrr.splitlines():
    prx.append(i)    
rrrrrrrrrrrrr=requests.get('https://www.proxy-list.download/SOCKS5').text
for i in rrrrrrrrrrrrr.splitlines():
    prx.append(i)
rrrrrrrrrrrrrr=requests.get('https://premiumproxy.net/https-ssl-proxy-list').text
for i in rrrrrrrrrrrrrr.splitlines():
    prx.append(i)
rrrrrrrrrrrrrrr=requests.get('https://proxyscrape.com/free-proxy-list').text
for i in rrrrrrrrrrrrrrr.splitlines():
    prx.append(i)
rrrrrrrrrrrrrrrr=requests.get('https://geonode.com/free-proxy-list').text
for i in rrrrrrrrrrrrrrrr.splitlines():
    prx.append(i)
rrrrrrrrrrrrrrrrr=requests.get('https://advanced.name/freeproxy').text
for i in rrrrrrrrrrrrrrrrr.splitlines():
    prx.append(i)
rrrrrrrrrrrrrrrrrr=requests.get('https://www.scraperapi.com').text
for i in rrrrrrrrrrrrrrrrrr.splitlines():
    prx.append(i)
rrrrrrrrrrrrrrrrrrr=requests.get('http://spys.one/en').text
for i in rrrrrrrrrrrrrrrrrrr.splitlines():
    prx.append(i)
rrrrrrrrrrrrrrrrrrrr=requests.get('https://openproxy.space/list').text
for i in rrrrrrrrrrrrrrrrrrrr.splitlines():
    prx.append(i)
rrrrrrrrrrrrrrrrrrrrr=requests.get('http://free-proxy.cz/en').text
for i in rrrrrrrrrrrrrrrrrrrrr.splitlines():
    prx.append(i)
rrrrrrrrrrrrrrrrrrrrrr=requests.get('http://www.freeproxylists.net').text
for i in rrrrrrrrrrrrrrrrrrrrrr.splitlines():
    prx.append(i)
rrrrrrrrrrrrrrrrrrrrrrr=requests.get('https://spys.one/en/free-proxy-list').text
for i in rrrrrrrrrrrrrrrrrrrrrrr.splitlines():
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