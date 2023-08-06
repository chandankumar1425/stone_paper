import random

def get_user_choice():
    choice = input("Enter your choice (stone, paper, scissors): ").lower()
    while choice not in ["stone", "paper", "scissors"]:
        print("Invalid choice. Please choose from stone, paper, or scissors.")
        choice = input("Enter your choice (stone, paper, scissors): ").lower()
    return choice

def get_computer_choice():
    return random.choice(["stone", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    if (user_choice == "stone" and computer_choice == "scissors") or \
       (user_choice == "scissors" and computer_choice == "paper") or \
       (user_choice == "paper" and computer_choice == "stone"):
        return "You win!"
    return "Computer wins!"

def main():
    print("Welcome to the Stone-Paper-Scissors game!")
    
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        
        result = determine_winner(user_choice, computer_choice)
        print(result)
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break
    
    print("Thanks for playing!")

if __name__ == "__main__":
    main()