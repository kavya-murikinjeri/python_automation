# A function is a reusable block of code that performs a specific task. 
# Functions help make programs more organized, readable, and easier to maintain.
'''
 def function_name(parameters):
    # Function body
    return value
'''
# function without argu,emts
'''
def add():
    print(10+30)

add()
add()

'''
#function with arguments
'''

def sub(a,b):
    print(a-b)

sub(20,10)
sub(40,10)
'''

# function with return value
#The return statement is used inside a function to send a value back to the place where the function was called. 
# When Python executes a return statement, the function immediately stops executing.

'''
print() vs return
print()	                               return
Displays output on the screen	Sends a value back to the caller
Cannot be reused in calculations	Returned value can be stored or used in expressions
Does not end the function	Immediately ends the function

'''
def mult(a,b):
    return a*b
result=mult(10,20)
print(mult(20,20))
print(result)
