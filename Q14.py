def ispowoftwo(n):
	if (n == 0):
		return 0
	while (n != 1):
		if (n%2 != 0):
			return 0
		n = n/2
  	return 1

n=input("Enter the number\n")
c=ispowoftwo(n)
if c==1:
	print("n is a power of 2\n")
else: 
	print("n is not a power of 2\n")
