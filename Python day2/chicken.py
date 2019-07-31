g=100//5
m=100//3
for i in range(0,g):
    for j in range(0,m):
        k=100-i-j
        if 5*i+3*j+k/3==100:
            print('公鸡={0} 母鸡={1} 小鸡={2}',i,j,100-i-j)
