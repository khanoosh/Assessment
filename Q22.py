sent = raw_input("Enter the sentence\n")
digits=sum(c.isdigit() for c in sent)
letters=sum(c.isalpha() for c in sent)
print("LETTERS "+str(letters))
print("DIGITS "+str(digits))


