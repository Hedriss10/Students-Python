

def factorial(n):
    if not isinstance(n , int):
        print("Factorial is only defined for integers")
        return None 
    elif n < 0:
        print("Factorial is only defined for negative integers")
        return None
    elif n == 0:
        return 1 
    else:
        return n * factorial(n-1)
        
        
        
        
def factorial(n):
    space = ' ' * (4 * n)
    print(space, 'gpt35k', n)
    if n == 0:
        print(space, "returnig 1")
        return 1
    else:
        recurseve = factorial(n-1)
        result = n * recurseve
        print(space, 'parameters', result)
        return result
    




def b(z):
    prod = a(z, z)
    print((z, prod))
    return prod

def a(x, y):
    x = x + 1
    return x * y

def c(x, y, z):
    total = x + y + z
    square = b(total)**2
    return square

x =  1
y = x + 1

print(c(x, y+3, x+y))