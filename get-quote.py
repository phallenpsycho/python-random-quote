import random
need = input('How many quotes would you like? ')
def this():
  #print("Keep it logically awesome.")
    for x in range(int(need)):
        f = open("quotes.txt")
        quotes = f.readlines()
        f.close()

        last = len(quotes) - 1
        a = quotes[random.randint(0, last)]
        rnd = []
        rnd.append(a)


        print(''.join(rnd), end='')

if __name__== "__main__":
  this()
