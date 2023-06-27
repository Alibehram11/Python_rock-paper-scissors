import random
computer = 0
you = 0

game = ["rock ","paper","scissors"]
print("Welcome to "Rock Paper Scissors Game Please Choose Something")
while True:
    query = str(input(rock Paper Scissors:"))
    query.lower()
    guess = random.choice(game)
    print("guess:",guess)
    print("you:",query)


    if query not in game:
        print("you have not made a valid choice")
        continue

    if query == guess:
        print("deuce")
    
    elif (query == "rock" and guess == "scissors") or (query == "scissors" and guess == "kağıt") or (query == "kağıt" and guess == "rock"):
        print("congratulations you win")
        you+=10
        print("me",you)
    else:
        print("you lost")
        bilgisayar+=10
        print("computer",computer)

    if 20 == you or 20 == computer:
        print("me",you)
        print("computer",computer)
        break




