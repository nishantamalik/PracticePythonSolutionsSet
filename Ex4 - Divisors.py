def divisor(number):
  new_list=[]
  x = range(1,((number/2)+1))
  for elem in x:
    if number%elem==0:
      new_list.append(elem)
  
  return new_list    

def main():
  
  number = input("Enter any integer of you choice: ")
  print number, type(number)
  assert number>0 and type(number)!="int","Wrong input"
  print divisor(number)
  
main()  
  

https://gist.github.com/anonymous/ec91975707af033572077c2f70947283