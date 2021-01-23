"""
Escribir una clase en python llamada círculo que contenga un radio, 
con un método que devuelva el área y 
otro que devuelva el perímetro del círculo.

Si se instancia la clase con radio <= 0 mostrar una excepción indicando un error amigable al
usuario e impidiendo la instanciación.

Si printeamos el objeto creado debe mostrarse una representación amigable.

El objeto debe tener su atributo radio modificable, si se le intenta setear un valor <= 0
mostrar un error y no permitir modificación.

Permitir la multiplicación del circulo: Circulo * n debe devolver un nuevo objeto con el radio
multiplicado por n. No permitir la multiplicación por números <= 0
"""
import math
import doctest

class Circulo():
    radio = False

    def __init__(self, radio):
        self.set_radio(radio)

    def get_area(self):
        """
        >>> Circulo(5).get_area()
        78.54
        """
        return round((self.radio ** 2) * math.pi, 2)
    
    def get_perimetro(self):
        """
        Devuelve el perimetro del objeto Circulo

        >>> Circulo(5).get_perimetro()
        31.42
        """
        return round(self.radio * 2 * math.pi, 2)
    
    def __str__(self):
        """
        >>> print(Circulo(5))
        Instancia del objeto Circulo de radio 5
        """
        return f"Instancia del objeto Circulo de radio {self.radio}"
    
    def set_radio(self, new_radio):
        """
        # >>> Circulo(1)
        
        >>> Circulo(0)
        Traceback (most recent call last):
        ...
        Exception: No puede crearse una instancia de la clase si el radio es menor o igual a Cero, ingrese una cantidad distinta y vuelva a intentarlo
        """ 
        self.validate_radio(new_radio)       
        self.radio = new_radio
    
    def validate_radio(self, radio):
        """
        >>> Circulo(1).validate_radio(1)
        True
        >>> Circulo(1).validate_radio(0)
        Traceback (most recent call last):
        ...
        Exception: No puede crearse una instancia de la clase si el radio es menor o igual a Cero, ingrese una cantidad distinta y vuelva a intentarlo
        """
        if(radio <= 0):
            raise Exception("No puede crearse una instancia de la clase si el radio es menor o igual a Cero, ingrese una cantidad distinta y vuelva a intentarlo")
        return True

    def __mul__(self, n):
        """
        >>> (Circulo(5) * 2).radio
        10
        >>> (Circulo(5) * 0).radio
        Traceback (most recent call last):
        ...
        Exception: No puede crearse una instancia de la clase si el radio es menor o igual a Cero, ingrese una cantidad distinta y vuelva a intentarlo
        """
        new_radio = self.radio * n
        self.validate_radio(new_radio)
        return Circulo(new_radio)

if __name__ == '__main__':
    doctest.testmod()