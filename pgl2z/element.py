# -*- coding: utf-8 -*-
r"""
Elements of the extended modular group PGL(2,Z)
"""

import itertools
from sage.groups.matrix_gps.group_element import MatrixGroupElement_generic

class PGL2Z_Element(MatrixGroupElement_generic):
    r"""
    Element of the extended modular group PGL(2,Z)
    """
    def __eq__(self, other):
        return type(self) is type(other) \
                and (all(self.matrix()[i,j] == other.matrix()[i,j] for (i,j) in itertools.product((0,1),(0,1))) \
                     or all(self.matrix()[i,j] == -other.matrix()[i,j] for (i,j) in itertools.product((0,1),(0,1))))
