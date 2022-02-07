def unique_list(listed):
  listed = sorted(listed)
  output_list = []
  output_list = [listed[0]]
  
  for elem in listed:
    if elem > output_list[-1]:
      output_list.append(elem)
      
  return output_list
  
def main():
  list1 = input("Enter first list:")
  list2 = input("Enter second list:")
  new_list1 = unique_list(list1)
  new_list2 = unique_list(list2)
  for element in new_list2:
    new_list1.append(element)
  
  
  new_list1 = sorted(new_list1)
  print unique_list(new_list1)
  
main()  

https://gist.github.com/anonymous/f6b1ef67913269964b8b06654d5ea25d