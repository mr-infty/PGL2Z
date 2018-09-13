# PGL(2,Z)
An implementation of the projective linear group of 2x2 matrices over the integers (extended modular group) as a Coxeter group in Sage.

## Usage example
    sage: from pgl2z.pgl2z import PGL2Z
    sage: W = PGL2Z()
    sage: s1, s2, s3 = W.gens()
    sage: s1.descents()
    sage: from pgl2z.chamber import FundamentalChamber as C0
    sage: C0.separated_from(s1*C0, C0.walls[0])
    sage: H = IwahoriHeckeAlgebra(ZZ, 0, 0, W)
    sage: T = H.T()
    sage: T1, T2, T3 = T.algebra_generators()
