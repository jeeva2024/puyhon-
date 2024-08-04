import calendar
import datetime

print('calandar')
a = input("you need 'month' or 'year' calandar:")
if a == 'month':
    b = input("you need 'current calendar' or 'custom calendar':")
    if b == 'current calandar' :
        current1 = datetime.datetime.now().year
        current2 = datetime.datetime.now().month
        print(calendar.month(current1,current2))
    elif b == 'custom calandar':
        year1 = int(input('Enter the year:'))
        month1= int(input('Enter the month in number :')) 
        print(calendar.month(year1,month1))
else:
    c = input("you need 'current calandar' or 'custom calandar':")
    if c == 'current calandar':
        current3 = datetime.datetime.now().year
        print(calendar.calendar(current3))
    elif c == 'custom calandar':
        year2 = int(input('Enter the year:'))
        print(calendar.calendar(year2))
print('Thanking you for using our calandar  :)')