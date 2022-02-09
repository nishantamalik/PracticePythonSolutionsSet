import random

def list_overlap(list1,list2):
  unique_list = [x for x in list1 for y in list2 if x==y]
  return unique_list

def clean_list(listed):
  output_list = []
  listed = sorted(listed)
  output_list = [listed[0]]
  for elem in listed:
    if elem > output_list[-1]:
      output_list.append(elem)
  
  return output_list    

def main():
  userlist1 = input("Enter list 1: ")
  userlist2 = input("Enter list 2: ")
  userlist1 = clean_list(userlist1)
  userlist2 = clean_list(userlist2)
  print "User list output :",list_overlap(userlist1,userlist2)
  new_list1 = range(0,random.randint(0,500))
  print new_list1
  new_list2 = range(0,random.randint(0,500))
  print new_list2
  print "User list output :",list_overlap(new_list1,new_list2)
  
  
main()  

httpsgist.github.comanonymousecfe6343f9adf22e94abf3c7e89ee943