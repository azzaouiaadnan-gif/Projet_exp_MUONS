#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 19:10:25 2026

@author: Azzaoui
"""
import numpy as np
import re

def convert_data(filename):
    
    list_dat = []
    
    with open(filename) as file:
        for line in file:
            list_dat.append(line.strip())
            
    c = list_dat[3]
    c = c.strip(" =").split("==") 
    info = {}
    
    for cx in c :
        cx = cx.strip()
        if ":" in cx:
            cl, v = cx.split(":", 1) 
            info[cl.strip()] = v.strip().split()[0]
            
        elif "DATA SAMPLES" in cx:
            m = re.search(r'\[(.*?)\]', cx)
            if m:
                info["DATA SAMPLES"] = m.group(1)    
                
    Ncanals  = int(info['NB OF CHANNELS ACQUIRED']) 
    Time_step = int(info['DATA SAMPLES'])
    Sampling_time = float(info['Sampling Period'])*10**(-3)
    longueur = len(list_dat)
    
    time_length = Time_step * Sampling_time
    Time_sampling = np.arange(0 , time_length, Sampling_time) 
    list_data = list_dat[4:longueur]

    Nlines = Ncanals*2 + 2
    Nevents = int((longueur-4)/(Nlines))
    list_event = []

    for i in range (Nevents):
        a = i*Nlines
        b = a + Nlines
        list_event.append(list_data[a:b])

    def Event_sep(a): #V3 elle evite les problemes de fichier corrompu
        e = []
        for i in range(1, Ncanals + 1): 
            try:
                raw_line = list_event[a][1 + i * 2].strip().split()
                clean_line = []
                for x in raw_line:
                    try:
                        clean_line.append(float(x))
                    except ValueError:
                        continue 
                if len(clean_line) > Time_step:
                    clean_line = clean_line[-Time_step:]
                elif len(clean_line) < Time_step:
                    clean_line.extend([0.0] * (Time_step - len(clean_line)))
                    
                e.append(clean_line)
                
            except Exception as err:
                print(f"Erreur inattendue à l'événement {a}, canal {i}: {err}")
                e.append([0.0] * Time_step) # Secu si ca bug regardez les events indiquer et enlevez les
        return e
    
    """
    def Event_sep(a):
        e= []
        for i in range (1,Ncanals+1) :
            e.append([float(x) for x in list_event[a][1+i*2].strip().split()] )
        return e
    """
    
    
    array_events = np.zeros((Nevents, Ncanals, Time_step))
    
    for i in range(Nevents):
         array_events[i] = Event_sep(i)
    # V2 REcuperation du temps de mesure pour normaliser apres, on prends le temps du premier et dernier EVENT    
    Total_time = 0.0
    if Nevents > 0:
        try:
            ligne_premier_event = list_event[0][1]
            ligne_dernier_event = list_event[-1][1]
            def extraire_temps_reel(ligne):
                if "TDC corrected time =" in ligne:
                    # 12h12m21s,007.701.360ns "
                    temps_str = ligne.split("TDC corrected time =")[1].replace("===", "").strip()
                    
                    if "s," in temps_str:
                        partie_entiere, partie_frac = temps_str.split("s,")
                        
                        heures = float(partie_entiere.split("h")[0])
                        minutes = float(partie_entiere.split("h")[1].split("m")[0])
                        secondes = float(partie_entiere.split("m")[1])
                        
                        fraction_str = partie_frac.replace("ns", "").replace(".", "").strip()
                        fraction_seconde = float(fraction_str) * 1e-9
                        return (heures * 3600) + (minutes * 60) + secondes + fraction_seconde
                    else:
                
                        heures = float(temps_str.split("h")[0])
                        minutes = float(temps_str.split("h")[1].split("m")[0])
                        secondes = float(temps_str.split("m")[1].split("s")[0])
                        return (heures * 3600) + (minutes * 60) + secondes
                return None

            t_start = extraire_temps_reel(ligne_premier_event)
            t_end = extraire_temps_reel(ligne_dernier_event)
            
            if t_start is not None and t_end is not None:
                # Sécurité : passage de minuit
                if t_end < t_start:
                    t_end += 24 * 3600
                    
                Total_time = t_end - t_start
                
        except Exception as e:
            print(f"Erreur lors de l'extraction de l'heure : {e}")

 
    return array_events, Ncanals, Time_step, Sampling_time, Time_sampling ,Total_time



""" 
Total_time = 0.0 #V1 
if Nevents > 0:
    ligne_premier_event = list_event[0][1]
    ligne_dernier_event = list_event[-1][1]
    def extraire_tdc(ligne):
        segments = ligne.split("==")
        for seg in segments:
            if "TDC" in seg and "corrected" not in seg:
                valeur = seg.split("=")[1].strip()
                return int(valeur)
        return None

    tdc_start = extraire_tdc(ligne_premier_event)
    tdc_end = extraire_tdc(ligne_dernier_event)
    
    if tdc_start is not None and tdc_end is not None:
        print(tdc_end)
        print(tdc_start)
        diff = tdc_end - tdc_start
        print(diff/200)
        Total_time = ((tdc_end - tdc_start) / 200)*1e-6  # 200 MHz 
        
        print(Total_time)
"""



















