print("\t\t\t************** Saif ali_Rollno=24*************")
file=open("integer.txt","r")

for num in file:
    
    if int(num)%2==0:
            f1=open("even.txt","a")
            f1.write(num)
            f1.close()
    else:
            f2=open("odd.txt","a")
            f2.write(num)
            f2.close()
file.close()
print("file element are:")
f=open("integer.txt","r")
print(f.read())
print("even file element are:")
f1=open("even.txt","r")
print(f1.read())
print("odd file element are: ")
f2=open("odd.txt","r")
print(f2.read())
f.close()
f1.close()
f2.close()
        
