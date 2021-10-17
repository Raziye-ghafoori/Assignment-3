import random

Size=int(input('enter size of array::'))

number=[]
i= 0
while True:
    enter=random.randint(0,100)
    if enter  not in number:
        number.append(enter)
        i+=1
    if i  == Size:
        break

print(number)  


