Il y a deux launcher.sh, un pour faire du multi-thread.

Pour utiliser le multi_thread, il faut d'abord l'ouvrir, spécifier le nombre de threads voulant être utilisés, et le nombre d'événements par thread (je voulais mettre directement le nombre d'événements total mais ça dépend du nombre de cœurs, donc pour éviter les divisions et nombres irrationnels etc., j'ai fait ça). Ensuite, pour l'utiliser on tape :

./Multi_Thread.sh

On spécifie l'angle du détecteur ou non (0° par défaut), puis il s'occupe de fusionner les .root et de nommer le fichier en fonction du nombre d'événements simulés, du degré sélectionné et du temps simulé en minutes.

Le simu_exp est un autre .sh pour suivre le même protocole que l'expérimental. Il récupère le temps moyen de mesure et le convertit en muons à envoyer, met ça dans une liste et lit la liste pour configurer un .mac correspondant, puis crée plusieurs dossiers au nom des angles voulant être mesurés (0-90) avec un pas de 10.

Le MAKE DATA SIMEXP convertit les noms des .root et les compile dans un dossier qui va être transmis à l'analyse exp pour comparaison.

Le Lecteur data simulation V1 est la version squelette de la version finale Analyse_simulation. Il sert maintenant seulement à vérifier si les données sont logiques avant de les transmettre à la version finale.

Pour la simulation elle est commenté si besoin.

Commandes utile si besoin:


cmake -DCMAKE_POLICY_VERSION_MINIMUM=3.5 .. #Ma version de root est trop recente d'apres le terminal

chmod +x Multi_Thread.sh

chmod +x simu_exp.sh

rm -r job_*/

rm -r job_angle_*0_deg/


