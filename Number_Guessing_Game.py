import random

print("Choose difficulty:")
print("1. Easy")
print("2. Medium")
print("3. Hard")

difficulty = input("Enter your choice (1-3): ")

if difficulty == "1":
    minimum = 1
    maximum = 50

elif difficulty == "2":
    minimum = 1
    maximum = 100

elif difficulty == "3":
    minimum = 1
    maximum = 500

else:
    print("Invalid choice!")
    exit()

secret_number = random.randint(minimum, maximum)

attempts = 0

print(f"Guess a number between {minimum} and {maximum}.")

guess = int(input("Your guess: "))
attempts += 1

while guess != secret_number:

    if guess > secret_number:
        print("Too high!")

    else:
        print("Too low!")

    guess = int(input("Guess again: "))
    attempts += 1

print("Correct! You guessed the number!")
print(f"Attempts: {attempts}")