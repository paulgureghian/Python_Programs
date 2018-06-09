# -*- coding: utf-8 -*-
#!/usr/bin/env python 

import socket

s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ainfo = socket.getaddrinfo(None, 8888)

s.bind(ainfo[3][4]) 

s.listen(5)

while True:

    c, addr = s.accept()
    print('Got a request!', addr)
    c.close() 
