# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 07:34:52 2020

@author: Tuli
"""

heights = [1,1,4,2,1,3]
moves_2 =sum([1 for i in range(len(heights)) if heights[i] != sorted(heights)[i]])
print(moves_2)