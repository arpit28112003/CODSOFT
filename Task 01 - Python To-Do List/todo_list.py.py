'''A To-Do List poject in which you can create, update and track your To-Do List.'''


listt=[]
listd=[]

def create():
    n=int(input("\nEnter NUMBER of Tasks you want to add: "))
    for i in range(n):
        task=input("Please Enter the Name of the Tasks: ")
        listt.append(task)
    print("\nAll the tasks are Added Succesfully!!!")

def display():
    print("\nDisplaying your To-Do list...\n")
    for i in listt:
        print(i)
    print("\n")

def add():
    add=input("Enter the name of the task:-  ")
    listt.append(add)
    print("The Task has been Added and List Updated Successfully!!!\n")

def delete():
    try:
        rem=input("\nEnter the task you want to remove: ")
        listt.remove(rem)
        print("The Task has been Deleted and List Updated Successfully!!!\n")
    except:
        print("you have a mistake in your spelling pls enter the same as in list.\n")

def done():
    x=int(input("\nEnter the NUMBER of task you have completed: "))
    for i in range(x):
        done=input("Okay...Pls Enter those tasks one by one --  ")
        listd.append(done)
        
    print("That's Great of you to have come closer...Keep it up!!!\n")

def track():
    print('\nShowing the Tasks you have completed:--')
    for i in listd:
        print(i)
    print('\nShowing the Tasks you have not completed:--')
    sub = list(set(listt) - set(listd))
    for itm in sub:
        print(itm)

while True:
    print("\n\nMENU:-\n1. Create your own To-Do list.")
    print("2. Display your To-Do list.")
    print("  Updating the List:-")
    print("3. To add more tasks in the list.")
    print("4. To delete any task from the list.")
    print("5. To mark the tasks that you have competed.")
    print("6. To track your tasks from list.")
    print("7. Exit\n")
    
    choice=int(input("Enter your choice from the above Menu:-  "))
    if choice==1:
        create()
    if choice==2:
        display()
    if choice==3:
        add()
    if choice==4:
        delete()
    if choice==5:
        done()
    if choice==6:
        track()
    if choice==7:
        break
        

        
    
    
                  


    

