n=int(input("enter the number of elements:"))
print("enter the elements:")
list=[]
for i in (0,n):
    ele=int(input())
    list.append(ele)
    print("list of elements=",list)
if ele%2 != 0:
    print(list)
else:
    list.remove(ele)
    print("list of elements without even number=",list)

