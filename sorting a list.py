# sorting a list 
L = [5,4,8,76,4,-5,3,-6,3,0,-11,234,876,534,1]
for a in range(len(L)):
    m = L[a]
    idx = a
    count = a
    for b in range(a,len(L)):
        if L[b] < m:
            m = L[b]
            idx = count 
        count+=1
    tmp = L[a]
    L[a] = m
    L[idx] = tmp
print (L)  