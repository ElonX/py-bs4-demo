from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html, "html.parser")
_table = bsObj.find("table",{"id":"giftList"})
first_tr = _table.tr

index = 0
for _tr1 in first_tr.next_siblings:
    try:
        text = _tr1.find_all('td')[2].get_text()
        text = text.strip()
        print(text)
    except AttributeError as e:
        print(index)
        continue
    finally:
        index += 1


    
    
