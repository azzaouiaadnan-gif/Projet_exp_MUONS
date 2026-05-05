# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 12:31:39 2026

@author: Azzaoui
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

def analyse_simulation(data_sim,Time_sim,file,TOL=[0,0,0]):
    Ncanals = 3
    data_sim_co = [] 
    Time_sim_co  = [] 
    
    print(len(data_sim[0]),len(data_sim[1]))
    coincidence = (data_sim[0] > TOL[0]) & (data_sim[1] > TOL[1]) & (data_sim[2] > TOL[2])
    
    for i in range (Ncanals):
        data_sim_co.append(data_sim[i][coincidence])
        Time_sim_co.append(Time_sim[i][coincidence])   
    ToF_sim = Time_sim_co[2] - Time_sim_co[0]
    
    print(f"Temps de vol moyen et maximal d'un Muon : {np.mean(ToF_sim):.2f} ns  |  {np.max(ToF_sim):.2f} ns")
    print(f"Nombre d'événements enrefistrée data_2 : {len(data_sim_co[1])}")
    print(f"Énergie moyenne data_2 : {np.mean(data_sim_co[1]):.3f} MeV")
    
    sns.set_theme(style="whitegrid")
    plt.figure(figsize=(10,6))
    
    sns.histplot(data_sim_co[1], bins=100,alpha = 0.7, color='red', label='Geant4 Simulation')
    plt.xlabel("Energy (MeV)")
    plt.ylabel("Counts")
    plt.title("Energy spectre for the Second Scint (ROOT Data)")
    plt.xlim((0,30))
    plt.legend()
    save_path = os.path.join("PDF", f"Analyse_du_fichier_'{file}'.pdf")

    plt.savefig(save_path,bbox_inches='tight')
    plt.show()
    ToFm = np.mean(ToF_sim)
    N_muons = len(data_sim_co[1])
    Em =  np.mean(data_sim_co[1])
    
    
    return  N_muons, data_sim_co ,Time_sim_co ,ToFm ,Em















































    