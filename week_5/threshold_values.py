



def gather_values(x):

    '''
    this function counts the instance of a key, and appends a 1 or a 0 depending
    on the key value

    :param item: input list
    :type item: dict
    '''
    assert isinstance(x, list)
    
    dict={}
    for i in range(len(x)):
        if x[i] in dict:
            if str(1) in str(x[i]):
                dict[x[i]].append(1)
            else:
                dict[x[i]].append(0)
        else:
            dict.update({x[i]: [0] if x[i]== '00' else [1]})
    
    return dict


def threshold_values(seq, threshold=1):

    '''
    this function counts the instance of a key, and appends a 1 or a 0 depending
    on the key value

    :param item: input dict, int
    :type item: dict
    '''

    seq=gather_values(seq)

    assert isinstance(seq, dict)
    assert isinstance(threshold, int)
    assert (threshold>=1)

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

