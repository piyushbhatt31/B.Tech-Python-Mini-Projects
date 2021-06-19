import random
while(1):
    number = random.randint(1,100)
    user = int(input("Guess a number from 1 to 100:"))
    if user == number:
        print("Hurray!!")
        print(f"you guessed the number right it's {number}")
    if user != number:
        print(f"Your guess is incorrect the number is {number}")
    ch = input("press 1 to exit or any key to continue : ")
    if ch == "1":
        break
        
