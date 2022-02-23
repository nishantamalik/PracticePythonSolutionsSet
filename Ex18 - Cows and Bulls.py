import random

def cowsandbulls(input_number):
  number = random.randint(1000,9999)
  cows=0
  bulls=0
  print number
  print input_number
  for n,k in zip(str(number),str(input_number)):
    if n == k:
      cows+=1
  print "Cows : "+str(cows)
  
  for index1,item1 in enumerate(str(number)):
    for index2,item2 in enumerate(str(input_number)):
      
      if index1!= index2:
        
        if item1 == item2:
           
          bulls+=1    
  
  print "Bulls : "+str(bulls)    
  
def main():
  input_number = input("Enter any number: ")
  cowsandbulls(input_number)
  
main()  

https://gist.github.com/anonymous/a7073bab890b9bd2d22a79582429de67