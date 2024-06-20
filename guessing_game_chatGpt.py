import random

def guessing_game():
    # Dictionary to store best scores associated with player names
    best_scores = {}
    play_again = 'y'
    
    # Ask for player's name
    player_name = input("Please enter your name: ")
    
    # Greet the player
    print(f"\nWelcome, {player_name}! Let's play the Guessing Game.")
    
    while play_again.lower() == 'y':
        # Computer randomly selects a number between 1 and 10
        computer_choice = random.randint(1, 10)
        # Initialize the number of attempts for this round
        attempts = 0
        # Flag to check if the player has guessed correctly
        correct_guess = False
        
        print("\nI have chosen a number between 1 and 10. Try to guess it.")
        
        # Loop until the player guesses the correct number
        while not correct_guess:
            try:
                # Ask the player for their guess
                player_guess = int(input("Enter your guess: "))
                # Check if the guess is within the valid range
                if player_guess < 1 or player_guess > 10:
                    print("Please choose a number between 1 and 10.")
                    continue
                # Increment the number of attempts
                attempts += 1
                
                # Check if the player's guess is correct
                if player_guess == computer_choice:
                    correct_guess = True
                    print(f"Congratulations, {player_name}! You guessed the number in {attempts} attempts.")
                    # Update the best score for the player if this is the lowest number of attempts
                    if player_name not in best_scores or attempts < best_scores[player_name]:
                        best_scores[player_name] = attempts
                        print(f"New best score for {player_name}: {best_scores[player_name]} attempts!")
                elif player_guess < computer_choice:
                    print("Higher! Try again.")
                else:
                    print("Lower! Try again.")
            except ValueError:
                # Handle non-integer inputs
                print("Invalid input. Please enter a number between 1 and 10.")
        
        # Ask the player if they want to play again
        play_again = input("Do you want to play again? (y/n): ")
    
    # Game over, display the best score for the player
    print(f"\nThanks for playing, {player_name}! Your best score was {best_scores[player_name]} attempts.")

# Run the game
guessing_game()
