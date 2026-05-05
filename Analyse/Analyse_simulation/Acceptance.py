# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 14:18:56 2026

@author: Azzaoui
"""

import matplotlib.pyplot as plt
import numpy as np
import os

def Acceptance_Resolution(theta_deg,angle_detecteur,file):
    #============ RESOLUTION ===========
    plt.figure(figsize=(10, 6))
    
    n, bins, patches = plt.hist(theta_deg, bins=100, range=(0, 90), 
                                color='royalblue', alpha=0.7, edgecolor='black', label='Geant4 simulation')
    
    mean_theta = np.mean(theta_deg)
    std_theta = np.std(theta_deg) #Resolution
    textstr = '\n'.join((
        r'$\mu=%.2f^\circ$' % (mean_theta, ),
        r'$\sigma=%.2f^\circ$' % (std_theta, ),
        r'$N_{muons}=%d$' % (len(theta_deg), )))

    props = dict(boxstyle='round', facecolor='white', alpha=0.5)
    plt.gca().text(0.75, 0.95, textstr, transform=plt.gca().transAxes, fontsize=12,
            verticalalignment='top', bbox=props)

    plt.xlabel("Zenithal Angle (deg)", fontsize=12)
    plt.ylabel("Counts / deg", fontsize=12)
    sub_title = f"Detector angle = {angle_detecteur}°"
    plt.title(f"Angular Distribution \n {sub_title}", fontsize=14, fontweight='bold')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.5)
    save_path = os.path.join("PDF", f"Resolution_Angulaire_{file}.pdf")

    plt.savefig(save_path,bbox_inches='tight')
    
    
    plt.show()
    return 