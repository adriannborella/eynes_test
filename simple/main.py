"""
SIMPLE
Hacer una función que genere una lista de diccionarios que contengan id y edad, donde
edad sea un número aleatorio entre 1 y 100 y la longitud de la lista sea de 10
elementos. retornar la lista.
Hacer otra función que reciba lo generado en la primer función y ordenarlo de mayor a
menor. Printear el id de la persona más joven y más vieja. Devolver la lista ordenada
"""

import random
import doctest

def generate_list():
    """Genera una lista de 10 diccionarios

    Retorna:
    list of dictionary { 'id': number, 'age': integer }
    >>> len(generate_list())
    10
    """
    result = []
    for cnt in range(10):
        result.append({
            'id' : cnt,
            'age' : random.randint(1,100)
        })

    return result

def order_list(list_to_order):
    """Ordena una lista de diccionarios segun la edad e 
    imprime los id del menor registro y del mayor

    Parametros:
    Una lista de elementos con la forma { 'id': number, 'age': integer}

    Retorna:
    La lista pasada como parametro ordenada por edad

    >>> order_list([{'id': 0, 'age': 18}, {'id': 1, 'age': 41}, {'id': 2, 'age': 88}, {'id': 3, 'age': 25}, {'id': 4, 'age': 3}, {'id': 5, 'age': 27}, {'id': 6, 'age': 30}, {'id': 7, 'age': 26}, {'id': 8, 'age': 97}, {'id': 9, 'age': 89}])
    4
    8
    [{'id': 4, 'age': 3}, {'id': 0, 'age': 18}, {'id': 3, 'age': 25}, {'id': 7, 'age': 26}, {'id': 5, 'age': 27}, {'id': 6, 'age': 30}, {'id': 1, 'age': 41}, {'id': 2, 'age': 88}, {'id': 9, 'age': 89}, {'id': 8, 'age': 97}]
    """
    result = sorted(list_to_order, key = lambda r: r['age'])
    print(result[0]['id'])
    print(result[-1]['id'])
    return result

if __name__ == '__main__':
    result = generate_list()
    order_list = order_list(result)
    doctest.testmod()
