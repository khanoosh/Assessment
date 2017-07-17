number=input("Enter your number")
sum = 0
while number:
	sum += number % 10
	number //= 10
print("The sum of digits is " + str(sum))