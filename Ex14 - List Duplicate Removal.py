def list_duplicate(listed):
  output_list = []
  output_list = [listed[0]]
  for elem in listed:
    if elem > output_list[-1]:
      output_list.append(elem)
  
  return output_list    
  
#print list_duplicate([1,1,2,3,2,1,4])  
def set_duplicates(listed):
  output_set = set()
  listed = set(listed)
  return list(listed)
  
def set_intersect(list1,list2):
  list1 = set_duplicates(list1)
  list2 = set_duplicates(list2)
  list1 = set(list1)
  list2 = set(list2)
  return list(list1|list2)
  
  
def main():
  input_list = input("Enter a list of numbers : ")
  print list_duplicate(input_list)
  print set_duplicates(input_list)
  list1 = input("Enter list 1: ")
  list2 = input("Enter list2 : ")
  print set_intersect(list1,list2)
  
main()  

https://gist.github.com/anonymous/b3d05503dfc30b564f4695c4f34139da
