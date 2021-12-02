# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 03:56:43 2020

@author: Tuli
"""




class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        xBinary = ('{:032b}'.format(x))
        yBinary = ('{:032b}'.format(y))
        
        summBinaryDiff = 0
        for i in range(32):
            if xBinary[i] != yBinary[i]:
                summBinaryDiff += 1
        return summBinaryDiff