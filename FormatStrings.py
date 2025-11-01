# format() method is use to combine strings and numbers
""" We can not combine numbers and strings in python as below;
age = 36
txt = "My name is Charles and I am " + age
print(txt)
"""
# combined using format() method, used to insert numbers into strings

age = 36
txt = 'My name is Charles, and I am {}'
print(txt.format(age))

# The format() method takes the passed arguments, formats them, 
# and places them in the string where the placeholders {} are
# the format() methods takes unlimited no. of arguments, and are placed into the respective placeholders

quantity = 3
itemno   = 123
price    = 49.50
myorder  = "I want {} pieces of item {} for {} dollars"
print(myorder.format(quantity, itemno, price))

# You can use the index numbers to be ensure that the arguments are placed in the correct placeholders
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

 