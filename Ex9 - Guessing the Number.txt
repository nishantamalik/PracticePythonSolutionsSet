import random

def random_guess(user_choice):
  #count = count + 1
  number = random.randint(1,9)
  str = ""
  if number == user_choice:
    str = "Exactly right"
  elif number > user_choice:
    str = "User input is greater than the number"
  elif number < user_choice:
    str = "User input is smaller than the number"
  else:
    str = "Wrong input entered by the user"
  return str
  
def user_choice():
  choice = input("Do you still want to guess: Y/N")
  choice = choice.lower()
  return choice
  
def main():
  choice = user_choice()
  while choice == "y":
    user_input = input("Enter your guess: ")
    print random_guess(user_input)
    choice = input("Do you still want to guess: Y/N")
    choice = choice.lower()
    
    
main()    

https://gist.github.com/anonymous/b1500371ee610c49ff28c45e18a46d80