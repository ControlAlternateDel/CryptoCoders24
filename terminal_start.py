#This code is to be used in the terminal and takes the input grade level and returns the window.
print("Welcome to the adaptive test bot")
def main():
  print("Welcome to the adaptive test bot")
  level = input("Please enter your level(grade)\n")
  subj = input("Please enter your subject (Please note that you cannot enter a typo subject)\n")
  print("Please confirm that you are in grade " + level + " and your subject is " + subj + "\n You may change either by entering 'change'")
  confirm = input("Please enter 'confirm' to confirm or 'change' to change\n")
  if confirm.lower() == "confirm":
      print("Confirmed. Please go to the new window.")
  elif confirm.lower() == "change":
      print("Please re-enter your level and subject.")
      main()
main()

