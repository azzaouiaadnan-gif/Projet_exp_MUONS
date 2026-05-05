# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 21:26:07 2026

@author: Azzaoui
"""


import sys
import os
import lecteur as le
import Analyse_simu as anal #hum hum cest un acronmyme pro ok rien de bizzare
import Skymap as sk
import numpy as np

def SIM_EXP(TOL):
    
    Time_path = os.path.join("DATA_for_SIM", "Time.npy" )
    Time = np.load(Time_path).tolist()
    
    dossier = os.path.join("DATA_ROOT_EXP_SIM")

    List_Muons_seconde = []
    List_Muons = []
    List_Time = []
    i = 0
    
    for i in range(10):
        angle = i * 10
        f = f"Results_{angle}.root"
        path = os.path.join(dossier, f)
        # On vérifie que le fichier existe bien avant de l'ouvrir
        if os.path.exists(path):
            print("==========================================")
            print(f"Ouverture de : {f} (Angle = {angle}°)")
            
            data_sim, Time_sim, phi_deg, phi_rad, theta_rad, theta_deg = le.reader(path)
            
            N_muons, data_sim_co, Time_sim_co, ToFm, Em = anal.analyse_simulation(data_sim, Time_sim, f, TOL)
            List_Muons_seconde.append(N_muons/Time[i])
            print(f"-Muons enregistre par seconde : {List_Muons_seconde[i]}")
            List_Muons.append(N_muons)
            List_Time.append(Time[i])
    
    
    return List_Muons_seconde ,List_Muons , List_Time
