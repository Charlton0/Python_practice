"""
Rules:
variable name must start with a letter or an underscore character
variable name can not start with a number 
variable name can only contain alphanumeric and underscore characters and underscores(A-Z,0-9 and _)
variable names are case sensitive (age,Age,AGE, are different variables)
"""
myNameIs = "Charles" # camel case technique for reading multi word variable names
_MyNameIs = "John" # pascal case
my_name_is = "Junior" # snake case
myname2 = "Felix"
myName = "Teacher"
myname = "Book"
MYNAME = "Kenya"

print(my_name_is)
print(_MyNameIs)
print(myNameIs)
print(myname2)
print(myname)
print(MYNAME)

# All the above are correct variable naming

#Below are wrong variable naming in python
#2myvar = "John"
#my-var = "John"
#my var = "John"