'''BASIC CALCULATOR - BEGINNER LEVEL'''
     

def calculate():
    a=int(input("\nEnter your first number: "))
    b=int(input("Enter your second number: "))
    op=input("\nEnter any one operand from( + , - , * , / ): ")
    if op=="+":
        print('\nSum is: ',a+b,"\n\n")
    if op=="-":
        print('\nSubtract is: ',a-b,"\n\n")
    if op=="*":
        print('\nProduct is: ',a*b,"\n\n")
    if op=="/":
        print('\nDivision is: ',a/b,"\n\n")
        

while True:
    print(''' BASIC CALCULATOR\n
1. Start
2. Exit\n''')

    ch=int(input("Enter your choice: "))
    if ch==1:
        calculate()
    if ch==2:
        break
           
























        
    

    
