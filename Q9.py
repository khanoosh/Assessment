import re
# to use regular expression functions
def main():
	s= raw_input("Input your password")
	validate(s)

def validate(s):
	check = True
	while check:  
   		if (len(s)<6 or len(s)>12):
        		break
    		elif not re.search("[a-z]",s):
        		break
    		elif not re.search("[0-9]",s):
        		break
    		elif not re.search("[A-Z]",s):
        		break
    		elif not re.search("[$#@]",s):
    	    		break
    		elif re.search("\s",s):
    	 	   	break
    		else:
    	    		print("valid")
    	    		check=False
    	    		break
	if check:
		print("not valid")

main()