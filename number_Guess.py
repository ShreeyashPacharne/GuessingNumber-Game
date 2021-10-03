import random

ran = random.randrange(1,10)

while ran > 0:
    user_input = int(input("Guess: "))
    if user_input == ran:
        print("Whoaa! You Guessed Right")
        break;
    elif user_input - ran > 2:
        print("Hot")
    else:
        print("Cold")