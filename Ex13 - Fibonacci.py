def fibonacci(number)
  a=0
  b=1
  while number  0
    c=a+b
    a=b
    b=c
    number-=1
    print c
#or
def fib(n)
  listed = [1,1]
  while n0
    n-=1
    sumd = listed[-1]+listed[-2]
    listed.append(sumd)
  return listed
#input 
numb = int(input(Enter any number ))
print fib(numb)
fibonacci(numb)
 
 