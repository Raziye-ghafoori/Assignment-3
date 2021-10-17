enter=int(input('pleas enter your number::'))

i=1
fac=i
while True:
    fac=fac*(i+1)
    if fac==enter:
        print('Yes')
        print(i+1,'!')
        break
    if fac>enter:
        print('No')
        break
    i+=1