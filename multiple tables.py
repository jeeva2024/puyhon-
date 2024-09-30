a = int(input("enter the starting table:"))
b = int(input("enter the ending table:"))
c = int(input("enter the number of bottom:"))
while a <= b:
    for d in range(c+1):
        print(a,'x',d,'=',a*d)
    if a<b:
        print('next table')
    else:
        pass
    a+=1
print('done')