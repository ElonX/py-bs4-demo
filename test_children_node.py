from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html, "html.parser")
_table = bsObj.find("table",{"id":"giftList"})
first_tr = _table.tr


print("-------------------1")
for _tr2 in _table.children:
    print(_tr2)
print("-------------------2")
for _tr2 in _table.children:
    for _td2 in _tr2:
        print(_td2)
        print("--")
print("-------------------3")
for _tr1 in first_tr.next_siblings:
    try:
        text = _tr1.find_all('td')[2].get_text()
        print(text)
    except AttributeError as e:
        continue
    
print("-------------------4")
for _tr1 in first_tr.next_siblings:
    for _td2 in _tr1:
        try:
            print(_td2.get_text())
            print("----")
        except AttributeError as e:
            continue

