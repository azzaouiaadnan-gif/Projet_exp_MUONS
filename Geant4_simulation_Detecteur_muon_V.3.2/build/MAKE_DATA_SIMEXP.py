#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 20:58:14 2026

@author: meikai
"""
import os
import sys
import shutil #bibi pour copy paste

def add():
    for i in range(10):
        
        fichier_source = os.path.join(f"job_angle_{i}0_deg", "Results.root")
        ang = i * 10
        fichier_dest = os.path.join("DATA_ROOT_EXP_SIM", f"Results_{ang}.root")
        shutil.copy(fichier_source, fichier_dest)
add()
        
    
        
    
    
    