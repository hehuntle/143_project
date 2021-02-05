
def compute_average_word_length(instring,unique=True):

    '''
    function that takes string input then returns average value of words
    in the string
    if unique= True, exclude duplicate words of string from average calc

    :param item: input string, bool
    :type item: 
    '''
    
    val=0;
    if unique==False:
        instring=instring
        words=instring.split()
    elif unique == True:
        instring=instring.split()
        words=[]
        for i in instring:
            if i not in words:
                words.append(i)
        
    for word in words:
        val=val+len(word)
    
    average_length = val/ len(words)
    return average_length

