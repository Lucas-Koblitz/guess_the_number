import random 

def userGuess(x):
    number = random.randint(1, x)
    guess = 0
    while guess != number:
        guess = int(input("Type a number: "))
        if guess < number:
            print("too bad, the number is HIGHER, guess again ")
        elif guess > number:
            print("too bad, the number is LOWER, guess again ")
            
def pcGuess(x):
    low = 1
    high = x
    response = ''
    while response != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        response = input(f"if your number is higher than  {guess}  press (h), if it's lower, press (l), if it's correct, press (c) ")
        if response == 'l':
            high = guess-1
        elif response == 'h':
            low = guess+1 
        
            
    print(f"the number you imagined is {guess}")

print("Congrats, you guessed it right!")
userGuess(123)