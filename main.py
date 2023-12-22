import random 

def guess(x):
    number = random.randint(1, x)
    guess = 0
    while guess != number:
        guess = int(input("Type a number: "))
        if guess < number:
            print("too bad, the number is HIGHER, guess again ")
        elif guess >number:
            print("too bad, the number is LOWER, guess again ")
        
guess(19)
print("Congrats, you guessed it right!")