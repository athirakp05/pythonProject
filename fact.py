num=int(input("enter a number"))
fact=1
if num<= 0:
    print("no factorial for these numbers!!")
else:
    for i in range(1,num+1):
        fact=fact*i
    print("factorial of a number=",fact)
