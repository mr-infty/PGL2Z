# -*- coding: utf-8 -*-
r"""
Elements of the extended modular group PGL(2,Z)
"""

import itertools
from sage.groups.matrix_gps.group_element import MatrixGroupElement_generic
from sage.geometry.hyperbolic_space.hyperbolic_geodesic import HyperbolicGeodesic, HyperbolicGeodesicUHP 
from sage.geometry.hyperbolic_space.hyperbolic_point import HyperbolicPoint, HyperbolicPointUHP
from sage.geometry.hyperbolic_space.hyperbolic_model import HyperbolicModelUHP
from sage.geometry.hyperbolic_space.hyperbolic_interface import HyperbolicPlane
from sage.functions.other import conjugate
from sage.rings.infinity import infinity

UHP = HyperbolicPlane().UHP()

class PGL2Z_Element(MatrixGroupElement_generic):
    r"""
    Element of the extended modular group PGL(2,Z)
    """
    def __eq__(self, other):
        return type(self) is type(other) \
                and (all(self.matrix()[i,j] == other.matrix()[i,j] for (i,j) in itertools.product((0,1),(0,1))) \
                     or all(self.matrix()[i,j] == -other.matrix()[i,j] for (i,j) in itertools.product((0,1),(0,1))))

    def __getitem__(self, index):
        if index == 'a':
            return self.matrix()[0,0]
        elif index == 'b':
            return self.matrix()[0,1]
        elif index == 'c':
            return self.matrix()[1,0]
        elif index == 'd':
            return self.matrix()[1,1]
        else:
            raise KeyError(str(index))

    def __mul__(self, other):
        if isinstance(other, HyperbolicGeodesic):
            return HyperbolicGeodesic(other.model(), self * other.start(), self * other.end()) 
        elif isinstance(other, HyperbolicPointUHP):
            z = other.coordinates()
            if z is infinity:
                a = self['b']
                b = self['a']
                c = self['d']
                d = self['c']
                z = 0
            else:
                a = self['a']
                b = self['b']
                c = self['c']
                d = self['d']
            if self.matrix().det() == 1:
                num = a*z + b
                div = c*z + d
            else: # det == -1
                num = a*conjugate(z) + b
                div = c*conjugate(z) + d
            z = infinity if div.is_zero() else num/div
            return UHP.get_point(z)
        else: # TODO: Implement action for other models
            return NotImplemented
