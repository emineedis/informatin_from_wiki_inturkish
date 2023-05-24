"""it can useful for getting first explanation of the element which you are researching from wikipedi
but it's not fine enough for now . and for turkish language but i explained in english too in the code page.
I m sure maybe there is the preject more useful than mine. but its my first project , my little baby...
it is so special and will stay that for me"""
from bs4 import BeautifulSoup as bsoup
import requests
import re
while True:
    e=str(input("aradığın kelime? "))
    a=e.split(" ")
    print(a)
    url = "https://tr.wikipedia.org/wiki/"
    if len(a)>1:
        for i in a:
            if i==a[len(a)-1]:
                url+=i.lower()
            else:
                url+=i.capitalize()+"_"
    else:
        url="https://tr.wikipedia.org/wiki/"+e.lower()
    result=requests.get(url=url)
    doc=bsoup(result.content,"html.parser")
    tag=doc.p
    print(url)


    try:
        if "Vikipedi'de bu isimde bir madde bulunmamaktadır." in tag.text:
            print("bulamadım")

        elif "{} şu anlamlara gelebilir:".format(e.lower()) in tag.text:
            doce=doc.find("div",class_="mw-parser-output")
            docex=doce.ul.li.text
            print(docex[1:])
        elif "{} ile şu maddeler kastedilmiş olabilir:".format(e.capitalize()) or "{} sözcüğü ile şunlardan biri kastedilmiş olabilir:".format(e.capitalize()) in tag.text:
            doce = doc.find("div", class_="mw-parser-output")
            docex=doce.ul.li.text
            print(docex)
        else:
            print(tag.text)

    except:
        url ="https://sozluk.gov.tr/?//"+ e.lower()
        result = requests.get(url=url)
        doc = bsoup(result.content, "html.parser")
        tag =doc.p
        print(tag)



