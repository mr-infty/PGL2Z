# -*- coding: utf-8 -*-
r"""
Chamber in the canonical hyperplane arrangement in the hyperbolic plane associated
to the extended modular group PGL(2,Z)
"""

from abc import abstractproperty
from sage.geometry.hyperbolic_space.hyperbolic_interface import HyperbolicPlane
from sage.geometry.hyperbolic_space.hyperbolic_geodesic import HyperbolicGeodesicUHP
from sage.rings.infinity import infinity
from sage.functions.generalized import sgn
from sage.all import I, QQ

def uhp_separated_by(point1, point2, gamma):
    x, y = map(lambda x: x.coordinates(), gamma.ideal_endpoints())
    if x == infinity:
        return sgn(point1.coordinates().real() - y) != sgn(point2.coordinates().real() - y)
    elif y == infinity:
        return sgn(point1.coordinates().real() - x) != sgn(point2.coordinates().real() - x)
    else:
        center = (x+y)/QQ(2)
        r_squared = ((y-x)/QQ(2))**2
        return sgn((point1.coordinates() - center).norm() - r_squared) != sgn((point2.coordinates() - center).norm() - r_squared)

def separated_by(point1, point2, gamma):
    r"""
    Returns True if point1 and point2 (points in the hyperbolic plane) lie on different sides
    with respect to the geodesic gamma, and False if point1 and point2 lie on the same side.

    Note: If either point lies on the geodesic itself, the behaviour is unspecified.
    """
    # TODO: Find more efficient implementation
    if isinstance(gamma, HyperbolicGeodesicUHP):
        return uhp_separated_by(point1, point2, gamma)
    else:
        return point1.dist(point2) > point1.dist(gamma.reflection_involution()(point2))

class Chamber(object):
    r"""
    Chamber in the canonical hyperplane arrangement in the hyperbolic plane associated
    to the extended modular group PGL(2,Z)
    """
    def separated_from(self, other, hyp):
        r"""
        Returns True iff hyp separates self from other.
        """
        return separated_by(self.interiorpoint, other.interiorpoint, hyp)

    @abstractproperty
    def interiorpoint(self):
        r"""
        Returns a point lying in the interior of the chamber.
        """

    @abstractproperty
    def walls(self):
        r"""
        Returns a tuple containing the walls bounding the chamber.
        """

    def __eq__(self, other):
        return all(not self.separated_from(other, hyp) for hyp in self.walls)

class SimpleMindedChamber(Chamber):
    r"""
    Chamber that is defined by manuallly giving all data.
    """
    def __init__(self, interiorpoint, walls):
        self._interiorpoint = interiorpoint
        self._walls = walls

    @property
    def interiorpoint(self):
        return self._interiorpoint

    @property
    def walls(self):
        return self._walls

def python_has_no_let_clauses():
    UHP = HyperbolicPlane().UHP()
    H1 = UHP.get_geodesic(-1, 1)
    H2 = UHP.get_geodesic(QQ(1)/QQ(2), infinity)
    H3 = UHP.get_geodesic(0, infinity)
    interiorpoint = UHP.get_point(QQ(1)/QQ(4) + I) # TODO: Canonical point?
    walls = (H1,H2,H3)
    return (interiorpoint, walls)

FundamentalChamber = (lambda (x, y): SimpleMindedChamber(x, y))(python_has_no_let_clauses())
