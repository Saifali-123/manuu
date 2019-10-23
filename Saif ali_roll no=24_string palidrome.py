letter=str(input("enter the string="))
rev=""

for i in letter:
 rev=i+rev
print("reverse string is:",rev)

if(letter==rev):
 print("string is palidrom ")
else:
 print("string letteris not palidrom to:",letter,rev)
