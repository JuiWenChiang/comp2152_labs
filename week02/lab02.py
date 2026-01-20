import random

# Optional Enhancements
# Optional: Add a scoring system to track wins and losses.
# Optional: Use a loop to play multiple rounds.
# Optional: Generate a random computer choice using the random module.
choices = ["Rock", "Paper", "SciScissors"]
score = 0
playGame = True

while playGame:
    playerChoice = int(input("\nPleace enter your choice(1=Rock, 2=Paper, 3=Scissors)."))

    if playerChoice < 1 or playerChoice > 3:
        print("Error: Choice must be between 1 and 3.")
    else:
        computerChoice = random.randint(1, 3)
        playerChoiceIndex = choices[playerChoice - 1]
        computerChoiceIndex = choices[computerChoice - 1]

        print(f"Computer's choice (1-3):{computerChoice}")
        print(f"You chose: {playerChoiceIndex}")
        print(f"Computer chose: {computerChoiceIndex}")

        # Determine the winner logic using if/elif/else
        # Python emphasizes readability, so it uses English words rather than symbols for operators:
        # - logical operators: and, or, not 
        # - comparison Operators: ==, !=, >=, <=, >, <
        # - identity Operators: is, is not
        if playerChoice == computerChoice:
            score+=1
            print("\nIt's a tie!")
        elif playerChoice == 1 and computerChoice == 3:
            score+=2
            print("\nRock beats Scissors - You win!")
        elif playerChoice == 2 and computerChoice == 1:
            score+=2
            print("\nPaper beats Rock - You win!")
        elif playerChoice == 3 and computerChoice == 2:
            score+=2
            print("\nScissors beats Paper - You win!")
        else:
            print("\nYou lose!")

        if playGame:
            print(f"You're total score is {score}")
            playerChoice = int(input("\nAre you going to continue (0=No, 1=Yes)?"))
            if playerChoice == 0:
                playGame = False
            elif playerChoice != 1:
                playGame = False
                print("Error: Wrong choice. End up the game")

if playGame is False:
    print("\nGoodBye. See you next time! :) \n")