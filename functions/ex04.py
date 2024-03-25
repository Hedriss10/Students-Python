

# função fibonnaci para recursividade 
def fibonnaci(n):
    # verificação encadeada 
    if n == 0:
        print(n)
        return 0 
    elif n == 1:
        return 1 
    else:
        return fibonnaci(n-1) + fibonnaci(n-2)
    
    
    
fibonnaci(2)