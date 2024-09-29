import random

def computer():
    return random.choice(['paper', 'rock', 'scissors'])

def winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or (user_choice == 'scissors' and computer_choice == 'paper') or (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win"
    else:
        return "You lose"
    
def show(user_choice, computer_choice, result):
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    print(f"Result: {result}\n")

def main():
    user_score = 0
    computer_score = 0

    while True:
        user_choice = input("Choose rock, paper, or scissors: ").lower()

        if user_choice not in ['paper', 'rock', 'scissors']:
            print("Invalid choice.")
            continue
        computer_choice = computer()
        res = winner(user_choice, computer_choice)
        show(user_choice, computer_choice, res)
        if res == "You win":
            user_score += 1
        elif res == "You lose":
            computer_score += 1
        print(f"Scores - You: {user_score}, Computer: {computer_score}")
        play_again = input("Do you want to play again? (Y/N): ").lower()
        if play_again != 'y':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()

