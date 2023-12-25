import random 

def choice():
    
    usr_choice = input("If you want the computer to discover you number type 'pc' (number needs to be in a range between 1 and 10 000). If you want to discover the computer number, type 'me' (the number is between 1 and 500)")
    if usr_choice == 'pc':
        pcGuess(10000) 
    elif usr_choice == 'me':
        userGuess(500)
    else:
        choice()


def userGuess(x):
    number = random.randint(1, x)
    guess = 0
    while guess != number:
        try:
            guess = int(input("Type a number: "))
            if guess < number:
                print("too bad, the number is HIGHER, guess again ")
            elif guess > number:
                print("too bad, the number is LOWER, guess again ")
        except ValueError:
            print("That's not a valid number, it can't be a decimal or contain letters, guess again ")
    print(f"Congrats, you guessed it right!, the number was {guess}")
            
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

choice()