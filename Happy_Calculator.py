def Plus(a,b):
    return a+b
def Minus(a,b):
    return a-b
def Mult(a,b):
    return a*b

print("======= HAPPY CALCULATOR =======")
print("--------------------------------")
print(">> Press 1 to '+' numbers....")
print(">> Press 2 to '-' numbers....")
print(">> Press 3 to '*' numbers....")
print(">> Press 4 to '/' numbers....")
print(">> Press 5 to '%' numbers....")
print("--------------------------------")
while True:
    ch=int(input(">> Your choice -> "))
    print("--------------------------------")
    if ch<1 or ch>5:
        print(">> ERR.... No such choice.")
        print("--------------------------------")
    else:
        break
n1=float(input(">> Input the 1st number: "))
n2=float(input(">> Input the 2nd number: "))
print("--------------------------------")
if ch==1:
    print(">> Result:",Plus(n1,n2))
    print("--------------------------------")
elif ch==2:
    print(">> Result:",Minus(n1,n2))
    print("--------------------------------")
elif ch==3:
    print(">> Result:",Mult(n1,n2))
    print("--------------------------------")
print("================================")
