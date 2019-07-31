from math import sqrt
num=int(input('请输入一个正整数：'))
end=int(sqrt(num))
flag=True
for x in range(2,end+1):
    if num%x==0:
        flag=False
        break
if flag:
    print('是素数')
else:
    print('不是素数')