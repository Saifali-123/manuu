num=int(input("enter the number="))
fib1=0
fib2=1
if num<0:
    print("invalid number")
elif num==0:
    print(fib1)
elif num==1:
    print(num)
else:
   print(fib1)
   print(fib2)
   for i in range(2,num+1):
      fib=fib1+fib2
      fib1=fib2
      fib2=fib
      print(fib2)    
