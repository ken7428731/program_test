sum=0
for i in range(1,10):
    for j in range(1,10):
        sum=i*j
        print("%d * %d = %d"%(i,j,sum))
        if(j==9):print("\n")
del sum,i,j