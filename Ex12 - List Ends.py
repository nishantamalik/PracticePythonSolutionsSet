def list_ends(list1):
  length = len(list1)
  new_list=[]
  for index, item in enumerate(list1):
    if index == 0 or index == length-1:
      new_list.append(item)
      
  return new_list
  
  
def main():
  input_list = list(input("Enter a list of numbers :"))
  print list_ends(input_list)
  
main()  


#or
print((lambda list1 : [item for index,item in enumerate(list1) if index==0 or index==len(list1)-1])(input("Enter a list of numbers: ")))

https://gist.github.com/anonymous/1b31d84599b8f1234b303e6ed5a77469