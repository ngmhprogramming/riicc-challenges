from random import randint
with open("0_1.txt") as file:
    first = file.read().splitlines()
with open("0_2.txt") as file:
    last = file.read().splitlines()
while(True):
    num = int(input("How many names? "))
    for i in range(num):
        print("Hi, " + first[randint(0,len(first)-1)] + " " + last[randint(0,len(last)-1)] + "!")
