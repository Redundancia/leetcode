# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 07:52:47 2020

@author: Tuli
"""

name = "vtkgn"
typed = "vttkgnn"

counter = 0
for c in typed:
    print(c)
    if c != name[counter]:
        counter -= 1
        if c != name[counter]:
            print("False")
            break
    counter += 1
    
#comebacklater

            
        