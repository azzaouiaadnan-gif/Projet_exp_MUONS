#include "B2TrackerHit.hh"

#include "G4Event.hh"
#include "G4EventManager.hh"
#include "G4HCofThisEvent.hh"
#include "G4VHitsCollection.hh"
#include "G4TrajectoryContainer.hh"
#include "G4Trajectory.hh"
#include "G4VVisManager.hh"
#include "G4SDManager.hh"
#include "G4UImanager.hh"
#include "G4ios.hh"
#include "CLHEP/Random/RandGauss.h"
#include "VetoAna.hh"
#include "RootFile_evt.hh"
#include "ExN01RunAction.hh"
#include <iostream>
#include <fstream>
#include <iterator>
#include <string>
#include <vector>
//extern RootFile_evt *test
RootFile_evt* myRootFile = nullptr;
VetoAna::VetoAna()
{
	event=-1;
	//	trackerCollID1 = -1; // Chaque TrackerCollID est associé à un scintillateur
	trackerCollID2 = -1;
	//	trackerCollID3 = -1;
	myRootFile = new RootFile_evt();
}
VetoAna::~VetoAna()
{;}

void VetoAna::BeginOfRunAction(const G4Run* /**aRun*/)
{
    myRootFile->Create();
}

void VetoAna::EndOfRunAction(const G4Run */*aRun*/)
{
    myRootFile->EndOfAction();
}

void VetoAna::BeginOfEventAction(const G4Event* evt)
{
	//G4cout << "try" << G4endl;

	event=evt->GetEventID();

	G4SDManager * SDman = G4SDManager::GetSDMpointer();


	if(trackerCollID2)
	{
		G4String colNam;
		//G4cout << "try2 2" << G4endl;

		trackerCollID2 = SDman->GetCollectionID(colNam="TrackerHitsCollection_det2");

		//G4cout << "try2 3" << G4endl;

	}



	//initialisation
	//G4cout << "try 4" << G4endl;
}





void VetoAna::EndOfEventAction(const G4Event* evt)
{
    // j'ai neutraliser/enlever l'ancienne fonct car elle fait chier. 
}









void VetoAna::UserSteppingAction(const G4Step* aStep)  
{}
