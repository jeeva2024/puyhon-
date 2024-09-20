# sorting a list 
ip = int(input("first enter range of list and enter the list values one by one:"))
L = []
for c in range(ip):
    ele = int(input())
    L.append(ele) 
print("")
print("Your List",L)
print("")
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
print ("Sorted List in Asscending Order",L) 
print("") 
for c in range(len(L)):
    l = L[c]
    idx = c
    count = c
    for d in range(c,len(L)):
        if L[d] > l:
            l = L[d]
            idx = count
        count += 1
    ntmp = L[c]
    L[c] = l
    L[idx] = ntmp
print("Sorted List in Decending Order",L)