# Make a two-player Rock-Paper-Scissors game.
# Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game.

print("This is a Rock-Paper-Scissors game. Please choose one of the options: 'rock', 'paper' or 'scissors'.")

play_again = 'y'
while True:
    player1 = input("Player 1, enter your choice: ")
    player2 = input("Player 2, enter your choice: ")
    if player1 == player2:
        print("No one won!")

    elif player1 == 'rock':
        if player2 == 'scissors':
            print("Player 1, congratulations, you won!")
        elif player2 == 'paper':
            print("Player 2, congratulations, you won!")

    elif player1 == 'scissors':
        if player2 == 'rock':
            print("Player 2, congratulations, you won!")
        elif player2 == 'paper':
            print("Player 1, congratulations, you won!")

    elif player1 == 'paper':
        if player2 == 'rock':
            print("Player 1, congratulations, you won!")
        elif player2 == 'scissors':
            print("Player 2, congratulations, you won!")

    play_again = input("Do you want to play again? Type: 'y' or 'n': ")
    if play_again == 'n':
        break
