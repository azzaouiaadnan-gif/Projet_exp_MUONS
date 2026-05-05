# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 17:17:59 2026

@author: Azzaoui
"""
import numpy as np
import os

def convert_time_Nmuon(Time):
    return (Time/60) * 40000
def Main():
    path_BAT = os.path.join("DATA_for_SIM" ,'Time_BAT.npy' )
    path_FEN = os.path.join("DATA_for_SIM" ,'Time_FEN.npy' )
    path_TIME = os.path.join("DATA_for_SIM" ,'Time.npy' )
    Time_BAT = np.load(path_BAT).tolist()
    Time_FEN = np.load(path_FEN).tolist()
    Time , Real_Time = [] , []
    for i in range(len(Time_BAT)):
        Time.append((Time_BAT[i] + Time_FEN[i])/2)
        Real_Time.append(Time[i])
        Time[i] = int(convert_time_Nmuon(Time[i])) + 1 
    
    print(Time)
    print("=================")
    print(Time_BAT)
    print("=================")
    print(Time_FEN)
    print("=================")
    print(Real_Time)
    
    path_output = os.path.join("DATA_for_SIM", 'Time.txt')
    
    with open(path_output, 'w') as file:
        for t in Time:
            file.write(f"{t}\n")
    
    np.save(path_TIME,Real_Time)
    return Time

Main()
        
