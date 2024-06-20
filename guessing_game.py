import random

attempts_list = []

def show_score():
    if not attempts_list:
        print("there is no high score , please play so you can get a score")
    else:
        print(f"the current high score is , {min(attempts_list)} attempts ")

attempts = 0

rand_number = random.randint(1 , 10)

print ("hello player ! welcome tho the guessing game ")

player_name = input("what is your name ? ")
want_to_play = input (
    f"Hi , {player_name} , whould you like to play guessing game ?"
    " (Enter Yes/ NO) "
).lower()

if want_to_play == "no":
    print("that's cool , thanks")
    exit()
else:
    show_score()

while want_to_play == "yes":
    try:
        guess = int(input("please insert a number between 1 - 10 : "))
        if guess < 1 or guess > 10:
            raise ValueError ("please insert a number within between 1 and 10")
        
        attempts+= 1

        if (guess == rand_number):
            print("coooool ,  you matched the guess")
            print(f"you got it in {attempts} attempts")
            want_to_play = input("do want to take another round (Enter Yes/No) : ")
            
            attempts_list.append(attempts)



            if want_to_play == "no":
                print("that's cool have a nice day")
            else:
                attempts = 0
                rand_number = random.randint(1 , 10)
                show_score()
                continue
        elif guess > rand_number:
            print("it's lower")
        else:
            print("it's higher")
            
    except ValueError as err:
        print(err)


"""
using except here will make us contiue using the game even if an error ocur 
for example if we entered any value other than a number in the expected range for example any text it will give us error , 
an move us back to enter the intger in the given range 
but we used finally and iserted a value other than int it will let you to insert an error message but will exit the 
programm directly if you inserted any thing other than expected value in this case the number 
"""