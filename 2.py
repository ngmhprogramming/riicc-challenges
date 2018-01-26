while(True):
    convert = input("Convert to C or F: ").upper()
    measurement = int(input("Value: "))
    if convert == "C":
        print((measurement-32)/1.8)
    elif convert == "F":
        print(measurement*1.8+32)
    else:
        print("Invalid Unit")
