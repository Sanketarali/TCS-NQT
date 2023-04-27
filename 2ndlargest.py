import math

a=[10,20,30,40,50,15]
first=math.inf
second=math.inf

for i in range(len(a)):
    if a[i]>first:
       a[i]=first
for i in range(len(a)):
    if a[i]!=first and a[i]>second:
        second=a[i]

print(second)

