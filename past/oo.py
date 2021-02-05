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

list=[]
odd=0
limit=10
i=0
while i < limit:
    x=next(p).seconds
    if x/2!=0:
        odd=odd+1

    list.append(odd)
    i=odd

    

print(list)

