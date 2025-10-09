import random
print("Welcome to the number Gussing Game!")
print("I'am thinking of a number between 1 and 100")

secret_number=random.randint(1,100)
attempts=0
while True:
    guess=int(input("Enter your guess:"))
    attempts+=1
    if guess<secret_number:
        print("Too Low!")
    elif guess>secret_number:
        print("Too High!")
    else:
        print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts.")