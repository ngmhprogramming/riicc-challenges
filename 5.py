while(True):
    print("Fizz Buzz for numbers in the range s to e inclusive, and numbers to divide by are a and b. ")
    s = int(input("s: "))
    e = int(input("e: "))
    a = int(input("a: "))
    b = int(input("b: "))
    for i in range(s, e+1):
        print(i)
        if(i % a == 0):
            print("Fizz")
        if(i % b == 0):
            print("Buzz")
        if(i % a == 0 and i % b == 0):
            print(i)
