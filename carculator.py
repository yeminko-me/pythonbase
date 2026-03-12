x=input("Enter first number:")
y=input("Enter second number:")
op=input("Enter the operator(+-*/):")
try :
    x=int(x)
    y=int(y)
    output=True
    if op=="+":
      result=x+y
    elif op=="-":
       result=x-y
    elif op=="*":
       result=x*y
    elif op=="/":
       result=x/y
    else :
     output=False
     print("Wrong Operator")
    if output:
       print ("Result is",result)
    

except ValueError:
    print("Please enter the only number:")
    print(ValueError);
