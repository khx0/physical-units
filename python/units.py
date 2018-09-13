#!/usr/bin/python
# -*- coding: utf-8 -*-
##########################################################################################
# author: Nikolas Schnellbaecher
# contact: khx0@posteo.net
# date: 2018-09-13
# file: units.py
##########################################################################################

import time
import datetime
import sys
import os
import math
import numpy as np

"""
As of CODATA Recommended Values of the Fundamental Physical Constants: 2014
https://arxiv.org/abs/1507.07956

Also compare the new proposed SI Standard definition for 2019.

Also mentioned in Physik Konkret Nr.34 of the DPG - released in September 2018
"""
AVOGRADRO_CONSTANT = 6.022140758e23 # per mol (i.e. mol^(-1))

AVOGADRO_CONSTANT_VALUE = 6.022140758

"""
MOLAR_TO_MICROMETER converts quantities in Molar (M) to 
1 / (um)^3. This means
1 M = 6.022140758 x 10^(8) x (um)^(-3)
The resulting quantity is still a concentration, but expressed in units of
1 / (um)^3.
"""
MOLAR_TO_MICROMETER = AVOGADRO_CONSTANT_VALUE * 1.0e8

if __name__ == '__main__':

    pass
    
    



