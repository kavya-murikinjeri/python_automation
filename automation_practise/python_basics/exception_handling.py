# Exceptions occurs at thr runtime of a program
# we have try(code to be exceuted), except(catch the exception if any) and finally block(excecuted always)
#else block is executed ifthere is no exception caught
try:
    x=int(input("Enter number1: "))
    y=int(input("Enter number2: "))
    if y==0:
        raise Exception("The denominator is zero")
    res=x/y
    print(res)
except Exception as e:
    print(e)
    print("inside except block")
else:
    print("inside else block")
finally:
    print("This is executed always")