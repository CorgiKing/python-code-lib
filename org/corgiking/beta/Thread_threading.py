#！/usr/bin/python3

import threading
import time

exitFlag = 0

class myThread (threading.Thread):
    def __init__(self,threadID,name,counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print("开始线程：" + self.name)
        print_time(self.name,self.counter,5)
        print("退出线程：" + self.name)
        
def print_time(threadName,delay,counter):
    while counter:
        if exitFlag:
            threadName.exist()
        time.sleep(delay)
        print("%s:%s" % (threadName, time.ctime(time.time())))
        counter -= 1
        
thread1 = myThread(1,"thread-1",1)
thread2 = myThread(2,"thread-2",2)

thread1.start()
thread2.start()
thread1.join()
thread2.join()
        
        
        
        
        
        
        
        
        
        
        
        
        
        