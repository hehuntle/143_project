def is_string_integer(input):
    '''
    function that takes string input then returns true if valid digit
    :param item: input char
    :type item: str
    '''

    assert isinstance(input, str)
    assert len(input)==1
    return input.isdigit()

x=is_string_integer('5')
print(x)