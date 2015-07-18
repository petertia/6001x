##x = [2,1]
##y = [2,1]
##z = False
##if x == y:
##    if sorted(x) == sorted(y):
##         if x.sort() == y.sort():
##               z =  x.sort() == sorted(y)
##print(z)

def isMyNumber(guess):
    guess
    secret_number = -3;
    if guess == secret_number:
        return 0
    elif guess < secret_number:
        return -1
    else:
        return 1

def jumpAndBackpedal(isMyNumber):
    '''
    isMyNumber: Procedure that hides a secret number. 
     It takes as a parameter one number and returns:
     *  -1 if the number is less than the secret number
     *  0 if the number is equal to the secret number
     *  1 if the number is greater than the secret number
 
    returns: integer, the secret number
    ''' 
    
    
    foundNumber = False
    while not foundNumber:
        sign = isMyNumber()
        if sign == -1:
            guess *= 2
            if isMyNumber() == 0:
                return guess
            
        else:
            guess -= 1
            if isMyNumber() == 0:
                return guess
           
    return guess

