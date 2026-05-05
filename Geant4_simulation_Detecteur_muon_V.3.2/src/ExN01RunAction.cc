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
// $Id: ExN01RunAction.cc,v 1.9 2006/06/29 17:48:16 gunter Exp $
// GEANT4 tag $Name: geant4-08-03-patch-01 $
// 
//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......
//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......

#include "ExN01RunAction.hh"

#include "G4Run.hh"

//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......

ExN01RunAction::ExN01RunAction()
{}

//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......

ExN01RunAction::~ExN01RunAction()
{}

//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......

void ExN01RunAction::BeginOfRunAction(const G4Run* aRun)
{
  /*G4cout << "### Run " << aRun->GetRunID() << " start." << G4endl;
  ABC = 0;
  AB = 0;
  BC = 0;
  AC = 0;
  A = 0;
  B = 0;
  C = 0;
  
  G4double Total = ABC + AB + A + B + C + AC + BC;
 
  G4cout << " Ratio Ev scintillator : " << G4endl;
  G4cout << " ABC : " << ABC/Total << G4endl;
  G4cout << " AB : " << AB/Total << G4endl;
  G4cout << " A : " << A/Total << G4endl;
  G4cout << " B : " << B/Total << G4endl;
  G4cout << " AC : " << AC/Total << G4endl;
  G4cout << " BC : " << BC/Total << G4endl;
  G4cout << " C : " << C/Total << G4endl;*/
  
}

//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......

void ExN01RunAction::EndOfRunAction(const G4Run*)
{ }

//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......



