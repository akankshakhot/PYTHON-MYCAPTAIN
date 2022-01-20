from collections import Counter
  
# initializing string 
string = "mississippi"
  
# using collections.Counter() to get 
# count of each element in string 
res = Counter(string)
  
# printing result 
print ("Count of all characters  is :\n "
                                           +  str(res))