# Idea de este ejercicio --> arreglar el codigo de manera que devuelva el elemento mas chico de un array no vacio


def solution(A):
    ans = A[0]  # esto es lo que puse para arreglarlo
    # ans = 0   # Esto es lo decia
    for i in range(1, len(A)):
        if A[i] < ans:
            ans = A[i]
    return ans

