def prime(num):
  new_list = [x for x in range(2,((num/2)+1)) if num%x == 0]
  if new_list == []:
    print "Prime"
  else:
    print "Not Prime"
    
def main():
  prime(int(input("Enter any number: ")))
  
main()  


https://gist.github.com/anonymous/a5aa3519a6d0ce99ed00605f531835f2