def soma(x, y):
    """Soma x + y
    >>> soma (10, 20)
    30 
    >>> soma (250, 100)
    350
    >>> soma ('20', 20)
    Traceback (most recent call last):
    ...
    AssertionError: x precisa ser int ou float
    """
    assert isinstance(x,(int, float)), 'x precisa ser int ou float'
    assert isinstance(y,(int, float)), 'y precisa ser int ou float'
    return x + y 

def subtrai(x, y):
    """Subtrai x e y
    >>> subtrai (10, 5)
    5
    >>> subtrai ('100' , 50)
    Traceback (most recent call last):
    ...
    AssertionError: x precisa ser int ou float
    
    """
    assert isinstance(x,(int, float)), 'x precisa ser int ou float'
    assert isinstance(y,(int, float)), 'x precisa ser int ou float'
    return x - y 



if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
