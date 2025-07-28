import random

class Game:
    """
    A class to represent a game of Rock, Paper, Scissors.
    """
    def __init__(self):
        """
        Initializes the game with scores for the user and PC set to 0.
        """
        self.user_score = 0
        self.pc_score = 0

    def play(self):
        """
        Starts and manages the main game loop.
        The loop continues until the user decides to quit.
        """
        print("Game started!")
        self.show_rules()

        while True:
            # Get input from the user
            user_choice = self.get_user_input()

            # Check if the user wants to quit
            if user_choice == 'q':
                print("Thanks for playing!")
                print(f"Final Score -> You: {self.user_score} | PC: {self.pc_score}")
                break

            # Get a random choice from the computer
            pc_choice = self.get_pc_opponent()

            # Display the choices
            print(f"\nYou chose: {self.get_choice_name(user_choice)}")
            print(f"PC chose: {self.get_choice_name(pc_choice)}")

            # Determine the winner of the round
            result = self.get_winner(user_choice, pc_choice)
            print(f"\n{result}")

            # Update the score based on the result
            if "You win" in result:
                self.user_score += 1
            elif "PC wins" in result:
                self.pc_score += 1

            # Display the current score
            print(f"Score -> You: {self.user_score} | PC: {self.pc_score}\n")
            print("-" * 30)


    def show_rules(self):
        """
        Prints the rules of the game to the console.
        """
        print("\n--- Rules ---")
        print("Rock beats Scissors, Scissors beats Paper, and Paper beats Rock.")
        print("Enter 'r' for Rock.")
        print("Enter 's' for Scissors.")
        print("Enter 'p' for Paper.")
        print("Enter 'q' to quit the game.")
        print("-------------\n")

    def get_user_input(self):
        """
        Prompts the user for their choice and validates the input.
        It will keep asking until a valid input is entered.
        """
        while True:
            user_choice = input("Enter your choice (r, s, p) or q to quit: ").lower()
            if user_choice in ["r", "s", "p", "q"]:
                return user_choice
            else:
                print("Invalid entry. Please try again.")

    def get_pc_opponent(self):
        """
        Generates a random choice (Rock, Paper, or Scissors) for the computer.
        """
        weapon_list = ["r", "s", "p"]
        return random.choice(weapon_list)

    def get_winner(self, user_choice, pc_choice):
        """
        Determines the winner based on the user's and computer's choices.
        
        Args:
            user_choice (str): The user's choice ('r', 's', or 'p').
            pc_choice (str): The computer's choice ('r', 's', or 'p').
            
        Returns:
            str: A string declaring the winner or if it's a tie.
        """
        if user_choice == pc_choice:
            return "It's a Tie!"
        elif (user_choice == "r" and pc_choice == "s") or \
             (user_choice == "s" and pc_choice == "p") or \
             (user_choice == "p" and pc_choice == "r"):
            return f"You win! {self.get_choice_name(user_choice)} beats {self.get_choice_name(pc_choice)}."
        else:
            return f"PC wins! {self.get_choice_name(pc_choice)} beats {self.get_choice_name(user_choice)}."

    def get_choice_name(self, choice):
        """
        Converts the single-letter choice to its full name.
        
        Args:
            choice (str): The choice to convert ('r', 's', or 'p').
            
        Returns:
            str: The full name of the choice (e.g., "Rock").
        """
        if choice == 'r':
            return "Rock"
        if choice == 's':
            return "Scissors"
        if choice == 'p':
            return "Paper"
        return "Unknown"

def main():
    """
    The main function to run the game.
    """
    game = Game()
    game.play()

# This ensures the main() function is called only when the script is executed directly
if __name__ == "__main__":
    main()
