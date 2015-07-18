## Bisection Recursion
## currently does not work when the char is the last one in aStr


def isIn(char, aStr):
    if aStr == '':
        return False
    elif char == aStr[int(len(aStr)/2)]:
        return True
    else:
        if char < aStr[int(len(aStr)/2)]:
            print(aStr)
            return isIn(char, aStr[0:int((len(aStr))/2)])
            
        else:
            print(aStr)
            return isIn(char, aStr[int(len(aStr)/2):-1])
            
