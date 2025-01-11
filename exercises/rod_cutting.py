"""
Enunciado:
    Tenemos una varilla de longitud n pulgadas y una matriz de precios[].
    precio[i] denota el valor de una pieza de longitud i.
    Debemos determinar al máximo valor que se puede obtener al cortar la varilla y la venta de las piezas.
"""
#Resolución utilizando recursion O(n^n)
def cutRodRecur(i,price):
    if i == 0:
        return 0
    ans = 0

    for j in range(1,i+1): # j es el tamaño del corte actual que se está probando por i
        ans = max(ans, price[j - 1] + cutRodRecur(i - j,price))

    return ans

def cutRodR(price):
    n = len(price)
    return cutRodRecur(n,price)

price = [1,5,8,9]
print(cutRodR(price))

"""
cutRodRecur(4)
├── cutRodRecur(3) (j=1)
│   ├── cutRodRecur(2) (j=1)
│   │   ├── cutRodRecur(1) (j=1)
│   │   │   └── cutRodRecur(0) → devuelve 0
│   │   └── cutRodRecur(0) → devuelve 0
│   └── cutRodRecur(1) (j=2)
│       └── cutRodRecur(0) → devuelve 0
├── cutRodRecur(2) (j=2)
│   ├── cutRodRecur(1) (j=1)
│   │   └── cutRodRecur(0) → devuelve 0
│   └── cutRodRecur(0) → devuelve 0
└── cutRodRecur(1) (j=3)
    └── cutRodRecur(0) → devuelve 0
"""

#Metodo Top-Down DP (memoization) O(n)
"""
Memoization ayuda mediante el almacenamiento de los resultado de las costosas 
llamadas de función y la reutilización de ellos cuando los mismos insumos ocurren de nuevo.
"""
def  cutRodRecurMemoization(i,price,memo):
    if i == 0:
        return 0
    if memo[i - 1] != -1:
        return memo[i - 1]
    ans = 0

    for j in range(1,i+1):
        ans = max(ans,price[j - 1] + cutRodRecurMemoization(i - j,price,memo))
    memo[i - 1] = ans
    return ans

def cutRodMemoization(price):
    n = len(price)
    memo = [-1] * n
    return cutRodRecurMemoization(n,price,memo)

price = [1, 5, 8, 9]
print(cutRodMemoization(price))