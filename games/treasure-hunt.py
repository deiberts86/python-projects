print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
left_turn = "l" or "left" or "Left" or "L"
right_turn = "r" or "right" or "Right" or "R"

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
# Code will be below for user interactive choices
choice1 = input('You\'re at a crossroad, where do you want to go?'
                'Type "left" or "right".\n').lower()

if choice1 == "left":
    choice2 = input('You\'ve arrived near a lake shoreline. \n'
                    'There is an island with a house in the middle of it. \n'
                    'You see in the distance that there is a small boat arriving towards the shoreline. \n'
                    'You can wait it out and ask for a ride or make a swim towards the island itself. \n'
                    'Type "Swim" or "Wait".\n').lower()
    if choice2 == "wait":
        choice3 = input('You\'ve arrived on the island in the middle of the lake \n'
                        'from the person operating the boat. You\'re now at the house \n'
                        'but you have three choices to make for which color \n'
                        'door to choose to enter the strange looking house. \n'
                        'Choose "Yellow", "Red", or "Blue"\n ').lower()
        if choice3 == "blue":
            print("You were eaten by terrible beasts...Game Over!")
        elif choice3 == "yellow":
            print("You find treasure within a chest. You've Won!")
        elif choice3 == "red":
            print("Flame throwers torched you to a crisp... Game Over!")
        else:
            print("You didn't choose a door that exists.  You exploded... Game Over!")
    else:
       print('You\'ve been eaten by the legendary lake monster! Game Over')
else:
    print("You fell into a deep hole with spikes and died... Game Over!")
