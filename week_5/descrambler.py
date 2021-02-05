import itertools
w='trleeohelh'
k=(5,5)
values=[]

f=open("/Users/heatherhuntley/Desktop/text.txt")
d={}


for line in f:
    l = [elt.strip() for elt in line.split(',')]
    values.append(l)
merged = list(itertools.chain.from_iterable(values))
length = [len(i) for i in merged]

dictionary = dict(zip(merged, length))

chars = set(w[0:5])
count=0


for key in dict.items():
    if any((c in chars) for c in key):
        print(key)