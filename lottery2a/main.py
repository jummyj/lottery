import random


def play_lottery():
   lucky_numbers = random.sample(range(1, 50), 6)
   user_numbers = []
   while len(user_numbers) < 6:
       guess = input("Guess a number between 1 and 49: ")
       if guess.lower() == "q":
           return "Quitting game..."
       try:
           guess = int(guess)
       except ValueError:
           print("Invalid input. Please enter a number.")
           continue
       if guess < 1 or guess > 49:
           print("Invalid input. Please enter a number between 1 and 49.")
           continue
       if guess in user_numbers:
           print("You've already guessed that number. Please try again.")
           continue
       user_numbers.append(guess)
   num_correct = len(set(user_numbers).intersection(set(lucky_numbers)))
   if num_correct == 1:
       print(f"Sorry you have one leg. Lucky numbers: {lucky_numbers}. Your guesses: {user_numbers}.")
   elif num_correct == 2:
       print("Congratulations!!! You got two correctly.")
   elif num_correct == 3:
       print("Congratulations!!! You won 3 three strikes.")
   elif num_correct == 4:
       print("Congratulations!!! You won 4 strikes.")
   elif num_correct == 5:
       print("Congratulations!!! You won 5 strikes.")
   elif num_correct == 6:
       print("Congratulations!!! You have won a JackPot!!!")
   else:
       print(f"Sorry, you didn't win. Lucky numbers: {lucky_numbers}. Your guesses: {user_numbers}.")


play_lottery()

