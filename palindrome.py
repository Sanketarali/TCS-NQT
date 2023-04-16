i=int(input("Enter the number\n"))
rev=0
x=i
while(i>0):
    rev=(rev*10)+i%10
    i=i//10
print("Reverse =",rev)
if(x==rev):
    print("Palindrome")
else:
    print("Not Palindrome")


 