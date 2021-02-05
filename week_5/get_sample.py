
def get_sample(nbits, prob=None, n=1):  
    '''
    this function a num of bits to create my dict of bitstrings, a probability, and a num of random
    dict values to return from my dict of bitstrinfgs.

    :param item: input int, int, int
    :type item: list
    '''
    assert isinstance(nbits, int)
    assert isinstance(n, int)
    assert (nbits>=0)
    assert (nbits>=1)


    import itertools 
    import random
    
    x=[]
    dict={}
    p=[]

    for bits in itertools.product([0,1], repeat=nbits):
        x.append("".join(str(bit) for bit in bits))

    num=len(x)
    
    if prob != None:
        pr=prob
    else :
        pr=round(1/num, 3)

    for i in range(len(x)):
        dict.update({x[i]:pr})

    for i in range(n):
        p.append(random.choice(list(dict)))

    return p

