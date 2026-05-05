=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+
=-=-=-=-=--=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Il y a 2 dossiers : une analyse des données expérimentales et une des données
de la simulation. Ils disposent d'un main.py chacun.
=-=-=-=-=--=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

================================================================
================================================================
L'analyse expérimentale présente différents .py :
================================================================
================================================================

Convert_data.py : Lit les .dat bruts et les transforme en listes utilisables
pour l'analyse. Donne aussi le temps de mesure.

================================================================
================================================================

Analyse_3_canaux_exp.py : Filtre les données selon un ToF et une tolérance
donnés dans le main.py pour les 3 canaux.

================================================================
================================================================

Fit_landau.py : Prend les données analysées, fait un fit de Landau, plot et
donne les MPV calculées.

================================================================
================================================================

Plot.py : Contient toutes les fonctions de plot succinctes.

================================================================
================================================================

Run3.py : Fait une boucle d'analyse complète (lecture + analyse) sur tous
les fichiers d'un dossier donné.

=-=-=-=-=--=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Chaque plot est enregistré dans le dossier Plot_pdf.
=-=-=-=-=--=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
L'analyse simulation présente aussi différents .py :
=-=-=-=-=--=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

================================================================
================================================================

lecteur.py : Convertit les données du fichier .ROOT en listes et extrapole
les angles zénithaux et azimutaux, également donnés en listes.

================================================================
================================================================

Analyse_simu.py : Prend les données lues et qualifiées, calcule par la suite
le nombre de muons détectés en faisant un masque et le ToF. Intègre la
possibilité de modifier la tolérance du masque de coïncidence.

================================================================
================================================================

Fit_landau_3_canaux.py : Calcule les fits et MPV simulés des trois canaux.

================================================================
================================================================

Skymap.py : Prend les angles extrapolés par le lecteur.py et trace un
tableau de chaleur en fonction de l'angle zénithal et azimuthal.

================================================================
================================================================

Acceptance.py : Calcule la distribution du nombre de muons par leurs angles
zénithaux.

================================================================
================================================================

EnergievEnergie.py : Plot désigné pour montrer l'impact de la tolérance sur
les données simulées.

================================================================
================================================================

Run3_sim.py : Lit un dossier où sont situées les données simulées avec un
temps moyen de l'expérimentale, applique la boucle (lecture + analyse),
met tout dans une liste et l'enregistre.

================================================================
================================================================
