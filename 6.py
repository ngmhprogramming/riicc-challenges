from random import randint
while(True):
    moves = ["R", "P", "SC", "L", "SP"]
    beats = [["SC", "L"], ["R", "SP"], ["P", "L"], ["SP", "P"], ["SC", "R"]]
    move = input("What's your move? (R)ock, (P)aper, (Sc)issors, (L)izard, (Sp)ock: ").upper()
    com = moves[randint(0,4)]
    state = "N"
    for i in beats[moves.index(move)]:
        if(i == com):
            state = "W"
    for i in beats[moves.index(com)]:
        if(i == move):
            state = "L"
    if(state == "W"):
        print("You win!")
    elif(state == "L"):
        print("You lose!")
    else:
        print("You tied!")
