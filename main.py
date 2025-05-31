import random

def rock_paper_scissors():
    print("\nROCK, PAPER, SCISSORS!")

    while True:
        player_move = input("\nSelect (rock, paper, or scissors): ").lower()
        if player_move not in ['rock', 'paper', 'scissors']:
            print("Invalid move. Please try again")
            continue
    
        computer_move = random.choice(['rock', 'paper', 'scissors'])
        print(f"Computer chose: {computer_move}")

        if player_move == computer_move:
            print("It's a tie")
        elif (
            (player_move == 'rock' and computer_move == 'scissors') or
            (player_move == 'paper' and computer_move == 'rock') or
            (player_move == 'scissors' and computer_move == 'paper')
        ):
            print("You win!")
        else:
            print("Computer wins!")

        play_again = input("\nPlay again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing")
            break


def main():
    pass