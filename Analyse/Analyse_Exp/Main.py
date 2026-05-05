#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 20:16:02 2026

@author: Azzaoui
"""

import tkinter as tk
from tkinter import filedialog
import sys
import os
import numpy as np
import Convert_data as conv
import Analyse_exp as ana1
import Analyse_exp_V2 as ana2
import Analyse_3_canaux_exp as ana3
import Plot as pl
import Fit_landau as plot
import Run3 as r3
# ===============================================================
#              Ouverture des MPVs de simulation
# ===============================================================

path = os.path.join("Mpv_K" ,'Energies_mpv_320_Millions.npy' )
E_mpv_list_simu = np.load(path).tolist()

# =============================================================
#                     Parametres Globaux
# =============================================================
Tolerance = 0.040 # en V
ToF = 10          # en ns

print("======== Mode Unique ou Global ===========")
print("-Pour une analyse Unique taper : 1 ")
print("-Pour une analyse Globale taper : 2 ")
mode = int(input("Mode :  "))

"=============================================================================="
"========================== Analyse Unique ===================================="
"=============================================================================="

if mode == 1 : 
    
    # ===============================================================
    #                  Selection du fichier 
    # ===============================================================
    
    root = tk.Tk()
    root.withdraw()
    root.attributes("-topmost", True)  
    root.lift()
    print("Ouverture de la fenêtre de sélection...")
    file_path = filedialog.askopenfilename(
        title="Sélectionnez le fichier de données",
        filetypes=[("Fichiers DAT", "*.dat"), ("Tous les fichiers", "*.*")])
    if not file_path:
        sys.exit()

    file_name = os.path.basename(file_path)
    print(f"Fichier sélectionné : {file_name}")

    # =============================================================
    #                       Analyse
    # =============================================================

    print("--- Extraction des données ---")
    array_events, Ncanals, Time_step, Sampling_time, Time_sampling ,Total_time = conv.convert_data(file_path)

    print(f"Temps de mesure de {Total_time:.1f} s ")

    print("--- Analyse et Coïncidences ---")
    AM_ch, list_muons, liste_dT , list_amp = ana3.analyse(array_events, Ncanals, Sampling_time, ToF, Tolerance,Total_time)

    print("--- Fit de Landau , Graphiques et  Coef K ---")
    MPVs_exp , K = plot.Landau(AM_ch, E_mpv_list_simu, file_name)

    print("--- Nombre d'événements LHL ---")
    #ana2.analyse_LHL(array_events, Ncanals, Sampling_time, ToF, Tolerance,MPVs)
    pl.plot_tof(liste_dT, file_name)

    A = 3
    print(f"--- Representation du Event numero {A} ---")
    pl.plot_event(file_name, list_amp , Ncanals, Time_sampling , A)



"=============================================================================="
"========================== Analyse Global ===================================="
"=============================================================================="



if mode == 2 : 
    # ===============================================================
    #                          Extraction 
    # ===============================================================
    
    
    List_Muons_seconde_fenetre ,List_Muons_Total_fenetre , Time_fenetre = r3.extract_FEN(Tolerance , ToF)
    
    List_Muons_seconde_batiment ,List_Muons_Total_batiment , Time_Batiment = r3.extract_BAT(Tolerance ,ToF)
    
    path_Muon_seconde = os.path.join("DATA_for_SIM", "List_Muons_seconde_Sim.npy" )
    path_Muon = os.path.join("DATA_for_SIM", "List_Muons_Sim.npy" )
    path_Time = os.path.join("DATA_for_SIM", "List_Time_Sim.npy" )
    List_Muons_seconde_simulation = np.load(path_Muon_seconde).tolist()
    List_Muons_simulation  = np.load(path_Muon).tolist()
    List_Time_simulation = np.load(path_Time).tolist()
    
    pl.Graph_Dist_total(List_Muons_seconde_fenetre ,List_Muons_Total_fenetre, List_Muons_seconde_batiment , List_Muons_Total_batiment
                     ,List_Muons_seconde_simulation, List_Muons_simulation )
    
    save_path_FEN = os.path.join("DATA_for_SIM", "Time_FEN.npy" )
    save_path_BAT = os.path.join("DATA_for_SIM", "Time_BAT.npy" )
    
    np.save(save_path_FEN, Time_fenetre)
    np.save(save_path_BAT, Time_Batiment)
    
    
    
    
    
    
    
            
    


    

        


























































