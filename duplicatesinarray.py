a=[1,1,2,2,3,4,5]
for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if (a[i]==a[j]):
            print(a[j])

