'''Rock Paper Scissors Game in Python'''



import random

print('''\n                           Welcome to Rock, Paper, Scissors!!''')

def func():
    user = input("\nChoose One [Rock, Paper, Scissors] :   ")

    opt = ["Rock","Paper","Scissors"]
    comp = random.choice(opt)
    print("\nComputer's Choice: ",comp)


    if(user == comp):
        print("Tie!")

    elif(user == "Rock" and comp == "Scissors")or(user == "Scissors" and comp == "Paper")or(user == "Paper" and comp == "Rock"):
        print("\nYOU WIN!")

    else:
        print("\nYOU LOSE!")

func()

while True:
    print('''\n
1. Play again
2. Exit''')

    ch=int(input("Enter your choice: "))
    if ch==1:
        func()
    if ch==2:
        break
           
