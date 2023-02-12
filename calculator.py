# Thank you to LearningLad for the education on this application.

#User will select what they want to do

while True:
    print("1 - Addition")
    print("2 - Subtraction")
    print("3 - Multiplication")
    print("4 - Division")
    print("Enter q or Q to Exit")

    #This handles what the user will select
    choice = input("Enter a Number: ")

    #This allows our user to quit by inputting the specified command.

    if choice == 'q' or choice == 'Q':
        break

    #This part the user will select what number they want to put in
    num1 = float(input("Enter Number 1: "))
    num2 = float(input("Enter Number 2: "))

    #System will determine what the user has selected and equate based off it.
    if choice == '1':
        print(num1, "+", num2, "=", (num1+num2))
    elif choice == "2":
        print(num1, "-", num2, "=", (num1-num2))
    elif choice == "3":
        print(num1, "*", num2, "=", (num1*num2))
    elif choice == "4":
        if num2 == 0.0:
            print ("Error. Divide by Zero.")
        else:
            print(num1, "/", num2, "=", (num1/num2))
    else:
        print("Not a valid option:")

    print()

#test item written
