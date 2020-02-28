import random
def important():
   #print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last = 13
  rnd = random.randint(0, last)
  print("{0} {1} {2}".format(quotes[rnd],quotes[random.randint(0,last)],quotes[random.randint(0,last)]).replace("\n",""))

def addquote():
	# Open the file in append mode(add items)
	f = open("quotes.txt","a")
	# ASk user for a new input
	quote = input("Enter a new quote:\n")
	# write to file
	f.write(quote+"\n")
	# Make changes
	f.flush()
	#close the file
	f.close()


if __name__== "__main__":
	# input is always a string cast it to int
	
	choice = int(input("Choose an option:\n1.Print random Qoute\n2.Add quote\n"))
	if  choice == 1:
		important()
	elif choice == 2:
		addquote()