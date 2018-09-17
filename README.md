# PGL(2,Z)
An implementation of the projective linear group of 2x2 matrices over the integers (extended modular group) as a Coxeter group in Sage.

## Installation/Getting started

Clone the Git repository:

    > git clone https://github.com/mr-infty/PGL2Z.git

To use this package, change into the newly created directory (`PGL2Z`) and
start Sage as usual:

    > cd PGL2Z
    > sage

The package is available within Sage like any other Python package, i.e. can be
imported like

    > import pgl2z

(see usage example down below for more details).

## Staying Up-to-Date

To update to the newest version of this package, execute

    > git pull

from within the cloned Git repository (i.e. from `PGL2Z` or any
subdirectory).

## Usage example

In the hope that examples can serve as a substitute to a proper documentation
which hasn't been writen yet (and might never be), here are some:

    sage: from pgl2z.pgl2z import PGL2Z
    sage: W = PGL2Z()
    sage: s1, s2, s3 = W.gens()
    sage: s1.descents()
    sage: from pgl2z.chamber import FundamentalChamber as C0
    sage: C0.separated_from(s1*C0, C0.walls[0])
    sage: H = IwahoriHeckeAlgebra(W, 0, 0, ZZ)
    sage: T = H.T()
    sage: T1, T2, T3 = T.algebra_generators()

## A remark on Iwahori-Hecke algebras in Sage

Unfortunately, Iwahori-Hecke algebras in Sage aren't implemented in the
Bourbaki form, i.e. defined by relations of the form

    T^2 = bT + a

with parameters `a,b`, but instead in the less general 'split' form

    0 = (T-q_1)(T-q_2) = T^2 - (q_1+q_2) + q_1 q_2

with parameters `q_1,q_2`. Fortunately, for the purposes of mere computations
this isn't really a problem as you can do all computations in a localization of
the generic (universal) Hecke algebra over the ring `ZZ[a,b]` that is of the
split form.
Concretely,

    sage: S.<a,b> = ZZ['a','b']
    sage: L = S.fraction_field()
    sage: R.<Xbar> = L['X'].quotient(X^2 - (b**2 + 4*a))
    sage: q1 = (b+Xbar)/2
    sage: q2 = (b-Xbar)/2
    sage: H = IwahoriHeckeAlgebra(W, q1, q2, R)

should work (it doesn't at the moment, for some reason).
