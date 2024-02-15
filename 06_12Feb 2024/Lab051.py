# Match case
# Switch
numbers = int(input("Enter the number 1-3\n"))
match numbers:  # Break is not needed in case of Match and case
    case 1:
        print("You have entered 1")
    case 2:
        print("You have entered 2")
    case 3:
        print("You have entered 3")
    case _:
        print("No idea")
