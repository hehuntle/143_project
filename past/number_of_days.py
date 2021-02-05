
def number_of_days(year,month):
    
    '''
    function that returns the number of days 
    specified month of specified year
    :param item: input int, int
    :type item: int
    '''
  
    import calendar 
    count=0
    cal= calendar.Calendar()
    for i in cal.itermonthdays(year, month):
        if i != 0:
            count=count+1

    return count
      


