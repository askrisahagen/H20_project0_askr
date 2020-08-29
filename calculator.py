def add(x, y):
    return x + y

def factorial(x):
    if x < 0 or type(x) != int:
        return "This factorial only works with integers"

    elif x == 0 or x == 1:
        return 1

    else:   
        a = 1
        for i in range(1,x+1):
            a = a*i

        return a

def sin(x,n):
    a = 0
    for i in range(n+1):
        a += (-1)**i*x**(2*i+1)/factorial(2*i+1)
    
    return a