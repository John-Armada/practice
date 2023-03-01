# Christ John Armada - BSCS - 1


def prelim_lab():
    import random

    # Ask players for their names
    while True:  # It will ask a user to input a proper name and avoid numeric values
        player_1 = input("Player 1: ")
        player_2 = input("Player 2: ")
        if player_1.isalpha() and player_2.isalpha():
            break
        print("Please enter characters only for your name")

    while True:
        # Generate a random number between 1 and 10
        x = random.randint(1, 10)
        # Start the guessing game
        while True:
            # Ask each player for their guess
            try:
                player_1_guess = int(
                    input(f"\n{player_1}, please enter a number from 1 to 10: ")
                )
                player_2_guess = int(
                    input(f"{player_2}, please enter a number from 1 to 10: ")
                )
            except ValueError:
                print("Please enter numbers only")
            else:
                break

        # Check if both players guessed the same number
        if player_1_guess == player_2_guess:
            while True:
                player_2_guess = int(
                    input(f"No cheating, {player_2}! Please enter a different number: ")
                )
                if player_1_guess != player_2_guess:
                    if player_1_guess and player_2_guess != x:
                        print(f"Sorry, the random number is {x}. Try again.")
                        break  # exit the while loop
                else:
                    continue  # skip the current iteration and continue with the next iteration of the while loop

        # Check if one of the players guessed the correct number
        elif player_1_guess == x:
            print(f"\nCongrats, {player_1}! The random number is {x}!")
            break

        elif player_2_guess == x:
            print(f"\nCongrats, {player_2}! The random number is {x}!")
            break

        # Neither player guessed the correct number
        else:
            print(f"Sorry, the random number is {x}. Try again.")

    # Finish!


prelim_lab()
