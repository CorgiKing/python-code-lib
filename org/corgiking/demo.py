#coding=utf-8

import socket

print ('hello world!')

sk = socket.socket()
sk.connect(("192.168.7.4",8728))
print (U"192.168.7.4连接成功")


cmd = bytearray([6, 47, 108, 111, 103, 105, 110, 0])
sk.send(cmd)
ret = sk.recv(1024)
print (ret)




input("Press <enter> exit!")
exit()
