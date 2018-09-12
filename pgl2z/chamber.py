# -*- coding: utf-8 -*-
r"""
Chamber in the canonical hyperplane arrangement in the hyperbolic plane associated
to the extended modular group PGL(2,Z)
"""

class Chamber(object):
    r"""
    Chamber in the canonical hyperplane arrangement in the hyperbolic plane associated
    to the extended modular group PGL(2,Z)
    """
    def __init__(self):
        pass
    
    def separated_from(self, other, hyp):
        r"""
        Returns True iff h separates self from other. 
        """
        return False

    def __eq__(self, other):
        return all(not self.separated_from(other, hyp) for hyp in self.walls())
