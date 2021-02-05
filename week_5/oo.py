d={'10': [1, 1, 1, 1, 1],
'11': [1, 1, 1, 1, 1, 1],  
 '01': [1, 1, 1],  
'00': [0, 0, 0, 0, 0, 0]}  




dict=dict(sorted(d.items()))
s=[]
length_dict = {key: len(value) for key, value in dict.items()}
c=0
threshold=2
    
while c<threshold:
    p=max(length_dict, key=length_dict.get)
    if str(1) in str(p):
        s.append(p)
        c=c+1
    del length_dict[p]
        
dict= {key:0 for key in dict}

for key in dict:
    for i in range(len(s)):
        if key == s[i]:
            dict[key]=1



print(dict)

