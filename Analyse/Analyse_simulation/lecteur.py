# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 12:07:51 2026

@author: Azzaoui
"""

import uproot
import matplotlib.pyplot as plt
import numpy as np

def reader(file_name):
    
    Ncanals=3
    file = uproot.open(file_name)
    
    print(file.keys()) 
 
    tree = file["tree;1"]
    print(tree.keys())

    data_sim = [tree[f"Edep_{i}"].array(library="np") for i in range(1,Ncanals+1)]
    Time_sim = [tree[f"T_{i}"].array(library="np") for i in range(1,Ncanals+1)]
    #[data_sim.append(tree[f"Edep_{i}"].array(library="np")) for i in range(Ncanals)]

    data = tree.arrays(library="np")    
    mask = (data["Edep_1"] > 0) & (data["Edep_2"] > 0) &(data["Edep_3"] > 0) & (data["Z_1"] != 0) & (data["Z_2"] != 0) & (data["Z_3"] != 0)

    # filtre
    x1 = data["X_1"][mask]
    y1 = data["Y_1"][mask]
    z1 = data["Z_1"][mask]

    x3 = data["X_3"][mask]
    y3 = data["Y_3"][mask]
    z3 = data["Z_3"][mask]

    dx = x3 - x1
    dy = y3 - y1  
    dz = z3 - z1 

    norm = np.sqrt(dx**2 + dy**2 + dz**2)

    # --- Angle Zénithal (Theta) ---
    cos_theta = np.abs(dy) / norm 
    theta_rad = np.arccos(cos_theta)
    theta_deg = np.degrees(theta_rad)

    # --- Angle Azimutal (Phi) ---
    phi_rad = np.arctan2(dz, dx) 
    phi_deg = np.degrees(phi_rad)
    
    return  data_sim, Time_sim, phi_deg, phi_rad, theta_rad, theta_deg