 # Finding compound intrest
print('compound intrest')
p = int(input('Enter the ammount you borrowed:'))
n = int(input('Enter the number of years:'))
r = int (input('Enter the rate of intrest:'))
CI  = (p*(1+r/100)**n)-p
print('CI',CI)
