# Paper Fortune

fortune1 = "Your luck is about to change"
fortune2 = "Something good is going to happen tomorrow"

print("Welcome To Your Paper Fortune!")
choice = input("Enter a color (red, blue, green, orange) then press the enter key: ")

if len(choice) % 2 == 0:
    print(fortune2)
else:
    print(fortune1)
    
print("Game over!")
