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



def tracker(p, limit):
    list=[]
    odd=0
    i=0
    count=0
    x=next(p).seconds
    
    while i< limit:
        if x/2!=0:
            odd=odd+1
        
        yield odd
    '''
    while True:
        if lim:
            limit=lim
        else:
            break
    '''
p = producer()
t=tracker(p,limit=2)
print(list(tracker(p,limit=5)))
#print(t.send(5))
#print(t.send(5))

