c=float(input("Enter cost"))
s=float(input("enter selling price"))
a=0
if c>s:
  a=c-s
  print("total amount lost equals",a)
elif s>c:
  a=s-c
  print("total profit equals",a)
 else:
   print("neither profit nor loss")
