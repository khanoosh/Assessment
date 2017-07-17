n=input("enter the number\n")
while (n>=1):
	if n%2==0:
		n=n/2
	else:
		print("Not a power of two\n")
		break
if n==1:
	print("n is a power of 2")