import random
sysScore = 0
userScore = 0
line="-"*10


def sysPlayer():
    id = random.randint(1, 3)
    # if id --> 1 system plays stone as <str>:"stone"
    if id == 1:
        return "stone"
    # if id --> 2 system plays paper as <str>:"paper"
    elif id == 2:
        return "paper"
    # if id --> 3 system plays scissor as <str>:"scissor"
    elif id == 3:
        return "scissor"
print(" "*30)
print("ssssssss tttttttttt ooooooooooo  nn        n  eeeeeee           ")
print("s             t     o         o  n n       n  e                 ")
print("s             t     o         o  n  n      n  e                 ")
print("s             t     o         o  n   n     n  e                 ")
print("ssssssss      t     o         o  n    n    n  eeeeeee          ")
print("       s      t     o         o  n     n   n  e                ")
print("       s      t     o         o  n      n  n  e                ")
print("       s      t     o         o  n       n n  e                 ")
print("ssssssss      t     ooooooooooo  n        nn  eeeeeee           ")
print(" "*30)
maxScore=int(input("Enter the max score u want to stop the game : >> "))

while (sysScore<maxScore and userScore<maxScore):
    userInput = input("Enter Your play : ")
    sysMove = sysPlayer()
    print("*"*10)
    print("Ur move is  : ",userInput)
    print("System Move is : ",sysMove)
    if userInput=="stone" and sysMove=="stone":
        print(line)
        print("Its a tie")
        print("Your score: ",userScore,"System score:",sysScore)
        print(line)
    elif userInput=="stone" and sysMove=="paper":
        print(line)
        sysScore +=1
        print("System won the move")
        print("Your score: ",userScore,"System score:",sysScore)
        print(line)
    elif userInput=="paper" and sysMove=="stone":
        print(line)
        userScore +=1
        print("User won the move")
        print("Your score: ",userScore,"System score:",sysScore)
        print(line)
    elif userInput=="paper" and sysMove=="paper":
        print(line)
        print("Its a tie")
        print("Your score: ",userScore,"System score:",sysScore)
        print(line)
    elif userInput=="paper" and sysMove=="scissor":
        print(line)
        sysScore +=1
        print("System won the move")
        print("Your score: ",userScore,"System score:",sysScore)
        print(line)
    elif userInput=="scissor" and sysMove=="paper":
        print(line)
        userScore +=1
        print("User won the move")
        print("Your score: ",userScore,"System score:",sysScore)
        print(line)
    elif userInput=="scissor" and sysMove=="scissor":
        print(line)
        print("Your score: ",userScore,"System score:",sysScore)
        print(line)
    elif userInput=="stone" and sysMove=="scissor":
        print(line)
        userScore +=1
        print("Your score: ",userScore,"System score:",sysScore)
        print(line)
    elif userInput=="scissor" and sysMove=="stone":
        print(line)
        sysScore +=1
        print("Your score: ",userScore,"System score:",sysScore)
        print(line)


    
        
    

