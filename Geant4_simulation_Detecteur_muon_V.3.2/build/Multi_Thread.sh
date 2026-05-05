#!/bin/bash
N_JOBS=8
EVENTS_PER_JOB=30000

Angle=${1:-0}

TOTAL_EVENTS=$((N_JOBS * EVENTS_PER_JOB))

SIM_TIME=$(echo "scale=2; $TOTAL_EVENTS / 40000" | bc) # calcul du temps simulé

FILE="Results_${TOTAL_EVENTS}ev_${Angle}°deg_${SIM_TIME}_min.root"



echo " $N_JOBS simulation lancer avec un angle de $Angle° "

for ((i=0; i<N_JOBS; i++))
do
    DIR="job_$i"
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
/run/beamOn $EVENTS_PER_JOB
MACRO
    cd $DIR
    ./exampleN01 run.mac $Angle  > log.txt 2>&1 &
    cd ..
    
    echo "   - Job $i lancer "
done

echo "Calcul en cours..."
wait
echo "Finis."

echo "Fusion des fichiers ROOT en cours..."

hadd -f $FILE job_*/Results.root

echo "--------------------------------------------------------------"
echo "Fichier des résultats enregistré  : $FILE"
echo "--------------------------------------------------------------"
