def year(name,age,copy):
  total = 100-age
  add = 2017+total
  i=1
  while i<=copy:
    print "Name : %s" % name
    print "You will be 100 years in the year: %s" % add
    i+=1
  
names = raw_input("Enter your name: ")
aged = int(raw_input("Enter your age: "))
copies = int(raw_input("Enter the number of copies: "))
year(names,aged,copies)

<script src="https://gist.github.com/anonymous/b86feba7debd0b98b5df39e15567bc4c.js"></script>