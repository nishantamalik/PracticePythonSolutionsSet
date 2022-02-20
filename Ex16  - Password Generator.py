import random

def generate_password(choice = "strong"):
  word_list = ["asz","qdl","lrz","gir","ezc","koa","aas","bop","wek","str"]
  input_str_list = ["@","_",".","!","\"","#","$","%","&","\'","(",")","*","+",",","-",":",";","<",	"=",">","?","[","\\","]","^","`","{","|","}","~"]
  input_alpha_list = ["q","w","e","r","t","y","u","i","o","p","l","k","j","h","g","f","d","s","a","z","x","c","v","b","n","m"]
  outputlist = []
  iter=0
  new_str = ""
  if choice == "weak":
    outputlist = random.sample(word_list,2)
    return "".join(outputlist)
  elif choice == "strong":
    output_number_list = random.sample(range(0,10),3)
    output_str_list = random.sample(input_str_list,3)
    output_alpha_list = random.sample(input_alpha_list,3)
    
    while iter<=3:
      outputlist.append(random.sample(output_number_list,1))
      print outputlist
      outputlist.append(random.sample(output_alpha_list,1))
      print outputlist
      outputlist.append(random.sample(output_str_list,1))
      print outputlist
      iter+=1
    outputlist = [b for a in outputlist for b in a]
    random.shuffle(outputlist)
    for elem in outputlist:
      new_str = new_str+str(elem)
    
    return new_str
    
print(generate_password())    