n=eval(input("Enter the number of names"))
l=[]
p=0
v=0
for i in range(0,n):
    l.append(input("Enter the names"))
s=input("Enter the name to be searched")
for i in l:
    v+=1
    if i==s:
        p=v
print(s," is found in position ",p)            