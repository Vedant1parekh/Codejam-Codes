#Code for INDicium 
import numpy as np
from itertools import permutations
t=int(input())
for u in range(0,t):
    l=[]
    l1=[]
    y=[]
    m=0
    l+=[input().split()]
    a=np.array(l,dtype='int')
    N=a[0][0]
    K=a[0][1]
    for i in range(1,N+1):
        for j in range(1,N+1):
            l1.append(j)
    perm=permutations(l1)
    x=list(perm)
    new_arr=[]
    new_arr2=[]
    for i in x:
        s=0
        for j in range(0,N*N):
            if(j%(N+1)==0):
                s=s+i[j]
        if(s==K):
            y.append(i)
        
    for i in range(0,len(y)):
        a=np.array(y[i])
        new_arr.append(a.reshape(N,N))

        x=a.reshape(N,N)
        r=0
        c=0
        for I in range(0,N):
            if len(set(x[I,:]))!=N:
                r+=1
            elif len(set(x[:,I]))!=N:
                c+=1
        if(r==0 and c==0):
            new_arr2.append(x)
            m=1
            break
    if(m==1):
        print('Case #{}: POSSIBLE'.format(u+1))
        print(new_arr2[0])
    else:
        print('Case #{}: IMPOSSIBLE'.format(u+1))