import random
while True:
    print("~~~~~~~~Welcome To Rock Paper Scissors~~~~~~~~")
    user_score=0
    comp_score=0
    ties=0

    name=input("Enter your name here : ")
    print("""Winning Rules :
    1.Paper vs Rock --> Paper
    2.Rock vs Scissors --> Rock
    3.Scissors vs Paper --> Scissors """)
    print()
    for i in range(1,6):
        print("~~~Round",i,"Start~~~")
        print("""Choices are:
        1.Rock
        2.Paper
        3.Scissors""")
        choice= int(input("Enter your choice from 1-3 : "))
        print()
        while choice>3 or choice<1:
            choice=int(input("Enter valid Input : "))
        if choice==1:
            user_choice="Rock"
        elif choice==2:
            user_choice="Paper"
        else:
            user_choice="Scissors"

        print(name,"choice is",user_choice)

        computer = random.randint(1,3)
        if computer==1:
            comp_choice="Rock"
        elif computer==2:
            comp_choice="Paper"
        else:
            comp_choice="Scissors"

        print("Computer Choice is",comp_choice)

        if user_choice==comp_choice:
            user_score +=1
            comp_score +=1
            print("This Round is Drawn ")
        elif (user_choice=="Paper" and comp_choice=="Rock")or(user_choice=="Rock" and comp_choice=="Scissors")or(user_choice=="Scissors" and comp_choice=="Paper"):
            user_score +=1
            print(name,"win this Round")
        else:
            comp_score +=1
            print("Computer win this Round")


    if user_score > comp_score:
        print(name,"win the game....!!!")
        print()
        print(name,"Score : ",user_score)
        print("Computer Score : ",comp_score)
    elif comp_score > user_score:
        print("Computer win the game....!!!")
        print()
        print(name,"Score : ",user_score)
        print("Computer Score : ",comp_score)
    else:
        print("Match Drawn ...!")
        print()
        print(name,"Score : ",user_score)
        print("Computer Score : ",comp_score)
    new_choice=input("Want to Play again ? (Yes/Exit): ")
    if new_choice=="yes" or new_choice=="Yes" or new_choice=="YES" :
        continue
    else:
        break















        
