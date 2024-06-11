import random

attempts_list = []

def show_score():
    if not attempts_list:
        print("there is no high score , please play so you can get a score")
    else:
        print("the current high score is " + min(attempts_list) + "attempts")

attempts = 0

rand_number = random.randint(1 , 10)

print ("hello player ! welcome tho the guessing game")

player_name = input("what is your name ?")
want_to_play = input (f"Hi {player_name} whould you like to play guessing game ?"
                        "(Enter Yes/ NO)"
).lower

if want_to_play == "yes":
    print("that's cooooool! let gooooo")
    exit()
else:
    show_score()

while want_to_play == "yes":
    guess = int(input("please insert a number between 1 - 10"))
    if guess < 1 or guess > 10:
        raise ValueError ("please insert a number within between 1 and 10")