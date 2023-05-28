print('Введите число монеток:')
n=int (input())
reshka=0
orel=0
for i in range(n):
    print('0 - orel, 1 - reshka')
    x=int (input())
    if x==1:
        reshka+=1
    else:
        orel+=1
if reshka>orel:
    print(reshka)
else:
    print(orel)

