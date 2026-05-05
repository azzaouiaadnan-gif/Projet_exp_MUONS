#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 19:48:27 2026

@author: Azzaoui
"""
import numpy as np
import os
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def Landau(AM_ch , E_mpv_list_simu, filename):
    def landau_pdf(x, amp, loc, scale):
        z = (x - loc) / scale
        return amp * np.exp(-0.5 * (z + np.exp(-z)))

    MPV_results = []
    K = []
    plt.figure(figsize=(15, 5))
    
    # On boucle sur les 3 canaux pour les fitter et les afficher
    for ch in range(3):
        data_fit = np.array(AM_ch[ch])
        data_fit = data_fit[data_fit > 0]

        counts, bins = np.histogram(data_fit, bins=80)
        bin_centers = (bins[:-1] + bins[1:]) / 2
        
        guess_amp = np.max(counts)
        guess_loc = bin_centers[np.argmax(counts)]
        guess_scale = np.std(data_fit) / 4 
        
        p0 = [guess_amp, guess_loc, guess_scale]
        
        try:
            popt, _ = curve_fit(landau_pdf, bin_centers, counts, p0=p0, bounds=([0, 0, 0], [np.inf, np.inf, np.inf]), maxfev=5000)
            mpv_exp = popt[1]
        except RuntimeError:
            print("trop de bruit, jete ca ")
            popt = p0 
            mpv_exp = guess_loc
            
        
        
        MPV_results.append(mpv_exp)
        
        K_mV_MeV = mpv_exp / E_mpv_list_simu[ch]
        K.append(K_mV_MeV)
        
        data_fit = data_fit*1000
        plt.subplot(1, 3, ch+1)
        plt.hist(data_fit, bins=80, alpha=0.6, color='blue', label='Data')
        x_fit = np.linspace(min(bin_centers), max(bin_centers), 200)
        plt.plot(x_fit*1000, landau_pdf(x_fit, *popt), 'r-', linewidth=2, label=f'Landau Fit MPV: {1000*mpv_exp:.3f} mV')
        
        plt.xlabel("Pulse Amplitude (mV)")
        plt.ylabel("Counts")
        plt.title(f"Canal {ch}")
        plt.legend()
        
        
        
    plt.tight_layout()
    name = filename.replace('.dat', '')
    
    save_path = os.path.join("Plot_pdf", f'Fit_landeau_3_canaux_MPV_{name}.pdf' )
    
    plt.savefig(save_path)
    plt.show()
    
    print("--- Constantes de calibration finales ")
    for ch in range(3):
        print(f"Canal {ch} : V_MPV = {MPV_results[ch]*1000:.3f} mV  |  E_MPV = {E_mpv_list_simu[ch]:.3f} MeV ===> K_{ch} = {K[ch]:.3f} mV/MeV ")
        
    
    save_path = os.path.join("Mpv_K", f'Constante_K_{name}.npy' )
    np.save(save_path,  K )
    
    save_path = os.path.join("Mpv_k", f'MPVs_EXP_{name}.npy' )
    np.save(save_path, MPV_results )
    
    
    return MPV_results , K
