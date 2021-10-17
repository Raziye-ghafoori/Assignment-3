import random
w_bank=['bank','university','appel','linux','python','os','java','tree']
user_true=[]
w_choos=random.choice(w_bank)
joon=7
a='_'
for x in w_choos:
        print('-',end='')

while True: 
    user_guess=input('\nplese enter your guess::')

    if user_guess in w_choos:
        user_true.append(user_guess)
        for x in range(len(w_choos)):
            if w_choos[x] in user_true:
                print(w_choos[x],end='')
            else:
                print('-',end='')
    else:
        print("❌")
        joon-=1
        for x in range(len(w_choos)):
            if w_choos[x] in user_true:
                print(w_choos[x],end='')
            else:
                print('-',end='')
    
    if joon==0:
        print ("😈Game Over😈")
    
    elif len(w_choos)==len(user_true):
        print("\n👏🎊You Win🎊👏")