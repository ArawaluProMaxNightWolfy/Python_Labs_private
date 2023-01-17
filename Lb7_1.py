import socketserver
class MyTCPHandler(socketserver.StreamRequestHandler):
    names = ['Нефедов','Ковалев','Воронин']
    def handle(self):
        self.request.send('Введите имя студента: '.encode())
        self.name = self.request.recv(1024).decode().strip()
        print(self.name)
        if self.name in self.names:
            self.request.send(f'Привет, {self.name}!\n'.encode())
        else:
            self.request.send('Ой\n'.encode())
with socketserver.TCPServer(('', 7777), MyTCPHandler) as server:
    server.serve_forever()
        