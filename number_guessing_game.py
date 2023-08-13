import random

targ_num = random.randint(0, 100)
attempts = 0
score = 0
play = True

while play and attempts <= 10:
    guess = int(input("Enter any number between 1 to 100 "))
    attempts += 1
    score = 10-attempts

    if guess == targ_num:
        print(f"congratulations you guessed correct answer in {attempts} attempts and your score is {score}")
        break
    elif guess > targ_num:
        print("Guess is too high")
        score-=1
    else:
        print("Guess is too low")
        score-=1

    play_again = input("You want to continue playing, Enter Y for yes or N for no ")
    if play_again == "N":
        play = False

print(f"Your score is {score}")
