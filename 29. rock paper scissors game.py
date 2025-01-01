import random

options = ("rock", "paper", "scissors") # Not Changing the options so a tuple will be better
running = True

while running:
    player = None  # Store the Players Choice
    computer = random.choice(options)  # Computer is picking from the options a random one 1/3 each.


# Rock Beats Scissors
    while player not in options: # While Player variable is not found it will continue forever until the player enters correctly.
        player = input("Enter a choice (rock,paper,scissors): ")

    print(f"Player: {player}")
    print(f"Computer: {computer}") # Sucessfully picking a option from the list

    if player == computer:
        print("Its a tie!")
    elif player == "rock" and computer == "scissors":
        print("You Win!")
    elif player == "paper" and computer == "rock":
        print("You Win!")
    elif player == "scissors" and computer == "paper":
        print("You Win!")
    else:
        print("You lose!")

    play_again = input("Play again (y/n)").lower()
    if not play_again == "y":
        running = False # If not playing again it will be false.

print("Thanks For Playing")

# if not input("Play again? (y/n): ").lower() == "y":
    # running = False

# You can do this also as well instead of making a variabole.
