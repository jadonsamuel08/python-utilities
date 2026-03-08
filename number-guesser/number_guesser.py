import random

def main():
    print("="*56 + "\n\tWELCOME TO NUMBER GUESSER BY JADON SAMUEL\n" + "="*56 , end="\n\n")
    print("RULES: A random number between 1 and 100 will be generated. You're goal is to guess that number. You have infinite tries.")
    
    num_guesses = 1
    rand_num = random.randint(1,100)
    
    while True:
        try:
            guess = int(input(f"Guess #{num_guesses}: "))
            if guess == rand_num:
                print("Congradulations You Won!!!")
                break
            else:
                print("Incorrect. Try again.")
                num_guesses += 1
        except Exception as e:
            print("Please enter a number between 1 and 100")
        
main()