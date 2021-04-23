import random
def foo():
  print("Keep it logically awesome.")
  f = open("quotes.txt","a")
  f.write("Aguante linux\n")
  f.write("Aguante Ubuntu\n")
  f.write("Aguante Manjaro\n")
  f.write("Aguante Pop os\n")
  f.close()
  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  new_quotes = [line.replace("\n",'') for line in quotes]
  print(new_quotes[random.randint(0,len(new_quotes)-1)])
  print(new_quotes[random.randint(0,len(new_quotes)-1)])

if __name__== "__main__":
  foo()
