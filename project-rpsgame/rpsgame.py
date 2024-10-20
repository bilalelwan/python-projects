point1 = 0
point2 = 0
while True:
    player1 = input("select your move R, P, S: ")
    player2 = input("select your move R, P, S: ")
    if (player1 == "R" or player1 == "r") and (player2 == "P" or player2 == "p"):
        print("player2 win! one point for player2")
        point2 +=1
    elif (player1 == "R" or player1) == "r" and (player2 == "R" or player2 == "r"):
        print("draw!, try again")
    elif (player1 == "R" or player1 == "r") and (player2 == "S" or player2 == "s"):
        print("player1 win, one point for player1")
        point1+=1
    elif (player1 == "P" or player1 == "p") and (player2 == "R" or player2 == "r"):
        print("player1 win! one point for player1")
        point1 +=1
    elif (player1 == "P" or player1 == "p") and (player2 == "P" or player2 == "p"):
        print("draw!, try again")
    elif (player1 == "P" or player1 == "p") and (player2 == "S" or player2 == "s"):
        print("player2 win! one point for player2")
        point2+=1
    elif (player1 == "S" or player1 == "s") and (player2 == "S" or player2 == "s"):
        print("draw!, try again")
    elif (player1 == "S" or player1 == "s") and (player2 == "R" or player2 == "r"):
        print("player2 win! one point for player2")
        point2 +=1
    elif (player1 == "S" or player1 == "s") and (player2 == "P" or player2 == "p"):
        print("player1 win! one point for player1")
        point1 +=1
    else:
        print("Invalid input, you should select between R, P, S")
        break
    if point1 == 3:
        print("player1 win the round")
        exit()
    elif point2 == 3:
        print("player2 win the round")
        exit()
    else:
        continue