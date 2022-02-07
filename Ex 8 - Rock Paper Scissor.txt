def rsp_game(user_choice1,user_choice2):
  str = ""
  if user_choice1 == "rock" and user_choice2 == "scissor":
    str = "User1 wins!!"
  elif user_choice1 == "rock" and user_choice2 == "paper":
    str = "User2 wins!!"
  elif user_choice1 == "scissor" and user_choice2 == "rock":
    str = "User2 wins!!"
  elif user_choice1 == "scissor" and user_choice2 == "paper":
    str = "User1 wins!!"
  elif user_choice1 == "paper" and user_choice2 == "rock":
    str = "User1 wins!!"
  elif user_choice1 == "paper"  and user_choice2 == "scissor":
    str = "User2 wins!!"
  else:
    str = "User inputs were not valid"
  return str  

def main():
  choice = input("Do you still want to play: Y/N")
  choice = choice.lower()
  while choice == "y":
    user1 = input("Enter user choice: ")
    user1 = user1.lower()
    user2 = input("Enter user choice: ")
    user2 = user2.lower()
    print rsp_game(user1,user2)
    choice = input("Do you still want to play: Y/N")
    choice = choice.lower()
    

main()

https://gist.github.com/anonymous/f36160adc6fea4d7784f0998e6b21cb5