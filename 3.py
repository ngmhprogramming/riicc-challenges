from datetime import date
while(True):
    birthday = [int(i) for i in input("Birthday(DD/MM/YY): ").split("/")]
    birthday.reverse()
    birthday = date(birthday[0], birthday[1], birthday[2])
    age = date.today() - birthday
    age = age.days*24*60*60
    print("You are " + str(age) + " seconds old.")
