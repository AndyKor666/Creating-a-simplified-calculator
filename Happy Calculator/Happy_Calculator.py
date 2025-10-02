
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
    if ch<0 or ch>5:
        print(">> ERR.... No such choice.")
        print("--------------------------------")
    else:
        break
n1=float(input(">> Input the 1st number: "))
n2=float(input(">> Input the 2nd number: "))
print("--------------------------------")