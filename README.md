# Projet_exp_MUONS
Projet de M1 pfa dmn GEANT4 + analyse python

Projet universitaire (Master 1 PFA - Modélisation Nucléaire) visant à modéliser un detecteur de Muons a triple scintillateur plastique et à analyser les dépôts d'énergie.

Ce dépôt présente une chaîne de traitement complète, séparée en deux environnements distincts : 

--- la simulation par geant 4 (C++).

--- le traitement automatisé (Python).

## Architecture du Projet

Le projet est structuré en deux modules. Chaque module a son propre read_me :

================= GEANT4 ======================

----`/Geant4_simulation_Detecteur_muon_V.3.2` : Code source de la simulation Monte-Carlo.

Consultez le `README` de ce dossier pour les instructions de compilation (CMake), la description de la géométrie et l'utilisation des macros.

================= ANALYSE ======================
----'/Analyse` : Scripts et outils de traitement de données brutes.

Consultez le `README` de ce dossier pour l'architecture du code, les dépendances et le lancement des analyses.
===============================================

## Aperçu 
<img width="1476" height="996" alt="Screenshot_20260505-211726_Perfect Viewer" src="https://github.com/user-attachments/assets/426dc358-f5a4-4a38-b7e4-3e01fa50bc93" />

[SkyMap_Results_0_320M.root.pdf](https://github.com/user-attachments/files/27413432/SkyMap_Results_0_320M.root.pdf)

[Angular_Distribution_of_Muon_Flux.pdf](https://github.com/user-attachments/files/27413444/Angular_Distribution_of_Muon_Flux.pdf)
