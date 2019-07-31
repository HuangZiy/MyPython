for i in range(100,1000):
    sum=0
    m=i
    while i!=0:
        j=i%10
        sum+=j ** 3
        i=i//10
    if m==sum:
        print(m)

