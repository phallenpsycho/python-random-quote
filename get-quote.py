import random

def this():
  print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  last = len(quotes) - 1

  print(quotes[random.randint(0, last)])

if __name__== "__main__":
  this()
