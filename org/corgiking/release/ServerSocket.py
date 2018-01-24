import socket

# 创建socket
serversk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 获取本地主机名
host = socket.gethostname()

# 绑定端口
serversk.bind(("localhost",5019))

# 设置最大连接数
serversk.listen(5)

while True:
    # 建立客户端连接
    clientsk,addr = serversk.accept()

    print("连接地址：%s" % str(addr))

    msg = "Hello Corgi King !"
    clientsk.send(msg.encode('utf-8'))
    clientsk.close()
    



input("Press <enter> exit!")
exit()
