#Code forNESting Depth
t=int(input())
for i in range(0,t):
    l=[]
    s=input()
    n=0
    c=0
    for x in s:
        if(n==0):
            z=int(x)
            for j in range(0,z):
                l.append('(')
                n=n+1
            l.append(x)
        elif(int(x)>n):
            for j in range(0,(int(x)-n)):
                l.append('(') 
            l.append(x)          
        else:
            for j in range(0,z-int(x)):
                l.append(')')
                n=n-1          
            l.append(x)
    if(n!=0):
        for j in range(0,n):
            l.append(')')

    
    ans=''.join([str(item) for item in l ])
    print('Case #{0}: {1}'.format(i+1,ans))