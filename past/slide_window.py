

def slide_window(x, width, increment):
    

    '''
    function that takes a list of ints, a width, and a increment to 
    shift the window by to produce another list
    
    :param item: input list, int, int
    :type item: str
    '''
    assert width>0
    assert increment>0
    assert isinstance (x,list)
    assert isinstance (width,int)
    assert isinstance (increment,int)
    
    w=width
    inc=increment
    x=x[-1]+1
    listx=[]
    final=[]
    
    L=0
    R=L+w
    while R<=x:
        for i in range(L,R):
            listx.append(i)
    
        L= R-1-inc
        R=L+w
        final.append(listx)
        listx=[]

    final_string ='\n'.join(str(j) for j in final)
    return final_string

print(slide_window(list(range(18)),5,2))
   
