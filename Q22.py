import string
sent=raw_input("Enter the sentence\n")
letters=0
digit=0
for i in sent:
    if i.isalpha():
        letters+=1
    elif i.isnumeric():
        digit+=1
print("LETTERS "+str(letters))
print("DIGITS "+str(digits))