#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 06:38:11 2026

@author: Azzaoui
"""

import matplotlib.pyplot as plt
import seaborn as sns
import os
import numpy as np
from scipy.optimize import curve_fit

def plot_tof(liste_dT, filename):
    plt.figure(figsize=(8, 5))
    
    # on trace l'histo des temps
    sns.histplot(liste_dT, bins=50, alpha=0.7, color='orange', edgecolor='black')
    
    plt.title("Time of Flight (ToF) Distribution between Top and Bottom")
    plt.xlabel(r"$\Delta T$ (ns)")
    plt.ylabel("Number of Events")
    plt.axvline(0, color='red', linestyle='--', alpha=0.7, label='Perfect Coincidence (0 ns)')
    plt.legend()
    
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    
    name = filename.replace('.dat', '')
    save_path = os.path.join("Plot_pdf",f'Distribution_ToF_{name}.pdf' )
    
    plt.savefig(save_path)
    plt.show()

def plot_event(filename,AM_ch, Ncanals, Time_Sampling, A):
    Event = AM_ch[A]
    plt.figure(figsize=(8, 5))
    
    for i in range(Ncanals):
        sns.lineplot( x = Time_Sampling ,y = Event[i]  )
        
    plt.title(f"Waveform of Event Number {A}", fontsize=16)
    plt.xlabel("Time $T$ (ns)", fontsize=14)
    plt.ylabel("Amplitude (V)", fontsize=14)
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    
    name = filename.replace('.dat', '')
    
    save_path = os.path.join("Plot_pdf",f'Distribution_ToF_{name}.pdf' )
    
    plt.savefig(save_path)
    plt.show()



def Graph_Dist_total(List_Muons_seconde_fenetre, List_Muons_Total_fenetre, 
                     List_Muons_seconde_batiment, List_Muons_Total_batiment,
                     List_Muons_seconde_simulation, List_Muons_Total_simulation):
    
    angles_deg = np.linspace(0, 90, 10)
    angles_rad = np.radians(angles_deg) 
    
    # 1. Error calculation (Poisson Statistics)
    def calculate_error(list_sec, list_tot):
        list_sec = np.array(list_sec)
        list_tot = np.array(list_tot)
        # Avoid division by zero
        time = np.where(list_sec > 0, list_tot / list_sec, 1)
        return np.sqrt(list_tot) / time

    err_win = calculate_error(List_Muons_seconde_fenetre, List_Muons_Total_fenetre)
    err_bui = calculate_error(List_Muons_seconde_batiment, List_Muons_Total_batiment)
    err_sim = calculate_error(List_Muons_seconde_simulation, List_Muons_Total_simulation)

    # 2. Theoretical Model (Cosine Law)
    def cos2(theta, I0, n):
        return I0 * (np.cos(theta)**n)

    # Fits 
    popt_win, _ = curve_fit(cos2, angles_rad, List_Muons_seconde_fenetre, p0=[max(List_Muons_seconde_fenetre), 2])
    popt_bui, _ = curve_fit(cos2, angles_rad, List_Muons_seconde_batiment, p0=[max(List_Muons_seconde_batiment), 2])
    popt_sim, _ = curve_fit(cos2, angles_rad, List_Muons_seconde_simulation, p0=[max(List_Muons_seconde_simulation), 2])

    # plot sns
    sns.set_theme(style="whitegrid")
    plt.figure(figsize=(11, 7))
    
    # Barre erreurs merci pyplot 
    plt.errorbar(angles_deg, List_Muons_seconde_fenetre, yerr=err_win, fmt='o', color="red", 
                 ecolor='darkorange', elinewidth=1, capsize=3, label="Window Side (Data ± $\sqrt{N}$)")
    
    plt.errorbar(angles_deg, List_Muons_seconde_batiment, yerr=err_bui, fmt='s', color="green", 
                 ecolor='green', elinewidth=1, capsize=3, label="Building Side (Data ± $\sqrt{N}$)")
                 
    plt.errorbar(angles_deg, List_Muons_seconde_simulation, yerr=err_sim, fmt='D', color="black", 
                 ecolor='black', elinewidth=1.5, capsize=3, label="Geant4 Simulation (± $\sqrt{N}$)")

    # Fit 
    x_fit = np.linspace(0, np.pi/2, 100)
    plt.plot(np.degrees(x_fit), cos2(x_fit, *popt_win), color="red", linestyle="--", alpha=1, 
             label=fr"Fit Window Side ($n={popt_win[1]:.2f}$ )  Law Fit = $\cos^n(\theta)$ ")
             
    plt.plot(np.degrees(x_fit), cos2(x_fit, *popt_bui), color="green", linestyle="--", alpha=1, 
             label=f"Fit Building Side ($n={popt_bui[1]:.2f}$)")
             
    plt.plot(np.degrees(x_fit), cos2(x_fit, *popt_sim), color="black", linestyle=":", alpha=1, 
             label=f"Fit Simulation Geant4 with Tolerance ($n={popt_sim[1]:.2f}$)")
   
    plt.title("Angular Distribution of Muon Flux", fontsize=15)
    plt.xlabel("Zenith Angle $\\theta$ (degrees)", fontsize=12)
    plt.ylabel("Flux (muons / s)", fontsize=12)
    plt.xlim(-5, 95)
    max_flux = max(max(List_Muons_seconde_fenetre), max(List_Muons_seconde_batiment), max(List_Muons_seconde_simulation))
    plt.ylim(0, max_flux * 1.2)
    
    plt.legend(frameon=True)
    
    # Console output
    print("--- Fit Results ---")
    print(f"Window Side   : I0 = {popt_win[0]:.3f} s⁻¹, n = {popt_win[1]:.2f}")
    print(f"Building Side : I0 = {popt_bui[0]:.3f} s⁻¹, n = {popt_bui[1]:.2f}")
    print(f"Simulation    : I0 = {popt_sim[0]:.3f} s⁻¹, n = {popt_sim[1]:.2f}")
    path_dist = os.path.join("Plot_pdf", "Angular_Distribution_of_Muon_Flux.pdf" )
    plt.savefig(path_dist)
    plt.show()
    
    