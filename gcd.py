a=int(input('enter frst number::'))
b=int(input('enter secend number::'))
gcd=1

if a>b:
    t=b
else:
    t=a
for i in range(t,1,-1):
    if((a%i == 0) and (b%i == 0)):
        gcd=i
        break

print('GCD::',gcd)