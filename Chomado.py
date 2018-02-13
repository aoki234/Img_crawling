import requests
from bs4 import BeautifulSoup
from time import sleep
import re
import sys

args = sys.argv
query= args[1]
url="https://search.yahoo.co.jp/image/search?p="+query+"&ei=UTF-8&fr=top_ga1_sa"
images=[]
responses=[]
i=0
pattern = r".gif"

ua=""
#自分のユーザーエージェントを入力
res=requests.get(url,headers={"User-Agent":ua})
bs=BeautifulSoup(res.text,"html.parser")

print(res.status_code)

for link in bs.find_all("img"):# imgタグを取得しlinkに入れる
    if link.get("src"):
        images.append(link.get("src"))# imagesリストに入れる
        print("done")


for target in images:# リストはrequests.getで読めないようなので一旦targetに入れる
    print(target)
    resp = requests.get(target)
    #print(resp)
    responses.append(resp.text)
    sleep(1)
    i+=1
    if re.search(pattern,target):
        print("gif")
    else:
        print("Saved Now")
        with open('img1/' + 'Chomado'+str(i)+".jpg", 'wb') as f:# splitでファイル名を短縮する
            f.write(resp.content)
