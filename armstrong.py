enter=int(input('pleas enter your number::'))

h=enter
size=len(str(enter))
j=0
while h>0:
    temp=h%10
    j=j+temp**size
    h//=10
   

if j==enter:
    print('Yes')
else:
    print('No')