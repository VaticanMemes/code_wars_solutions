def zero(operation = None): 
    if operation == None:
        return 0
    else:
        return int(operation(0))
def one(operation = None): 
    if operation == None:
        return 1
    else:
        return int(operation(1))
def two(operation = None): 
    if operation == None:
        return 2
    else:
        return int(operation(2))
def three(operation = None): 
    if operation == None:
        return 3
    else:
        return int(operation(3))
def four(operation = None): 
    if operation == None:
        return 4
    else:
        return int(operation(4))
def five(operation = None): 
    if operation == None:
        return 5
    else:
        return int(operation(5))
def six(operation = None): 
    if operation == None:
        return 6
    else:
        return int(operation(6))
def seven(operation = None): 
    if operation == None:
        return 7
    else:
        return int(operation(7))
def eight(operation = None): 
    if operation == None:
        return 8
    else:
        return int(operation(8))
def nine(operation = None): 
    if operation == None:
        return 9
    else:
        return int(operation(9))

def plus(number):
    return lambda y: y + number
def minus(number):
    return lambda y: y - number
def times(number):
    return lambda y: y * number
def divided_by(number):
    new_num = lambda y: y / number
    return new_num

"""
Dense code my ass lol
"""