## Semordnilap

def semordnilap(str1, str2):
    '''
    str1: a string
    str2: a string
    
    returns: True if str1 and str2 are semordnilap;
             False otherwise.
    '''
    if len(str1) == 1 and len(str2) == 1 and str1 == str2:
        return True
    elif len(str1) != len(str2)
        return False
    else:
        if str1[0] == str2[-1]:
            return semordnilap(str1[1:],str2[0:-1])
        else:
            return False
