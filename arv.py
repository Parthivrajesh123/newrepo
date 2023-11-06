nn=int(input("enter the number of subjects:"))
eng=int(input("enter the marks for english"))
acc=int(input("enter the marks for accountancy"))
bs=int(input("entrer the marks for business studies"))
eco=int(input("enter the marks for economics"))
ip=int(input("enter thde marks of infromatic practices"))
total=eng+acc+bs+eco+ip
avg=total/nn
print("the average is:",avg)
if avg>=90 and avg<=100:
  gr="A1"
elif avg>=80 and avg<=89:
  gr="A2"
elif avg>=70 and avg<=79:
  gr="B1"
print("average grade is:",gr)  
