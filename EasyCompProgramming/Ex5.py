# Problema: tomar array y retornar el numero mas alto que aparece exactamente su cantidad de veces. Ejemplo: [2,4,2,3,5,2,7,4,4,4]
# Esto retorna 4 ya que se repite exactamente 4 veces. 2 se repite dos veces tambien pero es menor que 4.

# ESTE PROBLEMA LO TUVE QUE HACER EN 50 MIN APROX. Esto fue lo mejor que se me ocurrio para hacerlo lo mas eficiente posible

def ordenarArray(A):
    if len(A) == 0:
        return []
    else:
        left = []
        right = []
        pivot = A[0]
        
        for i in range(1,len(A)):
            if A[i] < pivot:
                left.append(A[i])
            else:
                right.append(A[i])

        return ordenarArray(left) + [pivot] + ordenarArray(right)

def solution(A):
    # write your code in Python 3.6
    B = ordenarArray(A)
    res = 0
    iter = 0
    cont = 0
    actual = B[0]
    while iter < len(B):
        if B[iter] == actual:
            cont = cont + 1
            if cont == actual and iter == len(B) - 1:
                res = actual
        else:
            if cont == actual:
                res = actual
            actual = B[iter]
            cont = 1
        iter = iter + 1
    return res

print(solution([1,2,4,5,2,6,7,6,4,3,4,5,6,6,5,4,7,7,7,7,7,7]))