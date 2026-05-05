#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 18:15:00 2026

@author: Azzaoui
"""

import numpy as np

import numpy as np

def analyse_LHL(array_events, Ncanals, Sampling_time, ToF, sensibilite, MPV_list):
    conv = ToF / Sampling_time
    
    list_muons_LHL = []
    L_event_LHL = [[], [], []]
    
    s = abs(sensibilite)
    Nevents = array_events.shape[0] 
    
    for i in range(Nevents):
        data_set = array_events[i] 
        pic = []
        index = []
        
        for j in range(Ncanals):
            canal_data = np.abs(data_set[j])
            pic.append(np.max(canal_data))
            index.append(np.argmax(canal_data))
            
        if pic[0] > s and pic[1] > s and pic[2] > s:
            
            p_norm = [pic[0]/MPV_list[0], pic[1]/MPV_list[1], pic[2]/MPV_list[2]]
            
            is_LHL = (p_norm[0] < 0.6) and (p_norm[1] > 0.8) and (p_norm[2] < 0.6)
            
            diff_ToF = abs(index[0] - index[2])
            if diff_ToF < conv:
                if is_LHL:
                    list_muons_LHL.append(i)
                    L_event_LHL[0].append(pic[0])
                    L_event_LHL[1].append(pic[1])
                    L_event_LHL[2].append(pic[2])  
                    
    print(f"Nombre d'événements LHL : {len(list_muons_LHL)}")
    
    return L_event_LHL, list_muons_LHL
