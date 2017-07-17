from ast import literal_eval

l = literal_eval(raw_input("Enter a list of tuples: "))
print("Sorted\n")
print(sorted(l,key=lambda x: x[1]))

