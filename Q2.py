from __future__ import print_function

n=input("Input number of lines\n")
A = 65
for i in range(0, n):
	for j in range(0, i+1):
		ch = chr(A) 
            	print(ch, end=" ")
   		A=A+1
        print("")
 