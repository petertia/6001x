##def myLog(x, b):
##
##    result = 0
##    power = 0
##    while result < x:
##        power = power + 1
##        
##        result =  b**(power)
##      
##    if result <= x:
##        return power
##    else:
##        return power - 1

    
##def laceStrings(s1, s2):
##    word_copy = list(s1)
##    word_copy2 = list(s2)
##    i = 0
##    new_word = []
##    if len(s1) == len(s2):
##        while i < max(len(s1), len(s2)):
##            new_word.append(word_copy[i])
##            new_word.append(word_copy2[i])
##            i = i+1
##    elif max(len(s1), len(s2)) == len(s1):
##        while i < len(s1):
##            while i <  len(s2):
##                new_word.append(word_copy[i])
##                new_word.append(word_copy2[i])
##                i = i+1
##            new_word.append(word_copy[i])
##            i = i + 1
##    else:
##        while i <  len(s2):
##            while i <  len(s1):
##                new_word.append(word_copy[i])
##                new_word.append(word_copy2[i])
##                i = i + 1
##            new_word.append(word_copy2[i])
##            i = i+1
##    answer = ''.join(new_word)    
##    return answer


##def laceStringsRecur(s1, s2):
##    """
##    s1 and s2 are strings.
##
##    Returns a new str with elements of s1 and s2 interlaced,
##    beginning with s1. If strings are not of same length, 
##    then the extra elements should appear at the end.
##    """
##    def helpLaceStrings(s1, s2, out):
##        if s1 == '':
##            return s2
##        if s2 == '':
##            return s1
##        else:
##            return s1[0] + s2[0] +helpLaceStrings(s1[1:], s2[1:], out)
##    return helpLaceStrings(s1, s2, '')


def McNuggets(n):
    """
    n is an int

    Returns True if some integer combination of 6, 9 and 20 equals n
    Otherwise returns False.
    """
    if n % 6 == 0:
        return True
    elif n % 9 == 0:
        return True
    elif n % 20 == 0:
        return True
    elif n % 15 == 0:
        return True
    elif n % 26 == 0:
        return True
    elif n % 29 == 0:
        return True   
    elif n % 20 == 6 or n % 20 == 12 or n % 20 == 9 or n % 20 == 18 or n % 20 == 15:
        return True
    elif n % 9 == 6:
        return True
    else:
        return False
