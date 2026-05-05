//
// ********************************************************************
// * License and Disclaimer                                           *
// *                                                                  *
// * The  Geant4 software  is  copyright of the Copyright Holders  of *
// * the Geant4 Collaboration.  It is provided  under  the terms  and *
// * conditions of the Geant4 Software License,  included in the file *
// * LICENSE and available at  http://cern.ch/geant4/license .  These *
// * include a list of copyright holders.                             *
// *                                                                  *
// * Neither the authors of this software system, nor their employing *
// * institutes,nor the agencies providing financial support for this *
// * work  make  any representation or  warranty, express or implied, *
// * regarding  this  software system or assume any liability for its *
// * use.  Please see the license in the file  LICENSE  and URL above *
// * for the full disclaimer and the limitation of liability.         *
// *                                                                  *
// * This  code  implementation is the result of  the  scientific and *
// * technical work of the GEANT4 collaboration.                      *
// * By using,  copying,  modifying or  distributing the software (or *
// * any work based  on the software)  you  agree  to acknowledge its *
// * use  in  resulting  scientific  publications,  and indicate your *
// * acceptance of all terms of the Geant4 Software license.          *
// ********************************************************************
//
//
// $Id: ExN01DetectorConstruction.hh,v 1.6 2006/06/29 17:47:13 gunter Exp $
// GEANT4 tag $Name: geant4-08-03-patch-01 $
//

#ifndef ExN01DetectorConstruction_h
#define ExN01DetectorConstruction_h 1

#include "G4VUserDetectorConstruction.hh"
#include "globals.hh"

class G4LogicalVolume;
class G4VPhysicalVolume;

class ExN01DetectorConstruction : public G4VUserDetectorConstruction
{
  public:
    ExN01DetectorConstruction(G4double angle = 0.0); //nouveau detecteur avec un input d'angle ou non (0 par defaut)
    //ExN01DetectorConstruction(); ancien constructeur sans l'input en angle 
    virtual ~ExN01DetectorConstruction();

    virtual G4VPhysicalVolume* Construct();
    
    virtual void ConstructSDandField(); 

    

  private:
  // Input
    G4double fAngle; 
  
  // Logical volumes
    G4LogicalVolume* experimentalHall_log;
    G4LogicalVolume* tonneau_log;
    G4LogicalVolume* paroi_log;
    G4LogicalVolume* scint_log;

    // Physical volumes
    G4VPhysicalVolume* experimentalHall_phys;
    G4VPhysicalVolume* tonneau_phys;
};

#endif