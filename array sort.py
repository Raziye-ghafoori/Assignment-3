siz=int(input('enter size:::'))
arry=[]
check=0
print('enter arry::')
while siz>0:
    h=int(input())
    arry.append(h)
    siz-=1


for i in range(len(arry)):
    if i+1 == len(arry):
        break
    elif arry[i]<arry[i+1]:
        check=0
    else:
        check=1
        break

if check==0:
    print('Yes!!')
else:
    print('No!!')
