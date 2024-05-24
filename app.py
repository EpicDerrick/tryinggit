#this is a test app to help try git for the first time
import random

def guess_the_number():
    number_to_guess = random.randint(1, 100)
    user_guess = int(input("Guess a number between 1 and 100: "))
    score = 100 - abs(number_to_guess - user_guess)
    
    print(f"The number was: {number_to_guess}")
    print(f"Your guess was: {user_guess}")
    print(f"Your score is: {score}")

if __name__ == "__main__":
    guess_the_number()
