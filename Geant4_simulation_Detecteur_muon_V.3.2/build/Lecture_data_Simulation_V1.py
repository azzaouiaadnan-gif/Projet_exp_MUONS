#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 28 13:43:53 2026

@author: meikai
"""
import uproot
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LogNorm
import matplotlib.gridspec as gridspec
import seaborn as sns
import sys as os
from matplotlib import cbook, cm
from matplotlib.colors import LightSource
from mpl_toolkits.mplot3d import Axes3D
from scipy.optimize import curve_fit
from scipy.stats import moyal

Ncanals=3

file = uproot.open("Results_50_test.root")
#file = uproot.open("Results.root")
#file = uproot.open("Results_Final.root")
#file = uproot.open("Results_0_320M.root")

print("Contenu du fichier :", file.keys()) 

tree = file["tree;1"]
print("Variables disponibles :", tree.keys())

data_sim = [tree[f"Edep_{i}"].array(library="np") for i in range(1,Ncanals+1)]
Time_sim = [tree[f"T_{i}"].array(library="np") for i in range(1,Ncanals+1)]
#[data_sim.append(tree[f"Edep_{i}"].array(library="np")) for i in range(Ncanals)]

data = tree.arrays(library="np")    
mask = (data["Edep_1"] > 0) & (data["Edep_2"] > 0) &(data["Edep_3"] > 0) & (data["Z_1"] != 0) & (data["Z_2"] != 0) & (data["Z_3"] != 0)

# filtre
x1 = data["X_1"][mask]
y1 = data["Y_1"][mask]
z1 = data["Z_1"][mask]

x3 = data["X_3"][mask]
y3 = data["Y_3"][mask]
z3 = data["Z_3"][mask]

dx = x3 - x1
dy = y3 - y1  
dz = z3 - z1 

norm = np.sqrt(dx**2 + dy**2 + dz**2)

# --- A. Angle Zénithal (Theta) ---
cos_theta = np.abs(dy) / norm 
theta_rad = np.arccos(cos_theta)
theta_deg = np.degrees(theta_rad)

# --- B. Angle Azimutal (Phi) ---
phi_rad = np.arctan2(dz, dx) 
phi_deg = np.degrees(phi_rad)


def Graph_brut():
    data_graph = []
    for i in range (Ncanals):
        data_graph.append(data_sim[i])
        data_graph[i] = data_graph[i][data_graph[i] > 0]
        print(f"Nombre d'événements enrefistrée data_{i+1} : {len(data_graph[i])}")
        print(f"Énergie moyenne data_{i+1} : {np.mean(data_graph[i])} MeV")
    plt.figure()
    plt.hist(data_graph[1], bins=100, alpha=0.7, color='red', label='Simulation Geant4')
    plt.xlabel("Énergie (MeV)")
    plt.ylabel("Nombre de coups")
    plt.title("Spectre d'Énergie (Données ROOT)")
    plt.legend()
    plt.show()
    #os.exit()


def analyse_simulation():
    data_sim_co = []
    Time_sim_co = []
    print(len(data_sim[0]),len(data_sim[1]))
    coincidence = (data_sim[0] > 0) & (data_sim[1] > 0) & (data_sim[2] > 0)
    for i in range (Ncanals):
        data_sim_co.append(data_sim[i][coincidence])
        Time_sim_co.append(Time_sim[i][coincidence])   
    ToF_sim = Time_sim_co[2] - Time_sim_co[0]
    print(f"Temps de vol moyen et maximal d'un Muon : {np.mean(ToF_sim):.2f} ns  |  {np.max(ToF_sim):.2f} ns")
    print(f"Nombre d'événements enrefistrée data_2 : {len(data_sim_co[1])}")
    print(f"Énergie moyenne data_2 : {np.mean(data_sim_co[1]):.3f} MeV")
    
    plt.figure(figsize=(10,6))
    
    plt.hist(data_sim_co[1], bins=100,alpha = 0.7, color='red', label='Simulation Geant4')
    plt.xlabel("Énergie (MeV)")
    plt.ylabel("Nombre de coups")
    plt.title("Spectre d'Énergie (Données ROOT)")
    plt.xlim((0,30))
    plt.legend()
    plt.show()
    
    '''''
    plt.figure()
    plt.plot(data_sim_co[0],data_sim_co[1],".", alpha=0.07, color='red', label='Simulation Geant4')
    plt.xlim((0,40))
    plt.ylim((0,40 ))
    plt.xlabel("Energie Scint 1 (MeV)")
    plt.ylabel("Energie Scint 2 (MeV)")
    plt.title("Comparaison d'Énergie (Données ROOT)")
    plt.legend()
    plt.show()
    '''
    
def Graph_Energie():
    plt.figure()
    plt.plot(data_sim[0],data_sim[1],".", alpha=0.7, color='red', label='Simulation Geant4')
    plt.xlim((0,40))
    plt.ylim((0,40 ))
    plt.xlabel("Energie Scint 1  (MeV)")
    plt.ylabel("Energie Scint 2  (MeV)")
    plt.title("Comparaison d'Énergie (Données ROOT)")
    plt.legend()
    plt.show

def Graph_dis():
    N_muons = [10448, 10308, 9184,  7797, 6520 ,4732 ]
    angles = [0,10,20,30,40,50]
    cos2 = []
    for i in range (len(N_muons)):
        cos2.append((np.cos(angles[i]*(np.pi/180))**2)*np.max(N_muons))
    plt.plot(angles, N_muons)
    plt.plot(angles, cos2)
def Skymap():
    # SKYMAP-----v.2.0
    sns.set_theme(style="ticks", context="talk")


    fig = plt.figure(figsize=(12, 8))
    gs = gridspec.GridSpec(2, 2, width_ratios=[5, 1], height_ratios=[0.2, 5], wspace=0.05, hspace=0.3)

    ax_cbar  = fig.add_subplot(gs[0, 0])             
    ax_main  = fig.add_subplot(gs[1, 0])             
    ax_right = fig.add_subplot(gs[1, 1], sharey=ax_main) 

    ax_main.set_facecolor('#000004') 
    h = ax_main.hist2d(phi_deg, theta_deg, bins=[60, 60], range=[[-180, 180], [0, 60]], cmap='inferno', norm=LogNorm())

    ax_main.set_xlabel("Azimuthal Angle $\phi$ (degres)", weight='bold')
    ax_main.set_ylabel("Zenithal Angle $\\theta$ (degres)", weight='bold')
    bbox_blind = dict(boxstyle="round,pad=0.4", fc="black", ec="white", lw=1.5, alpha=0.7)
    ax_main.text(0, 55, "Blind Zone", color='white', ha='center', va='center', fontsize=12, fontweight='bold', bbox=bbox_blind)

    bbox_zenith = dict(boxstyle="round,pad=0.4", fc="white", ec="black", lw=1.5, alpha=0.9)
    ax_main.text(0, 5, "Vertical Axis (Z)", color='black', ha='center', va='center', fontsize=12, fontweight='bold', bbox=bbox_zenith)


    sns.histplot(y=theta_deg, bins=60, binrange=[0, 60], ax=ax_right, color='#9a0000', element="step")
    ax_right.set_xlabel("Counts")
    ax_right.tick_params(left=False, labelleft=False) 
    cbar = plt.colorbar(h[3], cax=ax_cbar, orientation='horizontal')
    cbar.set_label("Muons Count (Log Scale)", weight='bold', labelpad=10)
    cbar.ax.xaxis.set_ticks_position('top')
    cbar.ax.xaxis.set_label_position('top')
    fig.suptitle("SKY MAP  :  Detector Angular Acceptance", fontsize=20, fontweight='bold', y=1.05)
    #plt.savefig("SkyMap.png", dpi=400, bbox_inches='tight')
    plt.savefig("SkyMap.pdf", dpi=300, bbox_inches='tight')
    plt.show()

def Acceptance_Resolution():
    #============ RESOLUTION ===========
    plt.figure(figsize=(10, 6))
    
    n, bins, patches = plt.hist(theta_deg, bins=100, range=(0, 90), 
                                color='royalblue', alpha=0.7, edgecolor='black', label='Simulation Geant4')
    
    mean_theta = np.mean(theta_deg)
    std_theta = np.std(theta_deg) #Resolution
    textstr = '\n'.join((
        r'$\mu=%.2f^\circ$' % (mean_theta, ),
        r'$\sigma=%.2f^\circ$' % (std_theta, ),
        r'$N_{muons}=%d$' % (len(theta_deg), )))

    props = dict(boxstyle='round', facecolor='white', alpha=0.5)
    plt.gca().text(0.75, 0.95, textstr, transform=plt.gca().transAxes, fontsize=12,
            verticalalignment='top', bbox=props)

    plt.xlabel("Angle Zénithal Reconstruit (deg)", fontsize=12)
    plt.ylabel("Coups / deg", fontsize=12)
    plt.title("Distribution Angulaire Reconstruite", fontsize=14, fontweight='bold')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.5)

    plt.savefig("Resolution_Angulaire.pdf", dpi=300, bbox_inches='tight')
    
    plt.show()
    
    #============= ACCEPTANCE =============
    
    bin_centers = 0.5 * (bins[:-1] + bins[1:])

    #  Filtre On garde theta > 1° 
    mask = (bin_centers > 1.0) & (bin_centers < 90.0) & (n > 0)

    theta_phys = bin_centers[mask]
    counts_phys = n[mask]

    # SIN * COS
    theta_rad_phys = np.radians(theta_phys)
    geom_factor = np.sin(theta_rad_phys) * np.cos(theta_rad_phys)
    flux_corrige = counts_phys / geom_factor
   
    # Normalisation
    valeur_theorique_au_pic = np.cos(np.radians(angle_detecteur))**2  # angle du detecteur
    flux_corrige = flux_corrige / np.max(flux_corrige) * valeur_theorique_au_pic

    # --- PLOT ---
    plt.figure(figsize=(10, 6))

    #  Données corrigées
    plt.plot(theta_phys, flux_corrige, 'ro', label=r'Données / $(\sin\theta \cdot \cos\theta)$', markersize=4)

    #  Théorie Cos^2
    x_theorie = np.linspace(0, 70, 100)
    y_theorie = np.cos(np.radians(x_theorie))**2 
    plt.plot(x_theorie, y_theorie, 'k--', linewidth=2, label=r'Loi Théorique $\cos^2(\theta)$')

    plt.xlabel("Angle Zénithal (deg)", fontsize=12)
    plt.ylabel("Flux Relatif Normalisé", fontsize=12)
    plt.title("Loi Physique Retrouvée (Correction Projection + Angle Solide)", fontsize=14, fontweight='bold')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.5)

    plt.savefig("Acceptance_géometrique.pdf", dpi=300 , bbox_inches='tight')
    plt.show()
    return 

def fit_landau_K(amp):
    coincidence = (data_sim[0] > 0) & (data_sim[1] > 0) & (data_sim[2] > 0)
    data_fit = data_sim[1][coincidence]
    data_fit = data_fit[(data_fit > 0.5) & (data_fit < 25)]
    counts, bins = np.histogram(data_fit, bins=80)
    bin_centers = (bins[:-1] + bins[1:]) / 2
    def landau_pdf(x, amp, loc, scale):
        return amp * moyal.pdf(x, loc, scale)
    p0 = [np.max(counts), bin_centers[np.argmax(counts)], 0.5]
    popt, _ = curve_fit(landau_pdf, bin_centers, counts, p0=p0)
    mpv_sim = popt[1]
    width_sim = popt[2]
    
    # Calcul de la constante K
    K = mpv_sim / amp

    print(f"FIT DE LANDAU RÉUSSI")
    print(f"MPV Simulation (E_MIP) : {mpv_sim:.3f} MeV")
    print(f"Largeur du pic (sigma) : {width_sim:.3f} MeV")
    print(f"Constante K calculée  : {K:.4f} MeV/mV")

    # Plot
    plt.figure(figsize=(8, 5))
    plt.hist(data_fit, bins=80, alpha=0.8, color='r', label="Data Sim (MIPs)")
    x_axis = np.linspace(min(bin_centers), max(bin_centers), 500)
    plt.plot(x_axis, landau_pdf(x_axis, *popt), 'k-', lw=2, 
             label=f"Fit Landau (Moyal)\nMPV = {mpv_sim:.2f} MeV")
    
    plt.axvline(mpv_sim, color='b', linestyle='--', label=f"E_peak = {mpv_sim:.2f} MeV")
    plt.xlabel("Énergie déposée (MeV)")
    plt.ylabel("Nombre de muons")
    plt.xlim(4, 25)
    plt.title(f"Extraction de K (K = {K:.4f} MeV/mV)")
    plt.legend()
    plt.grid(alpha=0.3)
    plt.savefig("Fit_Landau.pdf", dpi=300 , bbox_inches='tight')
    plt.show()

    return K 
print(0.040*75)

def fit_landau_3_channels(v_mpv_exp_list):
    """
    Extrait l'énergie MPV (en MeV) des 3 détecteurs simulés par Geant4,
    et calcule les 3 constantes de calibration K (en mV/MeV) en utilisant
    les amplitudes expérimentales fournies.
    """
    # 1. On exige que le muon ait traversé les 3 plans (comme dans la réalité)
    coincidence = (data_sim[0] > 0) & (data_sim[1] > 0) & (data_sim[2] > 0)
    
    K_constants = []
    E_mpv_list = []
    
    # Configuration du graphique
    plt.figure(figsize=(15, 5))
    
    # Fonction de Landau (approximation de Moyal)
    def landau_pdf(x, amp, loc, scale):
        return amp * moyal.pdf(x, loc, scale)
        
    for ch in range(3):
        # 2. Filtrage des données pour le canal en cours
        data_fit = data_sim[ch][coincidence]
        # On coupe les queues extrêmes pour aider l'algorithme de fit
        data_fit = data_fit[(data_fit > 0.5) & (data_fit < 25)]
        
        counts, bins = np.histogram(data_fit, bins=80)
        bin_centers = (bins[:-1] + bins[1:]) / 2
        
        # 3. Paramètres initiaux (Guesses)
        guess_amp = np.max(counts)
        guess_loc = bin_centers[np.argmax(counts)]
        guess_scale = 0.5
        
        p0 = [guess_amp, guess_loc, guess_scale]
        
        # 4. Fit
        try:
            popt, _ = curve_fit(landau_pdf, bin_centers, counts, p0=p0)
            mpv_sim = popt[1]
        except:
            print(f"Échec du fit pour canal {ch}")
            mpv_sim = guess_loc # Sécurité
            popt = p0
            
        E_mpv_list.append(mpv_sim)
        
        # 5. Calcul de K (en mV/MeV)
        K_mV_MeV = v_mpv_exp_list[ch] / mpv_sim
        K_constants.append(K_mV_MeV)
        
        # 6. Tracé du sous-graphique
        plt.subplot(1, 3, ch+1)
        plt.hist(data_fit, bins=80, alpha=0.6, color='red', label="Geant4 (MIPs)")
        
        x_axis = np.linspace(min(bin_centers), max(bin_centers), 200)
        plt.plot(x_axis, landau_pdf(x_axis, *popt), 'k-', lw=2, label=f"Fit MPV: {mpv_sim:.2f} MeV")
        plt.axvline(mpv_sim, color='blue', linestyle='--')
        
        plt.xlabel("Énergie déposée (MeV)")
        if ch == 0:
            plt.ylabel("Nombre de muons")
            
        plt.title(f"Canal {ch} | K = {K_mV_MeV:.1f} mV/MeV")
        plt.legend()
        
    plt.tight_layout()
    plt.savefig("Fit_Landau_3voies.pdf", dpi=300, bbox_inches='tight')
    plt.show()
    
    # 7. Résumé dans la console
    print("\n" + "="*40)
    print("=== CONSTANTES DE CALIBRATION FINALES ===")
    print("="*40)
    for ch in range(3):
        print(f"Canal {ch} : V_exp = {v_mpv_exp_list[ch]:.1f} mV  |  E_sim = {E_mpv_list[ch]:.2f} MeV  -->  K_{ch} = {K_constants[ch]:.2f} mV/MeV")
        
    return K_constants


 
if __name__ == "__main__":
    angle_detecteur = 0
    #Graph_dis()

    #Graph_brut()

    analyse_simulation()

    #Graph_Energie()

    #Skymap()

    #Acceptance_Resolution()
    
    #V_exp_trouves = [88.3, 100.9, 107.2] 
    #K_finaux = fit_landau_3_channels(V_exp_trouves)
    #fit_landau_K(0.1020)
    
   

