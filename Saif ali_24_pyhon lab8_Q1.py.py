file=open("data.txt","r")

digits=0
letters=0

for i in file.readline():
    if i.isdigit():
        digits+=1
    elif i.isalpha():
        letters+=1
    else:
        pass
print("digits:",+digits)
print("letters:",+letters)
