"""
Crear una matriz de 5x5 randomizada con números enteros, encontrar secuencia de 4
números consecutivos horizontal o vertical y si se encuentra mostrar la posición inicial y
final.
"""

import numpy as np
import random
import doctest

def generate_matrix():
    """
    Genera una matriz de 5x5 randomizada con numeros enteros

    >>> len(generate_matrix())
    5
    """
    result = np.random.randint(0, 5, (5, 5))
    return result

def search(matrix):
    find_sequence(matrix)
    find_sequence(np.transpose(matrix), True)

def find_sequence(matrix, is_transpose=False):
    """
    Busca por las filas y columnas de la matriz si existe una secuencia de 4 elementos consecutivos
    >>> find_sequence([[4, 0, 1, 2, 3],[4, 1, 3, 4, 3],[2, 4, 3, 0, 4],[1, 2, 3, 3, 4],[1, 4, 3, 1, 3]])
    Secuencia encontrada en la posición (01 04) (fila , columna)
    >>> find_sequence([[4, 4, 2, 1, 1],[0, 1, 4, 2, 4],[1, 3, 4, 5, 6],[2, 4, 0, 3, 1],[3, 3, 4, 4, 3]], True)
    Secuencia encontrada en la posición (12 42) (fila , columna)
    """
    cnt = 0
    for record in matrix:
        result = consecutive(record)
        if result != False:
            print(f"Secuencia encontrada en la posición ({print_position(result[0], cnt, is_transpose)} {print_position(result[1], cnt, is_transpose)}) (fila , columna)")
        cnt += 1

def print_position(position, cnt, is_transpose):
    """
    >>> print_position(1,2,False)
    '21'
    >>> print_position(1,2,True)
    '12'
    """
    nline = position if not is_transpose else cnt
    ncolumn = position if is_transpose else cnt
    return f"{ncolumn}{nline}"

def consecutive(data, stepsize=1):
    """
        Busca una secuencia de 4 elementos consecutivos
    
    >>> consecutive([4, 0, 1, 2, 3])
    [1, 4]
    >>> consecutive([0, 1, 2, 3, 5])
    [0, 3]
    """
    arr_consecutive = np.split(data, np.where(np.diff(data) != stepsize)[0]+1)
    index = 0
    for record in arr_consecutive:
        len_rec = len(record)
        if len_rec == 4:
            return [index, index  + len_rec -1]
        
        index += len_rec
    
    return False

if __name__ == '__main__':    
    doctest.testmod()