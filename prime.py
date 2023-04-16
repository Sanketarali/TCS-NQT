n=int(input("Enter the number\n"))
count=0
i=1
while(i<=n):
    if(n%i==0):
            count=count+1
    i=i+1
if count==2:
    print("Number is prime")
else:
    print("Not a Prime")


