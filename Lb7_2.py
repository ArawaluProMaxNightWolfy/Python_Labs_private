import socketserver
class MyUDPHandler(socketserver.DatagramRequestHandler):
    names = ['Нефедов','Ковалев','Воронин']
    def handle(self):
        data, socket = self.request
        #self.request.sendto('Введите имя студента: '.encode())
        self.name = data.decode().strip()
        print(self.name, self.client_address)
        if self.name in self.names:
            socket.sendto(f'Привет, {self.name}!\n'.encode(), self.client_address)
        else:
            socket.sendto('Ой\n'.encode(), self.client_address)
with socketserver.UDPServer(('', 7777), MyUDPHandler) as server:
    server.serve_forever()
