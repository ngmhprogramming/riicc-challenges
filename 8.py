from random import randint
letters = "abcdefghijklmnopqrstuvwxyz"
while(True):
    a = input("First Person's Name: ").lower()
    b = input("Second Person's Name: ").lower()
    score = 0
    for i in range(len(a)):
        score += letters.index(a[i])*(i+1)
    for i in range(len(b)):
        score -= letters.index(b[i])*(i+1)
    print("Love Level: " + str(score % 100))
