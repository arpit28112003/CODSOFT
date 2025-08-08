import random


smll = "abcdefghijklmnopqrstuvwxyz"
cap = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num = "1234567890"
smbl = "!@#$%&*?_+-=."


def func():
    print("\nYou can adjuist the complexity of the Password by changing the length according to You:- \n")
    len_cap = int(input("Enter the Number of Capital letters in your Password: "))
    len_smll = int(input("Enter the Number of Small letters in your Password: "))
    len_smbl = int(input("Enter the Number of Symbol in your Password: "))
    len_num = int(input("How much the Numbers in your Password have: "))


    pswd1 = ""
    pswd2 = ""
    pswd3 = ""
    pswd4 = ""
    pswd5 = ""


    for i in range(len_cap):
        pswd1 = pswd1 + random.choice(cap)
        pswd2 = pswd2 + random.choice(cap)
        pswd3 = pswd3 + random.choice(cap)
        pswd4 = pswd4 + random.choice(cap)
        pswd5 = pswd5 + random.choice(cap)

    for i in range(len_smll):
        pswd1 = pswd1 + random.choice(smll)
        pswd2 = pswd2 + random.choice(smll)
        pswd3 = pswd3 + random.choice(smll)
        pswd4 = pswd4 + random.choice(smll)
        pswd5 = pswd5 + random.choice(smll)

    for i in range(len_smbl):
        pswd1 = pswd1 + random.choice(smbl)
        pswd2 = pswd2 + random.choice(smbl)
        pswd3 = pswd3 + random.choice(smbl)
        pswd4 = pswd4 + random.choice(smbl)
        pswd5 = pswd5 + random.choice(smbl)

    for i in range(len_num):
        pswd1 = pswd1 + random.choice(num)
        pswd2 = pswd2 + random.choice(num)
        pswd3 = pswd3 + random.choice(num)
        pswd4 = pswd4 + random.choice(num)
        pswd5 = pswd5 + random.choice(num)



    print("\nYou can choose one from these:-\n",pswd1,"\n",pswd2,"\n",pswd3,"\n",pswd4,"\n",pswd5,"\n")

print("               --- PASSWORD GENERATOR ---\n")

func()

while True:
    print('''---------------------------
1. More Passwords
2. Exit''')

    ch=int(input("Enter your choice: "))
    if ch==1:
        func()
    if ch==2:
        break
           












