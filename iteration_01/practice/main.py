from random_number_guesser import Random_Number_Guesser
from game_user import Game_User

first_name1 = input("Enter your first name: ")
last_name1 = input("Enter your last name: ")

# first_name2 = input("Enter your first name: ")
# last_name2 = input("Enter your last name: ")

user1 = Game_User(first_name1, last_name1)
# user2 = Game_User(first_name2, last_name2)
rand_guess_game1 = Random_Number_Guesser(0,20)

# Run game
rand_guess_game1.run(user1)
