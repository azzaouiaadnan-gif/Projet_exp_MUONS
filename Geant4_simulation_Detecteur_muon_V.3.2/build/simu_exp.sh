#!/bin/bash

echo " Démarrage des simulations..."

TIME_ARRAY=($(cat Time.txt))
N_JOBS=${#TIME_ARRAY[@]}

echo " Lancement des jobs..."

for ((i=0; i<N_JOBS; i++))
do
    EVENTS=${TIME_ARRAY[$i]} # le nombre de muons a envoyer par angle 
    ANGLE=$((i * 10))        # On calcule l'angle exact )
    
    DIR="job_angle_${i}0_deg" 
    mkdir -p $DIR
    
    cp exampleN01 $DIR/
    cp Mu.root $DIR/
    
    SEED1=$((RANDOM + i*100))
    SEED2=$((RANDOM + i*200))
    
    cat > $DIR/run.mac <<MACRO
/run/verbose 0
/tracking/verbose 0
/event/verbose 0
/process/verbose 0
/run/initialize
/random/setSeeds $SEED1 $SEED2
/run/beamOn $EVENTS
MACRO
    cd $DIR
    ./exampleN01 run.mac $ANGLE > log.txt 2>&1 &
    cd ..
    echo "   - Angle ${i}0° (Job $i) lancé avec $EVENTS muons..."
done

echo " Calculs $N_JOBS..."
wait
echo " Calcul finis "
