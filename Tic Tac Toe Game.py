# for display the tic tac toe board
def print_board(a):
    print("",a[1],"|",a[2],"|",a[3]," ")
    print("---|---|---")
    print("",a[4],"|",a[5],"|",a[6]," ")
    print("---|---|---")
    print("",a[7],"|",a[8],"|",a[9]," ")

#for display the instruction of game
def print_instructions():
    print("\n~~~~~~~~Welcome To Tic Tac Toe~~~~~~~~")
    print_board(pos)
    print()

    players[0] =input("1st Player Name : ")
    players[1] =input("2nd Player Name : ")

    print("\n-----Instructions-----")
    print("->",players[0],"you will using X")
    print("->",players[1],"you will using 0")
    print("-> Turn starts from ",players[0])
    print("-> Positions are like :")
    print(" 1 | 2 | 3 ")
    print("---|---|---")
    print(" 4 | 5 | 6 ")
    print("---|---|---")
    print(" 7 | 8 | 9 ")
    print("-> Press S to start the game : ")
    flag = input()
    return flag

#for start the game
def startgame():
    turn = 0
    for i in range(9):
        if turn % 2==0:
            print("\n This is your turn",players[0])
            p=int(input("Please Enter Position : "))
            v='x'
            pos[p] =v
            print_board(pos)
            winner =checkwin(v)
            if winner == "nobody" :
                turn = 1
                continue
            else:
                print("\n\n Hurray !!!,",players[0],"you win ...!!")
                break
        else:
            print("\n This is your turn",players[1])
            p=int(input("Please Enter Position : "))
            v='0'
            pos[p] =v
            print_board(pos)
            winner =checkwin(v)
            if winner =="nobody" :
                turn = 0
                continue
            else:
                print("\n\n Hurray !!!,",players[1],"you win ...!!")
    else:
        print("\n Game is Tie ...")

#check for winner
def checkwin(v):
    for i in winning_conditions:
        if(pos[i[0]], pos[i[1]],pos[i[2]]) ==(v,v,v):
            winner = players[0]
            break
        elif(pos[i[0]], pos[i[1]],pos[i[2]]) ==(v,v,v):
            winner = players[1]
            break
    else:
        winner ="nobody"
    return winner

#main code
pos=['',' ',' ',' ',' ',' ',' ',' ',' ',' ']
players =['','']
winning_conditions =[(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7)]
flag = print_instructions()
if flag =='s' or flag =='S':
    startgame()
else:
    print("Invalid Entry")














