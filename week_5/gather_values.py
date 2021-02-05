


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




 
