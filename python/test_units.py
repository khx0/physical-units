#!/usr/bin/python
# -*- coding: utf-8 -*-
##########################################################################################
# author: Nikolas Schnellbaecher
# contact: khx0@posteo.net
# date: 2018-09-13
# file: test_units.py
# tested with python 2.7.15
# tested with python 3.7.0
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
        
    def test_Units_02(self):
        
        # 3D -> 2D affinity conversion factor
        conv_3D_to_2D_affinity = 1.2e-3 # in um
        
        # 3D equilibrium affinity
        KDB = 0.1e-9 # in Molar (M)
        
        KDX = conv_3D_to_2D_affinity * KDB * MOLAR_TO_MICROMETER
        
        KDX_reference = 0.722656891e-4 # in 1/ (um)^2
                        
        self.assertTrue(np.isclose(KDX, KDX_reference))
        
        return None

    def test_Units_03(self):
        
        # 3D -> 2D affinity conversion factor
        conv_3D_to_2D_affinity = 1.2e-3 # in um
        
        # 3D equilibrium affinity
        KDB = 100e-9 # in Molar (M)
        
        KDX = conv_3D_to_2D_affinity * KDB * MOLAR_TO_MICROMETER
        
        KDX_reference = 0.0722656891 # in 1/ (um)^2
                        
        self.assertTrue(np.isclose(KDX, KDX_reference))
        
        return None

    def test_Units_04(self):
        
        # 3D -> 2D affinity conversion factor
        conv_3D_to_2D_affinity = 1.2e-3 # in um
        
        # 3D equilibrium affinity
        KDB = 1.0e-6 # in Molar (M)
        
        KDX = conv_3D_to_2D_affinity * KDB * MOLAR_TO_MICROMETER
        
        KDX_reference = 0.722656891 # in 1/ (um)^2
                        
        self.assertTrue(np.isclose(KDX, KDX_reference))
        
        return None

if __name__ == '__main__':
    
    unittest.main()

    
    
    
    
