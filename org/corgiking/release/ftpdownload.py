from ftplib import FTP

ftp = FTP()

ftp.connect("127.0.0.1",21)
ftp.login("root","root")

# 如果参数 pasv为真，打开被动模式传输 (PASV MODE)
# 在被动模式打开的情况下，数据的传送由客户机启动，而不是由服务器开始。
ftp.set_pasv(0)

# 切换目录
dirpath = "/home/file"
ftp.cwd(dirpath)

# 为下载到本地的文件，创建文件对象
localfile = "d:/demofile.txt"
fw = open(localfile, "wb")

# 下载remotefile文件到localfile
remotefile = "remote.txt"
ftp.retrbinary("RETR %s"%remotefile, fw.write, 1024)

fw.close()
ftp.close()





















input("Press <enter> exit!")
exit()
