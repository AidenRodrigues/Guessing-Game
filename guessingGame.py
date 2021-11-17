import random
number=random.randint(1, 9)

print("Guess a Number between 1 and 9: ")
guess=int(input("Enter Your Guess: "))
if guess==number:
    print("Congradulations YOU WON!!!")
else:
    print("YOU LOSE")