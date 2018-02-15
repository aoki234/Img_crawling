import requests
from bs4 import BeautifulSoup
from time import sleep
import re
import sys
import os

args = sys.argv
query= args[1]
#url="https://search.yahoo.co.jp/image/search?p="+query+"&ei=UTF-8&fr=top_ga1_sa"
#url="https://search.yahoo.co.jp/image/search?p="+query+"&ei=UTF-8&save=0"
url="https://search.yahoo.co.jp/image/search?p="+query+"&rkf=1&dim=&ctype=&imw=0&imh=0&imc=&ei=UTF-8&xargs=7&b=0"
images=[]
responses=[]
pattern = r".gif"

cwd=os.getcwd()
if os.path.exists(query):
    print("Directory is already OK")
else:
    os.mkdir(query)

i = 0

def getImage(url):
    print(url)
    global i
    ua=""
    #自分のユーザーエージェントを入力
    res=requests.get(url,headers={"User-Agent":ua})
    bs=BeautifulSoup(res.text,"html.parser")

    #print(res.status_code)
    idc=bs.find(id="gridlist")
    for link in idc.find_all("img"):# imgタグを取得しlinkに入れる
        if link.get("src"):
            images.append(link.get("src"))# imagesリストに入れる
            #print("done")

    if i<1 :
        print("first page")
        i=i+1
        rein=bs.find("div",id="Sp1")
        for next in rein.find_all("a"):
            #print(next)
            if next.get("href"):
                print(next.get("href"))
                responses.append(next.get("href"))

    else:
        for target in images[-20:-1]:# リストはrequests.getで読めないようなので一旦targetに入れる
            resp = requests.get(target)
            #print(resp)
            sleep(1)
            i=i+1
            if re.search(pattern,target):
                print("gif")
            else:
                print("Saved Now")
                with open(str(query)+'/' +str(query)+str(i)+".jpg", 'wb') as f:# splitでファイル名を短縮する
                    f.write(resp.content)


if __name__ == '__main__':
    getImage(url)
    getImage(url)
    for (h,page) in enumerate(responses):
        if h<10:
            print(h)
            print("go to Next page")
            getImage(page)
        else:
            print("finished")
