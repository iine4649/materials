import random

class Random_Number_Guesser():
    def __init__(self, start_num, end_num):
        self.start_num = start_num
        self.end_num = end_num
        self.random_number = random.randint(self.start_num, self.end_num)
        self.turn_count = 0
        self.guess_status = False

    def run(self, game_user):
        while not self.guess_status:
            self.turn_count += 1
            print(f"Current Turn: {self.turn_count}")
            user_guess = int(input(f"Enter a number between {self.start_num} and {self.end_num}: "))
            if user_guess > self.random_number:
                print("Guess is too high...")
            elif user_guess < self.random_number:
                print("Guess is too low")
            else:
                print("Congrats! You got it!")
                if game_user.best_score == 0 or game_user.best_score > self.turn_count:
                    game_user.best_score = self.turn_count
                self.guess_status = True

            print("\n")
        print("Thank you for playing, you did a great job")

