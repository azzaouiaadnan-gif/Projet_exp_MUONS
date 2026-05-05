# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 15:31:09 2026

@author: Azzaoui
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
def Energy_Comparison(data_sim,Time_sim,file,TOL=[0,0,0]):
    Ncanals = 3
    data_sim_co, data_sim_co_0 = [] , []
    Time_sim_co, Time_sim_co_0 = [] , []
    
    print(len(data_sim[0]),len(data_sim[1]))
    coincidence = (data_sim[0] > TOL[0]) & (data_sim[1] > TOL[1]) & (data_sim[2] > TOL[2])
    coincidence_0 = (data_sim[0] > 0) & (data_sim[1] > 0) & (data_sim[2] > 0)
    
    for i in range (Ncanals):
        data_sim_co.append(data_sim[i][coincidence])
        Time_sim_co.append(Time_sim[i][coincidence])   
        data_sim_co_0.append(data_sim[i][coincidence_0])
        Time_sim_co_0.append(Time_sim[i][coincidence_0])
    
    fig , axes = plt.subplots(1, 2, figsize=(15, 6), sharey=True, sharex=True)
    
    
    sns.scatterplot(x=data_sim_co_0[0],y=data_sim_co_0[2] , marker=".", alpha=0.7, color='red', label='Geant4 Simulation without real tolerance',ax=axes[0] )
    
    axes[0].set_xlabel("Energy deposited in scintillator 1 (MeV)")
    axes[0].set_ylabel("Energy deposited in scintillator 3 (MeV)")
    axes[0].grid(True, linestyle='--', alpha=0.6)
    
    sns.scatterplot(x=data_sim_co[0],y=data_sim_co[2], marker= ".", alpha=0.7, color='blue', label='Geant4 Simulation  with real tolrance',ax = axes[1])

    axes[1].set_xlabel("Energy deposited in scintillator 1 (MeV)")
    axes[1].set_ylabel("Energy deposited in scintillator 3 (MeV)")
    axes[1].grid(True, linestyle='--', alpha=0.6)
   
    plt.xlim((0,40))
    plt.ylim((0,40 ))
   
    sous_titre = f"Applied Tolerance : Scint 1 > {TOL[0]:.2f} MeV | Scint 2 > {TOL[1]:.2f} MeV | Scint 3 > {TOL[2]:.2f} MeV"
    plt.suptitle(f"The impact of energy tolerance on Muons counts (ROOT Data)\n{sous_titre}" , fontsize = 15)
    plt.legend()
    save_path = os.path.join("PDF", f"E2vsE1_'{file}'.pdf" )

    plt.savefig(save_path,bbox_inches='tight')
    
    plt.show
    
    
    
    return  
