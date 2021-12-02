# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 03:02:30 2020

@author: Tuli
"""

def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        pair = []
        for i in range(len(nums)):
            try:
                pair.append(i)
                pair.append(nums.index(target - nums[i]))
                if pair[0] == pair[1]:
                    pair = []
                    continue
                return pair
            except:
                pair = []
                    

nums = [-3,4,3,90]
target = 0

print(twoSum(nums,target))