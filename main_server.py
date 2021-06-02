import socket,os,sys,threading
from time import sleep
from data.config import config
from data.encryption import encryption

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

    def handle_client(self,client,addr):
        pass

    def home(self):
        try:
            server_sock = self.create_socket()
            self.server_sock = server_sock
        except Exception as e:
            pass
        while True:
            (client,addr) = server_sock.accept()
            handle_client_thread = threading.Thread(target=self.handle_client,args=(client,addr))
            handle_client_thread.start()
#
users = {}
blacklist = {}
#

if __name__ == '__main__':
    os.system("cls") #Windows
    server_CL = SERVER()
    server_CL.home()
