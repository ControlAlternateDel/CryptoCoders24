def main():
    print("Welcome to the Adaptive Test bot")
    level = input("Please enter your level(grade)\n")
    subj = input("Please enter your subject\n")
    print("Please confirm that you are in grade " + level + " and your subject is " + subj + "\n You may change either by entering 'change'")
    confirm = input("Please enter 'confirm' to confirm or 'change' to change\n")
    if confirm == "confirm":
        print("Confirmed. Please go to the new window.")
    elif confirm == "change":
        print("Please re-enter your level and subject.")
        level = input("Enter your new level")
        main()

