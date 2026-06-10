# Fichero: vectores.py
# Descripción: Multiplicación de vectores y ortogonalidad

class Vector:    ## declaración clase
    # Tests unitarios:
    """
    >>> v1 = Vector([1, 2, 3])
    >>> v2 = Vector([4, 5, 6])
    >>> print(v1 * 2)
    [ 2 4 6 ]
    >>> print(v1 * v2)
    [ 4 10 18 ]
    >>> print(v1 @ v2)
    32
    >>> v1 = Vector([2, 1, 2])
    >>> v2 = Vector([0.5, 1, 0.5])
    >>> print(v1 // v2)
    [ 1.0 2.0 1.0 ]
    >>> print(v1 % v2)
    [ 1.0 -1.0 1.0 ]
    """
    vector = []
    def __init__(self, numeros): #constructor que toma un iterable y almacena sus valores en una lista
        self.vector = [numero for numero in numeros]

    def __repr__(self): #configuración representación textual
        return 'Vector(' + repr(self.vector) + ')'

    def __str__(self): #configuración representación textual para print()
        str_ = '['
        for componente in self.vector:
            str_ += ' ' + str(componente)
        str_ += ' ]'
        return str_

    def __getitem__(self, key):  #permite lonchas desde inicio o final, devuelve key de un tipo comp. o cont.
        return self.vector[key]    #getitem ahora convierte la clase com oiterable, permitiendo su uso en bucles

    def __setitem__(self, key, value): #con éste método podemos asignar valores a los elementos o lonchas del vector
        self.vector[key] = value

    def __len__(self): #devuelve el número de elmentos del vector
        return len(self.vector)

    ##Sobrecarga de operadores aritméticos
    def __add__(self, other):
        if isinstance(other, (int, float, complex)):
            return Vector(uno + other for uno in self)
        else:
            return Vector(uno + otro for uno, otro in zip(self, other))

    __radd__ = __add__ #nos permite sumarle un vector a un número o lista de números (para commutación en suma)
    """
    Resta en clase vector
    """
    def __neg__(self):
        return Vector([-1 * item for item in self])

    def __sub__(self, other):
        return -(-self + other)

    def __rsub__(self, other):   # __rsub__ no es = a __sub__ debido a que no hay conmutatividad
        return -self + other
    """
    multiplicación en clase vector
    """

    def __mul__(self, other):
        if isinstance(other, (int,float)):
            return Vector([x * other for x in self])

        if isinstance(other, Vector):
            if len(self) != len(other): #verificación los dos vectores son igual de largos
                raise ValueError("Los vectores deben tener la misma longitud")
            return Vector([x * y for x, y in zip(self, other)])

        return NotImplemented
    def __rmul__(self, other):
        return self.__mul__(other)
    # producto escalar
    def __matmul__(self, other):
        if not isinstance(other, Vector):#verificación other es un Vector
            return NotImplemented
        
        if len(self) != len(other):
            raise ValueError("Los vectores deben tener la misma longitud")
        
        return sum(x * y for x, y in zip(self, other))

    # (por simetría)
    __rmatmul__ = __matmul__

    def __floordiv__(self, other): #operador //
        if not isinstance(other, Vector): #verificación other es un Vector
            return NotImplemented
        if len(self) != len(other): #verificación los dos vectores son igual de largos
            raise ValueError("Los vectores deben tener la misma longitud")

        denom = other @ other #producto escalar del segundo vector
        if denom == 0: #si fuera 0, no tendria diracción y no podriamos trabajar
            raise ValueError("No se puede proyectar sobre el vector nulo")

        factor = (self @ other) / denom  #cálculo producto escalar v1 * v2 / denom qeu es el prdocuto escalar del sugndo vector
        return factor * other  #obtención vector paralelo a v2

    __rfloordiv__ = __floordiv__ #conmutación(simetria)

    def __mod__(self, other): #operador %
        if not isinstance(other, Vector): #verificación other es un Vector
            return NotImplemented

        return self - (self // other) #v1 perpendicular = v1 - v1 paralelo

    __rmod__ = __mod__ #conmutación (simetria)

if __name__ == "__main__":
    import doctest
    doctest.testmod()