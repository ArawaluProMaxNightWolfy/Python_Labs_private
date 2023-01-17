import http.client
def load(f, i):
    conn.request("GET", '/anatoly/' + f)
    r = conn.getresponse()
    n = r.read()
    f = open(i+'-картинка.jpg', 'bw')
    f.write(n)  
from html.parser import HTMLParser
class pars_str(HTMLParser):
    global a
    a = []

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for attr in attrs:
                if attr[0] == 'href': a.append(attr[1])
            return a   
class MyParser_foto(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == 'img':
            global s

        for attr in attrs:
            if attr[0] == 'src':
                s = (attr[1])
                return s 
            else:
                s = None
                return s
parser1 = pars_str()
conn = http.client.HTTPSConnection("beda.pnzgu.ru")
conn.request('GET', '/anatoly/')
r = conn.getresponse()
parser1.feed(r.read().decode())
parser1.close()
for i in range(len(a)):
    parser2 = MyParser_foto()
    conn.request('GET', '/anatoly/'+a[i])
    t = conn.getresponse()
    parser2.feed(t.read().decode())
    parser2.close()
    if s != None:
        load(s,str(i + 2))    
