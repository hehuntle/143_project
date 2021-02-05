
def fibonacci(n):

    '''
    function that takes int input then returns
    fibonacci sequence up till n
    
    :param item: input int
    :type item: list
    '''

    assert isinstance(n, int)
    assert n>0

    count=2
    F=[None]*n
    F[0]=1
    F[1]=1

    while count<n:
        F[count]=F[count-1]+F[count-2]
        count=count+1

    yield from F

