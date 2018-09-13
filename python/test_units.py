#!/usr/bin/python
# -*- coding: utf-8 -*-
##########################################################################################
# author: Nikolas Schnellbaecher
# contact: khx0@posteo.net
# date: 2018-09-13
# file: test_units.py
##########################################################################################

import sys
import os
import numpy as np
import unittest

from units import MOLAR_TO_MICROMETER

class Units_test(unittest.TestCase):
    
    """
    Test cases for the units.py module.
    
    Units as in physical units and not in unit tests.
    """
        
    def test_Units_01(self):
                
        reference_gauge_value = 6.022140758e8
                    
        self.assertTrue(np.isclose(reference_gauge_value, MOLAR_TO_MICROMETER))
        
        # 2 Molar to 1 / (um)^3
        
        referenceValue = 2.0 * 6.022140758e8
        
        concentrationValue = 2.0 * MOLAR_TO_MICROMETER
        
        self.assertTrue(np.isclose(referenceValue, concentrationValue))
        
        return None

if __name__ == '__main__':
    
    unittest.main()

    
    
    
    
