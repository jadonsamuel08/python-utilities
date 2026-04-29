import random

def main():
    print("=" * 45 + "\n\tNUMBER GUESSER BY JADON SAMUEL\n" + "=" * 45, end="\n\n")
    print("RULES: A random number between 1 and 100 will be generated. Your goal is to guess that number. You have infinite tries.\n")

    while True:
        num_guesses = 1
        rand_num = random.randint(1, 100)

        while True:
            try:
                guess = int(input(f"Guess #{num_guesses}: "))
                if guess < 1 or guess > 100:
                    print("Please enter a number between 1 and 100.")
                elif guess == rand_num:
                    print(f"Congratulations! You guessed it in {num_guesses} guess{'es' if num_guesses > 1 else ''}!")
                    break
                elif guess < rand_num:
                    print("Too low! Try again.")
                    num_guesses += 1
                else:
                    print("Too high! Try again.")
                    num_guesses += 1
            except ValueError:
                print("Invalid input. Please enter a integer.")

        play_again = input("\nPlay again? (y/n): ").strip().lower()
        if play_again != "y":
            print("Thanks for playing!")
            break

main()