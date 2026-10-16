room = "starting"
power = 0
game_running = True

while game_running:
    if room == 'starting':
        print("You are trapped in a dark cave. Looking up, there's a hole where you can see the sky, you need two powers to get up. In front, there is a exit.")
        print("If you want to try climbing up to the hole, enter '1'. To exit the cave, enter '2'")
        
    answer = input ("1-2: ")

    if answer == "1":
        room = "hole"
    elif answer == "2":
        room = "exit"
    else:
        print("Wrong answer traveller!")
    if room == "hole":
        if power >= 2:
            print ("You climbed through the hole and escaped!")
            game_running = False
        else:
            print ("You need two powers to get through this door, but you only have " + str(power) + "!")
            print("You slide back down to the cave floor.")
            room = 'starting'
    elif room == "exit":
        print("You have exited. To your left, you see a math puzzle. To your right, you see a word puzzle.")
        print("Enter '1' to do the math puzzle, enter '2' to do the word puzzle, enter '3' to go back to the cave")

        answer = input("1-3: ")


        if answer == "1":
            room = "math"
        elif answer == "2":
            room = "word"
        elif answer == "3":
            room = "starting"
        else:
            print ("Wrong answer traveller!")

        if room == "math":
            print("You see in front of you the following puzzle:")
            print("3 + 4 * 2")
            print("choose your answer below:")
            print("a: 8")
            print("b: 11")
            print("c: 14")
            print("d: 18")
            answer = input("a-d: "). lower()
            
        if answer == "a" or answer == "c" or answer == "d":
            print("Sorry, that is incorrect")

        elif answer == "b":
            print("That is correct! You have been awarded 1 power")
            power += 1
            room = "exit"
        else:
            print("Sorry, that is incorrect")
            room = "exit"

        if room == "word":
            print("You meet a wizard")
            print('He says "I am a wizard! Here is a riddle. Im tall when Im young and short when Im old. What am I?" ')
            print("type your answer below")

        if answer == "candle" or answer == "pencil":
                print("The wizard smiles. Correct! I award you 1 power")
                power += 1
                room = "exit"
        else:
            print("The wizard shakes his head.")
            room = "exit"