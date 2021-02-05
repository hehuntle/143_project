compute_average_word_length(instring, unique=False)
{
    if (unique=True)
    {

    }

}

def dup(s):
    #.split removes all of the spaces
    s=s.split()
    #initialize an empty set unique
    unique=[]
    for word in s:
        #check to see if a word is already in the set unique
        if word not in unique:
            #add words to the set unique
            unique.append(word)
    #After every check and possible append add a space.
    #if word is a dup will it give extra spaces? should not
    #but why not
    s=' '.join(unique)


    return ' '.join(dict.fromkeys(s.split()))

