list=[]
n=int(input("enter the number of element"))
for i in range(1,n+1):
    num=int(input("enter the element:"))
    list.append(num)
print("element are :",list)
print("maximum number is:",max(list))
print("minimum number is:",min(list))
