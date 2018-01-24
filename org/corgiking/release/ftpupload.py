from ftplib import FTP
import os

localfile = "d:/demo.txt"
remotefile = "upload.txt"

ftp = FTP()

ftp.connect("127.0.0.1", 21)
ftp.login("root", "root")


remotepath = "/home/file"

ftp.cwd(remotepath)

fr = open(localfile, "rb")
print("打开文件：" + os.path.basename(localfile))

# 上传localfile文件到remotefile
ftp.storbinary('STOR %s'%remotefile,fr)

fr.close()
ftp.quit()


















input("Press <enter> exit!")
exit()
