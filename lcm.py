def gcd (a,b):
    
    gcd=1

    if a>b:
        t=b
    else:
        t=a
    for i in range(t,1,-1):
        if((a%i == 0) and (b%i == 0)):
            gcd=i
            break

    return gcd

a=int(input('enter frst number::'))
b=int(input('enter secend number::'))

lcm=(a*b)//(gcd(a,b))

print('LCM::',lcm)