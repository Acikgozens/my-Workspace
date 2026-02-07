import random

print("Hi welcome to the number guessing game. You have 7 chances to guess the number lets start")

low = int(input("Enter a lower bound: "))
high = int(input("Enter a upper bound: "))

print(f"You have seven chances to guess the number between {low} and {high}")

num = random.randint(low, high)
ch = 7 #chances
gc = 0 #guess counter

while gc < ch:
    guess = int(input("Enter your guess: "))
    gc += 1
    
    if guess == num:
        print(f"Correct. The number is {num}. You guessed it in {gc} guesses")
        break

    elif gc >= ch and guess != num:
        print(f"Sorry the number is {num}. Try again next time")

    elif guess > num:
        print("Too high. Try again")

    elif guess < num:
        print("Too low. Try again")
   