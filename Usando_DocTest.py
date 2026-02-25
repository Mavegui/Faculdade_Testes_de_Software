import doctest

def maximo(x, y):
    """
    Retorna o valor maior entre x e y.
    
    Executar código: 
        - python3 Usando_DocTest.py -v 
    
    Exemplos:
    >>> maximo(10, 20)
    20
    
    >>> maximo(30, 20)
    30
    
    >>> maximo(100, 100)
    100
    
    """
    if x > y:
        return x
    else:
        return y
    
if __name__ == "__main__":
    doctest.testmod()