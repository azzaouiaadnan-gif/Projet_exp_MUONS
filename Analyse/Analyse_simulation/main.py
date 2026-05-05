# -*-  oding: utf-8 -*-
"""
Created on Thu Apr  2 12:07:20 2026

@author: Azzaoui
"""
import tkinter as tk
from tkinter import filedialog
import sys
import os
import lecteur as le
import Analyse_simu as anal #hum hum cest un acronmyme pro ok rien de bizzare
import Fit_landau_3_canaux as Fit3
import Skymap as sk
import numpy as np
import Acceptance as ass # encore et toujours pro
import EnergievEnergie as EvE
import Run3_sim as r3

angle_detecteur = 0

print("======== Mode Unique ou Experimental ===========")
print("-Pour une analyse de Simulation Unique taper : 1 ")
print("-Pour une analyse de Simulation de L'experimental de taper : 2 ")
mode = int(input("Mode :  "))

if mode == 1 : 
    print("-------Simulation Unique ----")
    
    root = tk.Tk()
    root.withdraw()
    root.attributes("-topmost", True)# Pour windows, microsoft is suck
    root.lift()


    file_path = filedialog.askopenfilename(
        title="Sélectionnez le fichier de données",
        filetypes=[("Fichiers ROOT", "*.root"), ("Tous les fichiers", "*.*")])
    if not file_path:
        sys.exit()

    file_name = os.path.basename(file_path)


    print(f"Fichier sélectionne : {file_name}")


    print("Extraction des data...")
    data_sim, Time_sim, phi_deg, phi_rad, theta_rad, theta_deg = le.reader(file_name)

    print("Analyse en cours....")
    #N_muons, data_sim_co ,Time_sim_co ,ToFm ,Em = anal.analyse_simulation(data_sim, Time_sim, file_name)

    print("Fit de landau en cours.....")
    #E_mpv_list = Fit3.fit_landau_3_channels(data_sim,file_name)
    #np.save(f"energies_mpv_{file_name}.npy", E_mpv_list)

    print("Skymap en cours...")
    sk.Skymap(phi_deg, theta_deg,file_name, angle_detecteur)
    print("--- Skymap genere ---")

    print("Calcul de l'acceptance Resolution en cours...")
    #ass.Acceptance_Resolution(theta_deg,angle_detecteur,file_name)
    print("--- Acceptance en Resolution genere ---")

    print("Energy Comparison en cours....")
    Coef_path = os.path.join("DATA_for_SIM", "Constante_K_Mesure_0_degres_de_reference.npy" )
    Coef_K_ref = np.load(Coef_path).tolist()
    tolerance_ref = []
    for i in range(len(Coef_K_ref)):
        tolerance_ref.append(0.04/Coef_K_ref[i])
    #EvE.Energy_Comparison(data_sim,Time_sim,file_name,tolerance_ref , angle_detecteur)

    
if mode == 2 :
    
    print("-------Simulation de L'experimental ----")


    Coef_path = os.path.join("DATA_for_SIM", "Constante_K_Run_0_deg_Data_3_20_2026_Ascii+.npy" )
    Coef_K = np.load(Coef_path).tolist()
    tolerance = []

    for i in range(len(Coef_K)):
        tolerance.append(0.04/Coef_K[i])
    List_Muons_seconde ,List_Muons , List_Time = r3.SIM_EXP(tolerance)
    path_Muon_seconde = os.path.join("DATA_for_SIM", "List_Muons_seconde_Sim.npy" )
    path_Muon = os.path.join("DATA_for_SIM", "List_Muons_Sim.npy" )
    path_Time = os.path.join("DATA_for_SIM", "List_Time_Sim.npy" )
    np.save(path_Muon_seconde, List_Muons_seconde)
    np.save(path_Muon, List_Muons)
    np.save(path_Time, List_Time)











