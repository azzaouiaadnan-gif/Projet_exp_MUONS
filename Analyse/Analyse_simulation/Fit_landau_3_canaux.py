# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 12:25:59 2026

@author: Azzaoui
"""

import numpy as np
from scipy.optimize import curve_fit
from scipy.stats import moyal
import matplotlib.pyplot as plt
import os
def fit_landau_3_channels(data_sim,file):
 
    coincidence = (data_sim[0] > 0) & (data_sim[1] > 0) & (data_sim[2] > 0) # On exige que le muon ait traversé les 3 plans (comme dans l'experimental)
    E_mpv_list = []
    
   
    plt.figure(figsize=(15, 5))
    
    
    
    def landau_pdf(x, amp, loc, scale):# Fonction de Landau (approximation de Moyal)
        return amp * moyal.pdf(x, loc, scale)
        
    for ch in range(3):
        data_fit = data_sim[ch][coincidence] #Filtrage des données pour le canal en cours
        
        data_fit = data_fit[(data_fit > 0.5) & (data_fit < 25)] # On coupe les queues extremes pour aider l'algorithme de fit
        
        counts, bins = np.histogram(data_fit, bins=80)
        bin_centers = (bins[:-1] + bins[1:]) / 2
        
        # Parametres de depart
        guess_amp = np.max(counts)
        guess_loc = bin_centers[np.argmax(counts)]
        guess_scale = 0.5
        
        p0 = [guess_amp, guess_loc, guess_scale]
        
        # Fit
        try:
            popt, _ = curve_fit(landau_pdf, bin_centers, counts, p0=p0)
            mpv_sim = popt[1]
        except:
            print(f"fit pour le canal {ch} echec")
            mpv_sim = guess_loc # Secu si le fit ne fonctionne pas
            popt = p0
            
        E_mpv_list.append(mpv_sim)
        
        # Trace du sous-graphique
        plt.subplot(1, 3, ch+1)
        plt.hist(data_fit, bins=80, alpha=0.6, color='red', label="Geant4 (MIPs)")
        
        x_axis = np.linspace(min(bin_centers), max(bin_centers), 200)
        plt.plot(x_axis, landau_pdf(x_axis, *popt), 'k-', lw=2, label=f"Fit MPV: {mpv_sim:.2f} MeV")
        plt.axvline(mpv_sim, color='blue', linestyle='--')
        
        plt.xlabel("Energy deposited (MeV)")
        if ch == 0:
            plt.ylabel("Counts")
            
        plt.title(f"Canal {ch}")
        plt.legend()
        
    plt.tight_layout()
    
    save_path = os.path.join("PDF", f"Fit_Landau_3voies_{file}.pdf" )

    plt.savefig(save_path,bbox_inches='tight')
    
    plt.show()
    
    # Print textuelle des resultats 
    print("\n" + "="*40)
    print("=== CONSTANTES DE CALIBRATION FINALES ===")
    print("="*40)
    for ch in range(3):
        print(f"Canal {ch} : Mpv_E_sim = {E_mpv_list[ch]:.2f} MeV")
        
    return E_mpv_list