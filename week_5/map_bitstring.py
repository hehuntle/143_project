def map_bitstring(x):
    
    '''
    this function takes a list and converts it to an dictionary
    with a value in it dpeending on whether there are more ones 
    or zeros in it

    :param item: input list
    :type item: dict
    '''
    assert isinstance(x, list)

    dict={}
    for i in range(len(x)):
        num_zero=str(x[i].count('0'))
        num_one=str(x[i].count('1'))

        dict.update({x[i]: 0 if num_zero>num_one else 1})
    return dict

