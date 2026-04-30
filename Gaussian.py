import numpy as np
import matplotlib.pyplot as plt


def func(xVal):
    """
    Evalúa la función a integrar.

    Calcula sin(x^2) para los valores de entrada.

    Parámetros
    ----------
        xVal : numpy.ndarray o float
            Valor(es) donde se evaluará la función.

    Retorna:
    ----------
        numpy.ndarray o float
            Resultado de evaluar sin(x^2) en xVal.

    Ejemplos:
    ----------
        >>> func(1.0)
        0.8414709848078965

        >>> func(np.array([0.0, 1.0]))
        array([0.0, 0.84147098])
    """
    return np.sin(xVal * xVal)


def gaussOriginal(N):
    """
    Obtiene nodos y pesos de Gauss-Legendre en el intervalo [-1, 1].

    Parámetros
    ----------
        N (int): Número de puntos de cuadratura.

    Retorna
    ----------
        numpy.ndarray:(xVal, weight), donde:
            - xVal: nodos de integración
            - weight: pesos asociados

    Ejemplos
    ----------
        >>> x, w = gaussOriginal(2)
        >>> x
        array([-0.577...,  0.577...])
        >>> w
        array([1.0, 1.0])
    """
    xVal, weight = np.polynomial.legendre.leggauss(N)
    return xVal, weight


def gaussInLimit(xInit, xFinal, xVal, weight):
    """
    Transforma nodos y pesos de Gauss-Legendre a un intervalo arbitrario.

    Realiza el cambio de variable desde [-1, 1] hacia [xInit, xFinal].

    Parámetros
    ----------
        xInit (float): Límite inferior de integración.
        xFinal (float): Límite superior de integración.
        xVal (numpy.ndarray): Nodos originales en [-1, 1].
        weight(numpy.ndarray): Pesos originales.

    Retorna
    ----------
        numpy.ndarray: ([xVal_transformado, weight_transformado])

    Ejemplos
    ----------
        >>> x, w = gaussOriginal(2)
        >>> x_new, w_new = gaussInLimit(0, np.pi, x, w)
        >>> x_new
        array([...])
    """
    return (
        0.5 * (xFinal - xInit) * xVal + 0.5 * (xFinal + xInit),
        0.5 * (xFinal - xInit) * weight
    )

def main()
    """
    Realiza una gráfica de las aproximaciones de la integral respecto a los valoenteros entre 1 y 10.  
    
    """    
    nVals = np.array([1,2,3,4,5,6,7,8,9,10])
    integVals = np.zeros(nVals.size)

    for i in range(nVals.size):
        gaussN = gaussOriginal(nVals[i])
        gaussNadj = gaussInLimit(0.0, np.pi, gaussN[0], gaussN[1])
        integVals[i] += np.sum(func(gaussNadj[0]) * gaussNadj[1])

    plt.plot(nVals, integVals)
    plt.grid()
    plt.xlabel("Valor de N")
    plt.ylabel("Aproximación de la integral")
    plt.show()

main()
