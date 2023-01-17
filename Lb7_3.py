import http.client

conn = http.client.HTTPSConnection('beda.pnzgu.ru') 
print(conn)
conn.request("GET", "/anatoly/")
r = conn.getresponse()
print('Proto : ', r.version)
print('Code :', r.status)
print('Status :', r.reason)
print(r.headers)
print(r.read().decode())
conn.close()
