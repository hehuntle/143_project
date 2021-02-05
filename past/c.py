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
print(next(p).seconds)
print(next(p).seconds)
print(next(p).seconds)
print(next(p).seconds)
print(next(p).seconds)
print(next(p).seconds)
print(next(p).seconds)
print(next(p).seconds)
print(next(p).seconds)
print(next(p).seconds)
print(next(p).seconds)

