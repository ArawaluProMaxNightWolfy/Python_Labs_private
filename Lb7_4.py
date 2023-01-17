import http.client
def download(f):
    conn.request("GET", '/anatoly/' + f)
    r = conn.getresponse()
    n = r.read()
    f = open('картинка.jpg', 'bw')
    f.write(n)
from html.parser import HTMLParser
class MyParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == 'img':
            for attr in attrs:
                if attr[0] == 'src':
                    global f
                    f = attr[1]
                    return f
parser = MyParser()
conn = http.client.HTTPSConnection("beda.pnzgu.ru")
conn.request('GET', '/anatoly/')
r = conn.getresponse()
parser.feed(r.read().decode())
parser.close()
download(f)
