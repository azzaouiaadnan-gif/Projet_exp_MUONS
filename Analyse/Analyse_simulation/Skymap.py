# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 13:02:47 2026

@author: Azzaoui
"""
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
import matplotlib.gridspec as gridspec
import seaborn as sns
import os

def Skymap(phi_deg, theta_deg,file , angle_detecteur):
    # SKYMAP-----v.2.1
    sns.set_theme(style="ticks", context="talk")


    fig = plt.figure(figsize=(12, 8))
    #gs = gridspec.GridSpec(2, 2, width_ratios=[5, 1], height_ratios=[0.2, 5], wspace=0.05, hspace=0.3)
    gs = gridspec.GridSpec(2, 2, width_ratios=[5, 1], height_ratios=[0.2, 5], wspace=0.05, hspace=0.08)
    ax_cbar  = fig.add_subplot(gs[0, 0])             
    ax_main  = fig.add_subplot(gs[1, 0])             
    ax_right = fig.add_subplot(gs[1, 1], sharey=ax_main) 

    ax_main.set_facecolor('#000004') 
    h = ax_main.hist2d(phi_deg, theta_deg, bins=[60, 60], range=[[-180, 180], [0, 60]], cmap='vanimo', norm=LogNorm())

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
    #cbar.set_label("Muons Count (Log Scale)", weight='bold', labelpad=10)
    cbar.set_label("Muons Count (Log Scale)", weight='bold', labelpad=5)
    cbar.ax.xaxis.set_ticks_position('top')
    cbar.ax.xaxis.set_label_position('top')
    
    sub_title = f"Detector angle = {angle_detecteur}°"
    fig.suptitle(f"SKY MAP  :  Detector Angular Acceptance\n{sub_title}", fontsize=20, fontweight='bold', y=1.07)
    #plt.savefig("SkyMap.png", dpi=400, bbox_inches='tight')
    
    save_path = os.path.join("PDF", f"SkyMap_{file}.pdf" )

    plt.savefig(save_path,bbox_inches='tight')
    
    plt.show()