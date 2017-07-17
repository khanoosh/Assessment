l=[1,2,3,4,6,7,8]
missing=sum(xrange(l[0],l[-1]+1)) - sum(l)
print("missing element from list "+str(l)+" is")
print(missing)
