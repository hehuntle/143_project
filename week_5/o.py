d={'10': [1, 1, 1, 1, 1],
'11': [1, 1, 1, 1, 1, 1],  
 '01': [1, 1, 1],  
'00': [0, 0, 0, 0, 0, 0]}  



def threshold_values(seq, threshold=1):
    dd={}
    dd=dict(sorted(seq.items()))
    s=[]
    length_dict = {key: len(value) for key, value in dd.items()}
    c=0
    
    while c<threshold:
        p=max(length_dict, key=length_dict.get)
        if str(1) in str(p):
            s.append(p)
            c=c+1
        del length_dict[p]
        
    dd= {key:0 for key in dd}

    for key in dd:
        for i in range(len(s)):
            if key == s[i]:
                dd[key]=1

    return dd



j=threshold_values(d, 3)
print(j)