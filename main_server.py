import socket,os,sys,threading,random
from time import sleep 

users = {}

class SERVER:
    def __init__(self):
        self.server_addr = ("localhost",1337)

    def run(self):
        pass

if __name__ == '__main__':
    server = SERVER()
