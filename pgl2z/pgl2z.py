# -*- coding: utf-8 -*-
r"""
The extended modular group PGL(2,Z)
"""

from sage.structure.parent import Parent
from sage.structure.unique_representation import UniqueRepresentation
from sage.groups.matrix_gps.finitely_generated import FinitelyGeneratedMatrixGroup_generic
from sage.categories.coxeter_groups import CoxeterGroups
from sage.combinat.root_system.coxeter_matrix import CoxeterMatrix
from sage.rings.all import ZZ
from pgl2z.element import PGL2Z_Element

class PGL2Z(FinitelyGeneratedMatrixGroup_generic):
#class PGL2Z(UniqueRepresentation, FinitelyGeneratedMatrixGroup_generic):
    Element = PGL2Z_Element
    r"""
    An implementation of the extended modular group, i.e.
    the group of projective invertible 2x2 integer matrices,
    as a (hyperbolic) Coxeter group.
    """
    def __init__(self):
        r"""
        Constructs the extended modular group.

        EXAMPLES::

            sage: from pgl2z import PGL2Z
            sage: PGL2Z()
            The extended modular group

        """
        self._matrix = CoxeterMatrix([[1, 3, 2]
                                     ,[3, 1,-1]
                                     ,[2,-1, 1]])
        FinitelyGeneratedMatrixGroup_generic.__init__(self, ZZ(2), ZZ, [matrix([[0, 1], [1, 0]])
                                                                       ,matrix([[-1, 1], [0, 1]])
                                                                       ,matrix([[-1, 0], [0, 1]])]
                                                                     , category=CoxeterGroups())
        self._s1, self._s2, self._s3 = self.gens()

    def index_set(self):
        return (1,2,3)

    def has_left_descent(self, i):
        return NotImplemented #TODO: Implement this

    def simple_reflection(self, i):
        if i == 1:
            return self._s1
        elif i == 2:
            return self._s2
        elif i == 3:
            return self._s3
        else:
            raise ValueError("%s is not a valid index" % str(i))

    def is_finite(self):
        return False

    def __repr__(self):
        return "The extended modular group PGL(2,Z)"

    def __contains__(self, x):
        r"""
        Check if the element x in in the mathematical parent self.
        """
        from sage.structure.all import parent
        return parent(x) is self

    def coxeter_matrix(self):
        return self._matrix

    #@cached_method
    #def one(self):
    #    r"""
    #    Implements :meth:`Monoids.ParentMethods.one`.
    #
    #    EXAMPLES::
    #
    #        sage: W = PGL2Z()
    #        sage: W.one()
    #        [ 1 , 0 ]
    #        [ 0 , 1 ]
    #    """
    #    return 
