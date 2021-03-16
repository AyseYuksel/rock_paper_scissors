import random

move = ['Rock', 'Paper', 'Scissors']
computer_point = 0
player_point = 0

print("Score : \n")
print("Computer : " + str(computer_point) + "\n")
print("Player : " + str(player_point) + "\n")

run = True
while run:
    computer_decision = random.choice(move)
    command = input("Rock , Paper , Scissors or Quit ?")

    if computer_decision == command:
        print("tie")
    elif command == 'Rock':
        if computer_decision == 'Paper':
            print("Computer won ! ")
            computer_point += 1
        else:
            print("Player won ! ")
            player_point += 1
    elif command == 'Paper':
        if computer_decision == 'Rock':
            print("Player won !")
            player_point += 1
        else:
            print("Computer won !")
            computer_point += 1
    elif command == 'Scissor':
        if computer_decision == 'Paper':
            print("Player won !")
            player_point += 1
        else:
            print("Computer won !")
            computer_point += 1
    elif command == 'Quit':
        break
    else:
        print("Wrong move !")

    print("Player move :" + command + "\n")
    print("Computer move : " + computer_decision + "\n")
    print("Player point : " + str(player_point) + "\n")
    print("Computer point :" + str(computer_point) + "\n")