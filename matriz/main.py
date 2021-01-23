"""
Crear una matriz de 5x5 randomizada con números enteros, encontrar secuencia de 4
números consecutivos horizontal o vertical y si se encuentra mostrar la posición inicial y
final.
"""

import numpy as np
import random

def generate_matrix():
    """
    Genera una matriz de 5x5 randomizada con numeros enteros

    >>> len(generate_matriz())
    5
    """
    result = np.random.randint(0, 5, (5, 5))
    return result

def search(matrix):
    import ipdb; ipdb.set_trace()
    
    pass

if __name__ == '__main__':
    result = generate_matrix()    
    result = [
       [4, 0, 2, 1, 3],
       [4, 1, 3, 4, 3],
       [2, 4, 3, 0, 4],
       [1, 2, 3, 3, 4],
       [1, 4, 3, 1, 3]]
    search(result)
    doctest.testmod()