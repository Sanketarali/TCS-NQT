y=int(input(("Enter the year\n")))
if (y%400==0) or (y%4==0 and y%100!=0):
    print(("leap year"))
else:
    print(("Not leap year"))
