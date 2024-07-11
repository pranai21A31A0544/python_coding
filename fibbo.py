def fibbanoic(n,i,a,b,count,l):
    if i==n:
        print(l)
        return 
    count=a+b
    l.append(count)
    a=b
    b=count
    fibbanoic(n,i+1,a,b,count,l)
l=[]
a=0
b=1
l.append(a)
l.append(b)
i=2
print(fibbanoic(6,i,a,b,0,l))

