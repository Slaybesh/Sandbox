import urllib.request 
import re
import time


all_links = ''

link_list = re.findall(r'https://d377pvttny04uz.cloudfront.net/t/[^"]+', all_links)
print(len(link_list))

for i, link in enumerate(link_list):
    with open(f'flohossi/{i}.jpg', 'wb') as f:
        f.write(urllib.request.urlopen(link).read())
        time.sleep(0.1)
