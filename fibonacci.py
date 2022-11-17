n=int(input("enter the number of terms:"))
count=1
n1=0
n2=1
if n<=0:
    print("negative number!!")
elif n==1:
    print("thr fibonacci series upto",n1)
    print(n1)
else:
    print("the fibonacci series of the number is")
    while count<=n:
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        count=count+1
