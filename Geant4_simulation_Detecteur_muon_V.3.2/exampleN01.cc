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
// $Id: exampleN01.cc,v 1.6 2006/06/29 17:47:10 gunter Exp $
// GEANT4 tag $Name: geant4-08-03-patch-01 $
//
// 
// --------------------------------------------------------------
//      GEANT 4 - exampleN01
// --------------------------------------------------------------

#include "G4RunManager.hh"

#include "G4UImanager.hh"
#include "QBBC.hh"

#include "G4VisExecutive.hh"
#include "G4UIExecutive.hh"
#include "G4SystemOfUnits.hh"

#include "Randomize.hh"

#include "ExN01DetectorConstruction.hh"
#include "ExN01PhysicsList.hh"
#include "ExN01PrimaryGeneratorAction.hh"
#include "ExN01RunAction.hh"
#include "ExN01EventAction.hh"
#include "ExN01SteppingAction.hh"
#include "B2TrackerHit.hh"
#include "B2TrackerSD.hh"
#include "VetoAna.hh"

#include "RootFile_evt.hh"
namespace CLHEP {}
using namespace CLHEP;
using namespace std;
int main(int argc,char** argv)
{
  G4int seed = time(0);
  HepRandom::setTheSeed(seed);
  G4UIExecutive* ui = 0;
  if ( argc == 1 ) {
    ui = new G4UIExecutive(argc, argv);
  }
  
  G4double angle_deg = 0.0;
  if (argc > 2) {
      // pour "./exampleN01 run.mac 10" argc = 3 donc ca lance mais si on lance "./exampleN01 run.mac " argc = 2 donc angle = 0 par defaut 
      angle_deg = std::atof(argv[2]); 
  }
  // ====================================================================

  // Construct the default run manager
  //
  G4RunManager* runManager = new G4RunManager;

  // set mandatory initialization classes
  //
  G4VUserDetectorConstruction* detector = new ExN01DetectorConstruction(angle_deg * deg);
  runManager->SetUserInitialization(detector);
  //
  G4VUserPhysicsList* physics = new ExN01PhysicsList;
  runManager->SetUserInitialization(physics);

  // set mandatory user action class
  //
  G4VUserPrimaryGeneratorAction* gen_action = new ExN01PrimaryGeneratorAction;
  runManager->SetUserAction(gen_action);

  //other action classer

  G4UserRunAction* run_action = new ExN01RunAction;
  VetoAna *analysis = new VetoAna();
  
  // On laisse VetoAna gérer le Run (car il ouvre et ferme le fichier ROOT)
  runManager->SetUserAction((G4UserRunAction *) analysis);
  
  // ICI ON CORRIGE : On force Geant4 à utiliser NOTRE EventAction !
  ExN01EventAction* event_action = new ExN01EventAction;
  runManager->SetUserAction(event_action); 
  
  G4UserSteppingAction* stepping_action = new ExN01SteppingAction(event_action);
  runManager->SetUserAction(stepping_action);

  // Initialize G4 kernel
  
  runManager->Initialize();
  G4VisManager* visManager = new G4VisExecutive;
  // G4VisExecutive can take a verbosity argument - see /vis/verbose guidance.
  // G4VisManager* visManager = new G4VisExecutive("Quiet");
  visManager->Initialize();

  // Get the pointer to the User Interface manager
  G4UImanager* UImanager = G4UImanager::GetUIpointer();

  // Process macro or start UI session
  //
  if ( ! ui ) { 
    // batch mode
    G4String command = "/control/execute ";
    G4String fileName = argv[1];
    UImanager->ApplyCommand(command+fileName);
  }
  else { 
    // interactive mode
    UImanager->ApplyCommand("/control/execute vis.mac");
    ui->SessionStart();
    delete ui;
  }


  return 0;
}


