n=int(input("Enter the number"))
sum=0
t=n
while t>0:
    sum=sum+(t%10)**3
    t=t//10
print("sum of cube of digits is",sum)
if sum==n:
  print(n,"is an armstrong number")
else:
   print(n,"is not an armstrong number")  
    