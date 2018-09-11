# PGL(2,Z)
An implementation of the projective linear group of 2x2 matrices over the integers (extended modular group) as a Coxeter group in Sage.

## Example
    sage: load("pgl2z/pgl2z.py")
    sage: W = PGL2Z()
    sage: H = IwahoriHeckeAlgebra(ZZ, 0, 0, W)
    sage: T = H.T()
    sage: T1, T2, T3 = T.algebra_generators()
