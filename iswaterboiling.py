def repeat():
    temp = int(input("Temperature of the water: "))
    if temp >= 100:
        print("Boiling")
    else:
        print("Not boiling.")
        
        check = input("Do you want to quit or start again, enter Y to restart or another key to end: ")
    if check.upper() == "Y": #loop back to the start
         repeat()
         exit() #exit the program

repeat()

# Please support me on Patreon: patreon.com/pizzavitditt
