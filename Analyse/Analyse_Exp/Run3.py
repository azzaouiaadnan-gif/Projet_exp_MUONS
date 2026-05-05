# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 16:01:32 2026

@author: Azzaoui
"""
import os
import sys
import Analyse_3_canaux_exp as anal
import Convert_data as conv

def extract_FEN (Tolerance , ToF):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    dossier = os.path.join(BASE_DIR, "DATA", "DATA_EXP_jour3", "FEN")

    files = os.listdir(dossier)
    List_Muons_seconde = []
    List_Muons = []
    Time = []
    for f in files:
        if f.endswith(".dat"):
            path_to_open = os.path.join(dossier, f)
            print("==========================================")
            print(f"Ouverture de : {f}")
            
            array_events, Ncanals, Time_step, Sampling_time, Time_sampling, Total_time = conv.convert_data(path_to_open)
            AM_ch, list_muons, liste_dT, list_amp = anal.analyse(array_events, Ncanals, Sampling_time, ToF, Tolerance, Total_time)
            List_Muons_seconde.append(len(list_muons)/Total_time)
            List_Muons.append(len(list_muons))
            Time.append(Total_time)
            #pl.plot_tof(liste_dT, f)
    
    return List_Muons_seconde ,List_Muons , Time

def extract_BAT (Tolerance , ToF):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    dossier = os.path.join(BASE_DIR, "DATA", "DATA_EXP_jour3", "BAT")

    files = os.listdir(dossier)
    List_Muons_seconde = []
    List_Muons = []
    Time = []
    for f in files:
        if f.endswith(".dat"):
            path_to_open = os.path.join(dossier, f)
            print("==========================================")
            print(f"Ouverture de : {f}")
            
            array_events, Ncanals, Time_step, Sampling_time, Time_sampling, Total_time = conv.convert_data(path_to_open)
            AM_ch, list_muons, liste_dT, list_amp = anal.analyse(array_events, Ncanals, Sampling_time, ToF, Tolerance, Total_time)
            List_Muons_seconde.append(len(list_muons)/Total_time)
            List_Muons.append(len(list_muons))
            Time.append(Total_time)
            #pl.plot_tof(liste_dT, f)
    
    return List_Muons_seconde , List_Muons  , Time

    