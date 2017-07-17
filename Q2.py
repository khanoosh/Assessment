from __future__ import print_function
for i in range(0,5):
	j=0
	while (j<=i):
		c=chr(65+i+j)
		print(c,end='')
		j=j+1
	print('')
