def reverse_word(input_str):
  output_str = ""
  new_list = input_str.split()
  output_str = " ".join(new_list[::-1])
  return output_str
  

def main():
  input_str = input("Enter any sentence: ")
  print reverse_word(input_str)
  
main()  

https://gist.github.com/anonymous/8befd3e9cd954d0690651bbfeeeb9515