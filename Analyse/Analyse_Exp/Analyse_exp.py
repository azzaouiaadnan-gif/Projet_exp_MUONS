#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 19:37:32 2026

@author: Azzaoui
"""

import numpy as np

def analyse(array_events, Ncanals, Sampling_time, ToF, sensibilite):
    conv = ToF/Sampling_time
    list_muons = []
    AM = []
    s = abs(sensibilite)
    Nevents = array_events.shape[0] 
    for i in range (Nevents):
        data_set = array_events[i]
        pic = []
        index = []
        for j in range(Ncanals):
            canal_data = np.abs(data_set[j])
            pic.append(np.max(canal_data))
            index.append(np.argmax(canal_data))
        if pic[0] > s and pic[1] > s and pic[2] > s: 
            index = []
            for l in range(Ncanals):
                index.append(np.argmax(abs(np.array(data_set[l]))))
            diff_ToF = abs(index[0] - index[2])
            
            if diff_ToF < conv :
                list_muons.append(i)
                AM.append((pic[0] + pic[1] + pic[2])/Ncanals)
    print(f"Nombre d'événements validés (muons) : {len(list_muons)}")
    return AM






