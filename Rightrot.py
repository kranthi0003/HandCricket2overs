def rightrot(l,n,x):

    if(n==0):

        l[0]=x

        return l

    else:

        l[n]=l[n-1]
        
	n-=1
        
return rightrot(l,n,x)

m=[]

l=list(map(int,input("Enter the list:\n").split()))

m=l

n=int(input("No.of Rotations:"))

n=n%len(l)

for i in range(n):

    m=rightrot(m,len(m)-1,m[len(m)-1])

print("The updated list is",m)