import socket,os,sys,threading
from time import sleep
from data.config import config

class SERVER:
    def __init__(self):
        self.server_ip = config.get('server_ip')
        self.server_addr = (self.server_ip,int(config.get('server_port')))
        self.max_connections = config.get('maximal_connections')

    def create_socket(self):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #TCP
        s.bind(self.server_addr)
        s.listen(int(self.max_connections))
        return s

    def home(self):
        try:
            server_sock = self.create_socket()
        except Exception as e:
            pass
        while True:
            (client,addr) = server_sock.accept()

#
users = {}
blacklist = {}
#

if __name__ == '__main__':
    os.system("cls") #Windows
    server_CL = SERVER()
    server_CL.home()
