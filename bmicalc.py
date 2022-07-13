def repeat():
    weight = int(input("Your Weight: "))
    height = float(input("Your Height: "))

    bmi = weight / height ** 2

    if bmi <= 18.5:
        print("Underweight")
    elif bmi >= 18.5 and bmi <= 25:
        print("Normal")
    elif bmi >= 25 and bmi <= 30:
        print("Overweight")
    elif bmi >= 30:
        print("Obesity")

    check = input("Do you want to quit or start again, enter Y to restart or another key to end: ")
    if check.upper() == "Y": #loop back to the start
         repeat()
         exit() #exit the program

repeat()
