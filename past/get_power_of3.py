
def get_power_of3(n):

    '''
    function that takes int input then returns weights for list to sum to 
    input value
    
    :param item: input int
    :type item: list
    '''

    for a in range(-1,2):
        for b in range(-1,2):
            for c in range(-1,2):
                for d in range(-1,2):
                    print(a,b,c,d)
                    sum=1*a+3*b+9*c+27*d
                    if sum == n:
                        w=[a,b,c,d]
                        return w
                    else:
                        pass

p=get_power_of3(8)
print(p)