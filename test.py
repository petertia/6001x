##print('Please think of a number between 0 and 100!')
##high_low = input('Is your secret number 50? Enter h to indicate the guess is too high. \
##                 Enter l to indicate the guess is too low. \
##                 Enter c to indicate I guessed correctly. -->')
##
##low = 0.0
##high = 100.0
##ans = 50.0
##reply = 'Is your secret number ' + str(ans) + ' ?'
##
##while high_low != 'c':
##    if high_low == 'h': #if the guess is too high move the higher bound to the current guess
##        high = ans
##        ans = (high + low)/2.0
##        reply = 'Is your secret number ' + str(ans) + ' ?'
##        print(reply)
##        high_low = input('Enter h to indicate the guess is too high. \
##                 Enter l to indicate the guess is too low. \
##                 Enter c to indicate I guessed correctly. -->')
##        
##    elif high_low == 'l': #if the guess is too low move the higher bound to the current guess
##        low = ans
##        ans = (high + low)/2.0
##        reply = 'Is your secret number ' + str(ans) + ' ?'
##        print(reply)
##        high_low = input('Enter h to indicate the guess is too high. \
##                 Enter l to indicate the guess is too low. \
##                 Enter c to indicate I guessed correctly. -->')
##        
##        
##    else:
##        print('I did not understand that input')
##        print(reply)
##        high_low = input('Enter h to indicate the guess is too high. \
##                         Enter l to indicate the guess is too low. \
##                         Enter c to indicate I guessed correctly. -->')
##    
##        
##
##reply = 'Game over. Your secret number was: ' + str(ans)
##print(reply)
##

    
    
##    ans = (high + low)/2.0
##while abs(ans**2 - x) >= epsilon:
##    if ans**2 <x:
##        low = ans
##    else:
##        high = ans
##    ans = (high + low)/2.0



unpaid = 1
while abs(unpaid) > 0.01:
    unpaid = unpaid -.001

print(unpaid)
