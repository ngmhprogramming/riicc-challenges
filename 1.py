from random import randint

while(True):
    result = ["H", "T"][randint(0,1)]
    guess = input("(H)eads or (T)ails: ").upper()
    if result == guess:
        print("You win.")
    else:
        print("You lose.")
