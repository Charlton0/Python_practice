# Global variable- is created outside a function and can be used both inside and outside of a function by everyone
# when a variable is created inside a function it is called a local variable and it can only be used within that function
# use the keyword 'global' to create a global variable inside a function
# also use 'global' keyword 

x = "awesome" #global variable
def myfunc():
    print("Python is", + x)

    myfunc()

    # when you create a variable inside a function with the same name as that of the global variable
    # but with a different value, it overrides the global one 

    x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

# therefore to change the value of a global variable inside a func, use the keyword "global"
x = "awesome"

def myfunc():
   global x
   x = "fantastic"


   myfunc()

   print("Python is", + x)