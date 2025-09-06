import random

# Word lists for each difficulty
easy_words=["apple","train","tiger","money","india"]
medium_words=["python","bottle","monkey","planet","laptop"]
hard_words=["elephant",'diamond',"umbrella","computer","mountain"]

# Game intro
print("welcome to the password guessing game")
print("choose difficulty level: easy, medium, hard")

# Take difficulty input and choose a secret word
level=input("Enter difficulty:").lower()
if level=="easy":
    secret=random.choice(easy_words)
elif level=="medium":
    secret=random.choice(medium_words)
elif level=="hard":
    secret=random.choice(hard_words)
else:
    print("Invalid choice. Default easy level")               # Default to easy if user input is invalid
    secret=random.choice(easy_words)

# Track the number of guesses
attempts=0
print("\nGuess the secret password")

# Main guessing loop
while True:
    guess=input("Enter your guess: ").lower()
    attempts +=1                                      # Count every guess attempt

    if guess == secret:                                # Correct guess — exit loop
        print(f"Congratulations! you guessed it in {attempts} attempts")
        break

# Create a hint showing correct letters in the correct position
    hint=""

    for i in range(len(secret)):
        if i < len(guess) and guess[i]==secret[i]:
            hint += guess[i]                              # Correct letter and position
        else:
            hint += "_"                                  # Wrong or missing letter

    print("Hint :", hint)

print("Game over")                         # End of game