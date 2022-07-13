def repeat():
    kilometers = int(input("Enter a value: "))
    miles = kilometers * 0.60934

    if kilometers >= 1:
         print(miles)
    else:
         print("Please enter a valid value.")
    check = input("Do you want to quit or start again, enter Y to restart or another key to end: ")
    if check.upper() == "Y": #loop back to the start
         repeat()
         exit() #exit the program

repeat()
