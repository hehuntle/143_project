def number_of_days(year,month):
    
    '''
    function that returns the number of days 
    specified month of specified year
    :param item: input int, int
    :type item: int
    '''
    assert year>0
    assert month>0

    import calendar 
    count=0
    cal= calendar.Calendar()
    for i in cal.itermonthdays(year, month):
        if i != 0:
            count=count+1

    return count
      
def number_of_leap_years(year1, year2):
    
    '''
    function that returns the number of 
    leap days between two specified years
    :param item: input int, int
    :type item: int
    '''  
    
    import calendar

    count=0

    assert year2>year1
    assert year2>0
    assert year1>0

    if year1>year2:
        x=year1
        year1=year2
        year2=x


    for i in range(year1, year2+1):
        if calendar.isleap(i) == True:
            count=count+1
    
    return count
        

def get_day_of_week(year,month,day):
    
    '''
    function the string day of the week when 
    given a year, month, day
    :param item: input int, int, int
    :type item: string
    '''

    assert year>0
    assert month>0
    assert day>0
    
    
    import datetime


    x = datetime.datetime(year, month, day)
    
    return x.strftime("%A")

