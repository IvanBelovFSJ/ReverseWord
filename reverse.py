# Tavonga Masheka T00600161
# Ivan Belov T00600161
# This project is in charge of reversing alphabetical content of any word
# provided by a user.

str=input("enter word") # initial string
stringlength=len(str) # calculate length of the list
slicedString=str[stringlength::-1] # slicing 
print (slicedString) # print the reversed string
