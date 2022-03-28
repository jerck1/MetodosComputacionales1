# <center> Operaciones con Matrices <center>

import numpy as np
import sympy as sy
## Suma


def suma(A,B):
    A=np.array(A)
    B=np.array(B)
    return A+B
def producto_escalar(k,A):
    A=np.array(A)
    return k*A
def producto(A,B):
    A=np.array(A)
    B=np.array(B)
    try:
        return A@B
    except:
        return "Matrices incompatibles"

A=[[1,2,3],[4,5,6]];B=[[6,5,4],[3,2,1]]; C=[[1,2],[3,4],[5,6]];D=[[1,2],[3,4]]; k=np.pi
print(suma(A,B))
print(producto_escalar(k,A))
print(producto(A,C))
print(np.shape(A))
A=sy.Matrix(A)
C=sy.Matrix(C)
D=np.matrix(D)
print(D.getH())
print(np.linalg.inv(D)*np.linalg.det(D))
print(A)

