def compute_sum_to_n(n):
    '''
    function that computes sum of all non neg num up to n
    
    :param item: input int
    :type item: int
    '''

    assert isinstance(n, int)
    
    if n>=0 :
        set=list(range(1,n+1))
        print(set)
        return sum(set)
    else :
        return 0

