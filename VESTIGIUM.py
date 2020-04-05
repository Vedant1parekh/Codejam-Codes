import numpy as np
t=int(input())
for x in range(0,t):
    l=[]
    r=0
    c=0
    n=int(input())
    for j in range(n):
        l+=[input().split()]
    a=np.array(l,dtype='int')
    for i in range(n):
        if len(set(a[i,:]))!=n:
            r+=1
        elif len(set(a[:,i]))!=n:
            c+=1
    print('Case #{0}: {1} {2} {3}'.format(x+1,a.trace(),r,c))