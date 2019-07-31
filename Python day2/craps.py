from random import randint

money=1000
while monety>0:
    print('你的资产为：',money)
    needs_go_on=False               #是否继续
    while True:                     #正确下注
        debt=int(input('请下注：'))
        if debt>0 and debt <=money:
            break
    first=randint(1,6) + randint(1,6)
    print('玩家摇出了{0}点',first)
    if first ==7 or first ==11:
        print('玩家胜！')
        money+=debt
    elif first==2 or first==3 or first == 12:
        print('庄家胜！')
        money-=debt
    else:
        need_go_on =True
    
    while needs_go_on:
        current = randint(1, 6) + randint(1, 6)
        print('玩家摇出了%d点' % current)
        if current == 7:
            print('庄家胜')
            money -= debt
            needs_go_on = False
        elif current == first:
            print('玩家胜')
            money += debt
            needs_go_on = False

print('你破产了, 游戏结束!')