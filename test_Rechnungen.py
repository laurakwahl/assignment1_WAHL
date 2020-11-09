# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 16:51:26 2020

@author: Laura
"""

from Rechnung import smallest_common_denominator, biggest_common_denominator, add_frac

def test_smallest_common_counter():
    assert smallest_common_counter(1,2) == 2
    
def test_biggest_common_denominator():
    assert biggest_common_denominator(1,2) == 1

def test_add_frac ():
    assert add_frac(1,2,3,4) == [5,4]
