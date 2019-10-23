num1=int(input("Enter the number: "))
print("Prime numbers between", 1, "and", num1, "are:")
for num in range(1, num1 + 1):   
   if num > 1:
       for i in range(2, int(num/2)+1):
           if (num % i) == 0:
               break
       else:
           print(num)
