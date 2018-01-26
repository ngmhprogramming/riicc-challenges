from random import randint

def encrypt(text, key):
    if key == "":
        for char in range(16):
            key += chr(randint(0, 127))
        print("Your key is " + key)
    if len(text) != len(key):
        oldKey = key
        key = ""
        for char in range(len(text)):
            key += oldKey[char % len(oldKey)]
    encrypted = ""
    for char in range(len(text)):
        newASCII = ord(text[char]) + ord(key[char])
        multiple = newASCII // 127
        newASCII -= multiple * 127
        encrypted += chr(newASCII)
    print("The encrypted text is:\n" + encrypted)

def decrypt(text, key):
    if key == "":
        for char in range(16):
            key += chr(randint(0, 127))
        print("Your key is " + key)
    if len(text) != len(key):
        oldKey = key
        key = ""
        for char in range(len(text)):
            key += oldKey[char % len(oldKey)]
    decrypted = ""
    for char in range(len(text)):
        newASCII = ord(text[char]) - ord(key[char])
        if newASCII < 0:
            newASCII = 127 + newASCII
        decrypted += chr(newASCII)
    print("The decrypted text is:\n" + decrypted)

while(True):
    action = input("What do you want to do? (E)ncrypt or (D)ecrypt ").upper()
    text = input("Enter your text. ")
    key = input("Enter your key. Leave blank for a random key. ")
    if action == "E":
        encrypt(text, key)
    elif action == "D":
        decrypt(text, key)
