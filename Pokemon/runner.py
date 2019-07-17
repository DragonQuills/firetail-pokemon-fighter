from pokemonClass import Pokemon

def newPokemon():
    print ("Got it, create a new Pokeon.")
    newName = None
    species = None
    stats = [0, 0, 0, 0]

    allCorrect = "n"
    while allCorrect != "y":
        print ("Please enter their name.")
        newName = input(">>> ")
        print ("Please enter " + newName + "'s species.")
        species = input(">>> ")
        print ("Please enter " + newName + " the " + species + "'s stats")
        stats[0] = input("HP: ")
        stats[1] = input("Attack: ")
        stats[2] = input("Defense: ")
        stats[3] = input("Speed: ")

        print("")
        print("Here's the info you gave me...")
        print("")
        print("Name: " + newName)
        print("Species: " + species)
        print("HP: " + stats[0])
        print("ATK: " + stats[1])
        print("DEF: " + stats[2])
        print("SPD: " + stats[3])
        print("")
        print("Is that all correct?")
        allCorrect = input(">>> ")[0].lower()

    print("Got all that! Your new Pokemon has been created.")
    print("")
    return







choice = "0"
while choice != "3":
    print ("Welcome Firetail! What would you like to do?")
    print ("1. Create a new Pokemon")
    print ("2. Change the stats of an existing Pokemon")
    print ("3. Quit")
    choice = input(">>> ")
    print("")

    if(choice == "1"):
        newPokemon()
