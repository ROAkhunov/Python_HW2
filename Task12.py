print ('введите сумму чисел:')
s=int(input())
print('введите произведение чисел')
p=int(input())
x=1
flag=True
while x<1000 and flag==True:
    if p%x==0:
        if x+p/x==s:
            print(x,int(p/x))
            flag=False
        else:
            x+=1
    else:
        x+=1

