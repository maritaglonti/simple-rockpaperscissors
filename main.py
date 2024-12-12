import random

choices = ('Rock', 'Paper', 'Scissors')
computer_choice = random.choice(choices)

while True:
      player_choice: str = input().capitalize()
      print(f"{computer_choice}")

      if player_choice == computer_choice:
        print("It's a draw!")
      if (player_choice == "Rock" and computer_choice == "Paper") or (player_choice == "Paper" and computer_choice == "Scissors") or (player_choice == "Scissors" and computer_choice == "Rock"):
        print("Computer wins!")
      if (player_choice == "Paper" and computer_choice == "Rock") or (player_choice == "Scissors" and computer_choice == "Paper") or (player_choice == "Rock" and computer_choice == "Scissors"):
        print("Player 1 wins!")

      replay = input("Do you want to play again? yes/no: ").lower()
      if replay != "yes":
            print("Thanks for playing!")
            break