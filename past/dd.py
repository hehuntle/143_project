from time import sleep
import random
from datetime import datetime
import itertools as it
 
def producer():
    'produce timestamps'
    starttime = datetime.now()
    while True:
         sleep(random.uniform(0,0.2))
         yield datetime.now()-starttime

p = producer()

def tracker(p, limit):
    list=[]
    odd=0
    i=0

    while i < limit:
        x=next(p).seconds
        if x/2!=0:
            odd=odd+1

        list.append(odd)
        i=odd
    yield list

    while True:
        lim= yield 
        if lim:
            limit=lim
        else:
            break
    

p = producer()
t = tracker(p,limit=3)
print(next(t))
print(t.send(None))
print(t.send(5))
print(t.send(8))
#print((t.send(None)))
print(list(t))
