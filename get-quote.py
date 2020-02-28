import random
def important():
   #print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last = 13
  rnd = random.randint(0, last)
  print("{0} {1} {2}".format(quotes[rnd],quotes[random.randint(0,last)],quotes[random.randint(0,last)]).replace("\n",""))

if __name__== "__main__":
  important()
