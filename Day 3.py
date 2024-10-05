print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
road = input("You're at a cross road. Where do you want to go?\n    Type 'left' or 'right'\n")
if road == "left":
    print("You've come to a lake. There is an island in the middle of the lake.")
    swim = input("Type 'wait' to wait for a boat. Type 'swim' to swin across.")
    if swim == "wait":
        print("You arrive at the island unharmed. There is a house with 3 door. One red, one yellow and one blue.")
        door = input("Wich colour do you choose?")
        if door == "yellow":
            print("You win!")
        elif door == "red":
            print("Burned by fire. Game Over.")
        elif door == "blue":
            print("Eaten by beasts. Game Over.")
        else:
            print("Game Over.")
    else:
        print("Attacked by trout. Game Over.")
else:
    print("Fall into a hole. Game Over.")