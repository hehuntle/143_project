
def get_day_of_week(year,month,day):
    
    '''
    function the string day of the week when 
    given a year, month, day
    :param item: input int, int, int
    :type item: string
    '''
    
    
    import datetime


    x = datetime.datetime(year, month, day)
    
    return x.strftime("%A")

