elements = [1,1,2,5,8,13,21,34,55,89]

def list_print(element):
  new_list = []
  for x in element:
    if x < 5:
      print x
      new_list.append(x)
  return new_list

def user_list_print(element,number):
  new_user_list = []
  for x in element:
    if x < number:
      print x
      new_user_list.append(x)
  return new_user_list
  
def main():
  print list_print(elements) #less than 5
  numbers = int(input("Enter a number:"))
  print user_list_print(elements,numbers) #less than user input
  
  print([x for x in [1,1,2,5,8,13,21,34,55,89] if x < 5]) #in one line
  print([x for x in elements if x < 5]) #or
  #print(x for x in [1,1,2,3,6,8,13,21,34,55,89] if x < 5)
  #for y in [x for x in [1,1,2,3,6,8,13,21,34,55,89] if x < 5]: print y

 main()  
https://gist.github.com/anonymous/36f54fbf2de2edb5b4967def0a1e8a7f

