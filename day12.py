import random
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
level = input("Choose a difficulty. Type 'easy' or 'hard': ")
#deciding level
if level == 'easy':
    attempt = 10
elif level == 'hard':
    attempt = 5
else:
    attempt = 0
#generating a random number
num = random.randint(1,100)
print(f"{num}")
while attempt >0:
    print(f"You have {attempt} attempts remaining to guess the number.")
    ch = int(input("Make a guess: "))
    if ch > num:
        print("Too high.")
    elif ch < num:
        print("Too low.")
    elif ch == num:
        print("You got it! The answer was 14.")
        break
    attempt -=1
    print("Guess again")
