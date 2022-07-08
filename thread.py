import threading
from threading import *
from time import sleep

class Sahithi(Thread):
    def run(self):
        for i in range(1,11):
            print(i,'thread 1')
            sleep(2)

class Priya(Thread):
    def run(self):
        for i in range(1,11):
            print(i,"thread 2")
            sleep(2)

obj = Sahithi()
obj.start()
sleep(1)

obj1 = Priya()
obj1.start()