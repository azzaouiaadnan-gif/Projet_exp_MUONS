#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 19:45:42 2026

@author: Azzaoui
"""

import numpy as np

def analyse(array_events, Ncanals, Sampling_time, ToF, tolerance ,Total_time):
    conv = ToF / Sampling_time
    list_muons = []
    AM_ch = [[], [], []] 
    list_amp = []
    t = abs(tolerance)
    liste_dT_haut_bas = [] 
    Nevents = array_events.shape[0] 
    
    for i in range(Nevents):
        data_set = array_events[i] 
        pic = []
        amp = []
        index = []
        
        for j in range(Ncanals):
            
            canal_data = np.abs(data_set[j])
            amp.append(data_set[j])
            pic.append(np.max(canal_data))
            index.append(np.argmax(canal_data))
            
        if pic[0] > t and pic[1] > t and pic[2] > t : 
            diff_ToF = abs(index[0] - index[2])
            
            if diff_ToF < conv:
                
                list_muons.append(i)
                
                AM_ch[0].append(pic[0])
                AM_ch[1].append(pic[1])
                AM_ch[2].append(pic[2])
                
                list_amp.append(amp)
                
                
                temps_ns = (index[0] - index[2]) * Sampling_time
                liste_dT_haut_bas.append(temps_ns)
                
                
    print(f"-Nombre d'événements validés (coïncidence des 3 canaux) : {len(list_muons)}")
    print(f"-Muons validé par seconde : {len(list_muons)/Total_time}")
    return AM_ch, list_muons ,liste_dT_haut_bas , np.array(list_amp) 
