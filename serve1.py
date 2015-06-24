#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import threading


max_sock = 99 #число подключений
sock = socket.socket()
sock.bind(('', 9090))
sock.listen(max_sock)

users={}

class Client:
    def __init__(self, conn, addr):
        self.data = []
        self.conn = conn
        self.addr = addr
        if "DONE" not in self.conn.recv(1024):#ждать чтобы софтина иницулась и скинула ДОНЕ
            self.conn.close()
            print "all bad"
        self.user_name = self.conn.recv(1024)
        print "hello", self.user_name
        
    def send_msg(self, msg):
        self.conn.send(msg)
        
    def __wait_msg(self):
        while True:
            try:
                data = self.conn.recv(1024)
                if not data:
                    break
                self.data.append(data)
                print data
                self.send_msg(data)
            except Exception as inst:
                a = str(inst)
                if '10054' in a:
                    self.conn.close()
                    print inst
                    del users[self.conn]
                    break
                else:
                    self.conn.close()

        self.conn.close()
        
    def activate(self):
        nus = threading.Thread(target=self.__wait_msg)
        nus.start()

def scan_new_user():
    while True:
        conn, addr = sock.accept()
        print 'connected:', addr
        users[conn] = Client(conn, addr)
        users[conn].activate()
        




s = threading.Thread(target=scan_new_user)
s.start()


#def is_send_to(amsg)
    
    #return name, msg

    #else: return 0




#conn.send(data.upper())#отправляем клиенту conn

#conn.close()

#input()
