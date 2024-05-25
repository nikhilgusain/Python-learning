#
def causeError1():
    try:
        div = 1/0
        print(div)
    except Exception as ex:
        print(ex) # this will print the error
    try:
        div = 1/0
        print(div)
    except Exception : # this will print user message
        print("There was some error")

#causeError1()

def causeError2():
    try:
        div = 1 + "a"
        print(div)
    except TypeError: # specific handling
        print("There was type error")
    except ZeroDivisionError:
        print("zero div error")
    except Exception: # general handling 
        print("tere was some error")


#causeError2()

# finally is always executed
try:
    print(1/0)
except Exception as ex:
    print(ex)
finally:
    print("this will always execute")



def handleException(func):
    def wrapper(*args):
        try:
            func(*args) # Call the wrapped function
        except TypeError:
            print("There was type error")
        except ZeroDivisionError:
            print("zero div error")
        except Exception:
            print("there was some error")
    return wrapper

@handleException # same name as function name 
def causeError():
    return 1/0

print(causeError())

# RASING AN ERROR

@handleException
def raiseError(n): # only acceots non zero values
    if n == 0:
        raise Exception
    print(n)

raiseError(0)

# custom exception

class customException(Exception):
    pass

def causeError4():
    raise customException()

causeError4()