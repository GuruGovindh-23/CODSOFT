import random

def get_computer_choice():
    """Randomly selects between 'rock', 'paper', or 'scissors' for the computer."""
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    """Determines the winner based on user and computer choices."""
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

def display_score(user_score, computer_score):
    """Displays the current score of the user and the computer."""
    print(f"\nCurrent Score -> You: {user_score}, Computer: {computer_score}")

def play_game():
    """Main game function that handles user input, computer choice, and displays results."""
    user_score = 0
    computer_score = 0
    print("Welcome to Rock, Paper, Scissors!")
    print("Instructions: Choose 'rock', 'paper', or 'scissors'.")
    while True:
        
        user_choice = input("\nEnter your choice (rock, paper, or scissors): ").lower()

        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please select 'rock', 'paper', or 'scissors'.")
            continue
        computer_choice = get_computer_choice()
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        result = determine_winner(user_choice, computer_choice)
        print(f"Result: {result}")
        if result == "You win!":
            user_score += 1
        elif result == "Computer wins!":
            computer_score += 1
        display_score(user_score, computer_score)
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! See you again!!")
            break

if __name__ == "__main__":
    play_game()
