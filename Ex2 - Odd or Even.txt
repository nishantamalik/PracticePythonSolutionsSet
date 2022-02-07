def evenodd(number):
  if number%2==0:
    print "Number is even"
    return "True"
  elif number%2!=0:
    print "Number is odd"
    return "False"
  else:
    print "Not valid"
def multipleof4(number):
  if number%4==0:
    return "True"
  else:
    return "False"
    
def call_check(num,check):
  assert num>0, "Number cannot be zero"
  assert check>0, "Number cannot be zero"
  result = int(num/check)
  ans = evenodd(result)
  if ans=="True":
    print "Second number divides first number evenly"
  else:
    print "Second number does not divide the first number evenly"

def main():
  number = int(input("Enter the number: "))
  boo = multipleof4(number)
  if boo=="True":
    print "Number is a multiple of 4"
  else:
    print "Number is not a multiple of 4"
    evenodd(number)
  num = int(input("Enter the first number"))
  check = int(input("Enter the second number"))
  call_check(num,check)
main()

https://gist.github.com/anonymous/31454f1021dbd6eb08d47340994bfc0e