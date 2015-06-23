#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import threading
import time

users = []
sock = socket.socket()
sock.bind(('', 9090))
sock.listen(10)

def news_users():
    while 1:
        conn, addr = sock.accept()
        users.append([conn, addr])
        print 'connected:', addr
        t = threading.Thread(target=user1, args=(15, users[-1][0]))
        t.start()


def user1(interval, conni):
    print "+1"
    while True:
        data = conni.recv(1024)
        if not data:
            print 'disconnected:', addr
            conn.close()
            break
        print data
        for i in users:
            i[0].send(data.upper())

nus = threading.Thread(target=news_users)
nus.start()




input()
