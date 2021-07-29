import requests
from bs4 import BeautifulSoup

def get_entries(url):

    soup = BeautifulSoup(url.content, 'html.parser')
    links = soup.findAll('div', class_='entry')

    entries = []

    for link in links:
        print(link)
        entry=(link.find('div',class_='entry-p').text)
        up=(link.find('span',{'class':['oylar arti_sayi', 'oylar arti_sayi color-yesil']}))
        down=(link.find('span',{'class':['oylar eksi_sayi', 'oylar eksi_sayi color-kirmizi']}))
        entries.append({"entry":entry})

        if(up == None):
            entries.append({"up": 'Olumlu Oylama Yok'})
        else:
            entries.append({"up":up.text})
        if(down == None):
            entries.append({"down": 'Olumsuz Oylama Yok'})
        else:
            entries.append({"down":down.text})
        
        print(entries)

    with open("text.txt",'w') as f:
        for option in entries:
            f.write('%s' % option)
            f.write('\n')

for x in range(1,11):
    url = requests.get("https://www.uludagsozluk.com/k/recep-tayyip-erdo%C4%9Fan/"+str(x)+"/")
get_entries(url)
