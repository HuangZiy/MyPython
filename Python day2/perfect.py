for i in range(1,1000):
    sum=0
    m=i
    end=int(i/2)
    for j in range(1,end+1):
        if i%j==0:
            sum+=j
    if m==sum:
        print(m)

