##balance = 4213
##annualInterestRate = .2
##monthlyPaymentRate = .04
##numberMonths = 12
##i = 0
##totalPaid = 0
##
##while i < numberMonths:
##    minMonthPay = balance*monthlyPaymentRate
##    balance = (balance - minMonthPay)* (1 + annualInterestRate/12)
##    i += 1
##    totalPaid = totalPaid + minMonthPay
##    print('Month:' + str(i))
##    print('Minimum monthly payment: ' + str(round(minMonthPay,2)))
##    print('Remaining balance: ' + str(round(balance,2)))
##    
##print('Total paid: ' + str(round(totalPaid,2)))
##print('Remaining balance: ' + str(round(balance,2)))


##balance = 3329
##annualInterestRate = .2
##minMonthPay = 10
##totalPaid = 0
##unpaid = balance
##numberMonths = 12
##while unpaid > 0:
##    i = 0
##    minMonthPay = minMonthPay + 10
##    print(minMonthPay)
##    print(i)
##    print('balance is ' + str(balance))
##    unpaid = balance
##    totalPaid = 0
##    while i < numberMonths:
##
##        
##        unpaid = (unpaid - minMonthPay)* (1 + annualInterestRate/12)
##        i += 1
##        totalPaid = totalPaid + minMonthPay
##        print('totalPaid is ' + str(totalPaid))
##        print('unpaid is ' + str(unpaid))
##
##print('Lowest Payment: ' + str(minMonthPay))
##

## Bisection method
balance = 320000
annualInterestRate = .2

lowerBound = balance/12
upperBound = (balance*(1 + annualInterestRate/12.0)**12)/12
totalPaid = 0
unpaid = balance
numberMonths = 12
ans =  (upperBound + lowerBound)/2.0
while abs(unpaid) > 0.01:
    i = 0
    unpaid = balance
    
    while i < numberMonths:
        unpaid = (unpaid - ans)* (1 + annualInterestRate/12)
        i += 1
        totalPaid = totalPaid + ans
##        print('totalPaid is ' + str(totalPaid))
##        print('unpaid is ' + str(unpaid))
##    print(unpaid)
##    print('upper is' + str(upperBound))
##    print('lower is' + str(lowerBound))

    if unpaid > 0:
        lowerBound = ans
##        print('lower is' + str(lowerBound))
        ans = (upperBound + lowerBound)/2.0
    else:
        upperBound = ans
##        print('upper is' + str(upperBound))
        ans = (upperBound + lowerBound)/2.0
##    print(ans)
##    print('balance is ' + str(balance))
    
    totalPaid = 0
##    print(unpaid)
print('Lowest Payment: ' + str(round(ans,2)))
