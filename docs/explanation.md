# Solución

## Cuadratura gaussiana

El método de aproximación de la cuadratura gaussiana aproxima la integral de la siguiente forma:

$\int f(x)\ dx\approx \sum_{k=1}^{N}f(x_{k})\omega_{k}$

Donde los $x_{k}$ son los puntos de locación o nodos, y los $\omega_{k}$ son los pesos de la aproximación. Usando los polinomios de Legendre de grado N $(P_{N}(x))$, se pueden obtener estos puntos y pesos de la siguiente manera:

$P_{N}(x_{k})=0$

$\omega_{k} = \left[\frac{2}{1-x^2}\left(\frac{dP_{N}}{dx}\right)^{-2}\right]_{x={x_k}}$  

## Código

Por medio de la libreria de ##Numpy##, se tiene la función ´´´np.polynomial.legendre.leggauss(N)´´´. La cual obtiene los valores de $x_{k}$ y $\omega_{k}$ para un polinomio de Legendre de grado $N$.

El código realizado, aproxima la solución de la integral y grafica el valor obtenido respecto a los valores de $N$ entre 1 y 10.    
