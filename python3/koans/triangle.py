#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.

# Triangle analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#
def triangle(a, b, c):
    sides = [a,b,c]
    tri_set = set(sides)

    if any(n <= 0 for n in tri_set):
        raise TriangleError(AttributeError('Looking for actual triangles, kids'))
    elif a + b + c <= 2 * max(a, b, c):
        raise TriangleError(AttributeError('There is no triangle, or Arizona'))
    elif len(tri_set) == 1:
        return 'equilateral'
    elif len(tri_set) == 2:
        return 'isosceles'
    elif len(tri_set) == 3:
        return 'scalene'

# Error class used in part 2.  No need to change this code.
class TriangleError(Exception):
    pass
