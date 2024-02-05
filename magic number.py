n=int(input("Enter the number"))
sum=0
t=n
while t>0:
    sum=(t%10)+sum
    t=t//10
    if sum>9:
        t=sum
        sum=0

if sum==1:
    print(n,"is a magic number")
else:
    print(n,"is not a magic number")
