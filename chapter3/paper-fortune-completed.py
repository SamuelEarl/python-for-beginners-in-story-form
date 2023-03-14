# Paper Fortune

fortune1 = "Your luck is about to change"
fortune2 = "Something good is going to happen tomorrow"
fortune3 = "You will live a long and happy life"
fortune4 = "Someone likes you"
fortune5 = "Go do it!"
fortune6 = "Everything will work out"
fortune7 = "Good things are coming your way"
fortune8 = "You are going to be tired if you stay up too late playing this game"

choice = ""

while choice != "stop":
    print("")
    print("Welcome To Your Paper Fortune!")
    choice = input("Enter a color and press the enter key (red, blue, green, orange): ")

    if choice == "stop":
        break
    # If blue or orange, then display the even numbered fortunes.
    elif len(choice) % 2 == 0:
        selection = input("Choose a fortune (2, 4, 6, 8): ")
        fortune = int(selection)
        if fortune == 2:
            print(fortune2)
        elif fortune == 4:
            print(fortune4)
        elif fortune == 6:
            print(fortune6)
        else:
            print(fortune8)
    # Otherwise display the odd numbered fortunes.
    else:
        selection = input("Choose a fortune (1, 3, 5, 7): ")
        fortune = int(selection)
        if fortune == 1:
            print(fortune1)
        elif fortune == 3:
            print(fortune3)
        elif fortune == 5:
            print(fortune5)
        else:
            print(fortune7)

print("Game over!")
