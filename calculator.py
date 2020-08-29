def add(x, y):
    return x + y

def factorial(x):
    if x < 0:
        return "This factorial only works with positiv real numbers"

    elif x == 0 or x == 1:
        return 1

    else:   
        a = 1
        for i in range(1,x+1):
            a = a*i

        return a