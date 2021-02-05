def number_of_leap_years(year1, year2):
    
    '''
    function that returns the number of 
    leap days between two specified years
    :param item: input int, int
    :type item: int
    '''  
    
    import calendar

    count=0

    if year1>year2:
        x=year1
        year1=year2
        year2=x


    for i in range(year1, year2+1):
        if calendar.isleap(i) == True:
            count=count+1
    
    return count
        
