## Pset 3
## area summation under curve
##def f(x):
##    import math
##    return 10*math.e**(math.log(0.5)/5.27 * x)
##
##def radiationExposure(start, stop, step):
##    i = start
##    rad_exp = 0
##    while i < stop:
##        
##        base = i
##        area = step*f(base)
##        rad_exp = rad_exp + area
##        i = i+ 1*step
##
##    return rad_exp



##def isWordGuessed(secretWord, lettersGuessed):
##    
##    word_copy = []
##    for char in secretWord:  
##        word_copy.append(char)
##
##
##    i = 0
##    while i < len(lettersGuessed):
##               
##        if lettersGuessed[i] in secretWord:
##            while lettersGuessed[i] in word_copy:
####                print(lettersGuessed[i])
####                print(secretWord)
##                word_copy.remove(lettersGuessed[i])
##
####            print(word_copy)
##            
##            i = i+1
##        else:
##            i = i+1
##
##    if len(word_copy) > 0:
##        return False
##    else:
##        return True


##def getGuessedWord(secretWord, lettersGuessed):
##    
##    word_copy = secretWord
##
##    i = 0
##    while i < len(secretWord):
####        print(i)   
##        if secretWord[i] not in lettersGuessed:
##
##            word_copy = word_copy.replace(secretWord[i], '_ ')
##
####            print(word_copy)
##            
##            i = i+1
##        
##        else:
##            i = i+1
##
##    return word_copy

def getAvailableLetters(lettersGuessed):

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_copy = []
    for char in alphabet:
        alphabet_copy.append(char)
    for i in lettersGuessed:
            alphabet_copy.remove(i)

    alphabet_string = ''.join(alphabet_copy)
    return alphabet_string
