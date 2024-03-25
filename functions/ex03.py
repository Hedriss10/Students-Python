

# função fatorial

def fatorial(n):
    if n == 0:
        return 1 
    else:
        recurse = fatorial(n-1)
        result = n * recurse
        return result
    
def countdow(n):
    if n <= 10:
        print("Parabéns seu número é maior menor ou igual a zero.")
    else:
        recurse = countdow(n-1)
        return recurse

