#!/bin/csh
alias xterm xterm -rightbar -sb -sl 1000  
set path=($path /home/m2rps)

## CMAKE

alias Cmake='. /.automnt/tanit2/linux/cmake-3.11.4/bin/cmake'

###############################################################################
## ROOT
###############################################################################
setenv ROOTSYS /home/linux/Geant4/root_v5.34.34.Linux-ubuntu14-x86_64-gcc4.8/root
setenv LD_LIBRARY_PATH ${ROOTSYS}/lib
set path = ($ROOTSYS/bin $path)

###############################################################################
### Geant4
###############################################################################
cd /home/linux/Geant4/geant4.10.04.p02-install/bin/ 
source geant4.csh
cd -

###############################################################################
###  DAWN
###############################################################################
#set path=($path /home/linux/Geant4/dawn-gcc4.9.2/dawn_3_90b)

###############################################################################
### GATE
###############################################################################
#set path=(${path} /home/linux/Geant4/gate_v8.1.p01-install/bin)
