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
    sage: from pgl2z.pgl2z import PGL2Z
    sage: W = PGL2Z()
    sage: s1, s2, s3 = W.gens()
    sage: s1.descents()
    sage: from pgl2z.chamber import FundamentalChamber as C0
    sage: C0.separated_from(s1*C0, C0.walls[0])
    sage: H = IwahoriHeckeAlgebra(W, 0, 0, ZZ)
    sage: T = H.T()
    sage: T1, T2, T3 = T.algebra_generators()
