import random

def rock_paper_scissors():
    print("\nROCK, PAPER, SCISSORS!")

    winning_combo = {
        'rock': 'scissors',
        'scissors': 'paper',
        'paper': 'rock'
    }

    while True:
        player_move = input("\nSelect (rock, paper, or scissors): ").lower()
        if player_move not in winning_combo:
            print("Invalid move. Please try again")
            continue
    
        computer_move = random.choice(list(winning_combo.keys()))
        print(f"Computer chose: {computer_move}")

        if player_move == computer_move:
            print("It's a tie")
        elif winning_combo[player_move] == computer_move:
            print("You win!")
        else:
            print("Computer wins!")

        play_again = input("\nPlay again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing")
            break


def main():
    pass