from random import randint
with open("7.txt") as file:
    words = file.read().splitlines()
while(True):
    guessed = False
    word = words[randint(0,len(words))-1]
    hidden = "_"*len(word)
    solved = 0
    counter = 0
    while(not guessed):
        guess = input("Your Guess: ").lower()
        counter += 1
        for i in range(len(word)):
            if(word[i] == guess):
                hidden = hidden[:i] + word[i] + hidden[i+1:]
                solved += 1
        print(hidden)
        if(solved == len(word)):
            guessed = True
    print("Yay! You guessed the word in " + str(counter) + " tries!")
        
