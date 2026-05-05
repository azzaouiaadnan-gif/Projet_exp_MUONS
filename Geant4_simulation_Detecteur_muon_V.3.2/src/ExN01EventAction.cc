#include "ExN01EventAction.hh"
#include "G4Event.hh"
#include "RootFile_evt.hh" 

extern RootFile_evt* myRootFile; 

ExN01EventAction::ExN01EventAction() : G4UserEventAction()
{}

ExN01EventAction::~ExN01EventAction()
{}

RootFile_evt* ExN01EventAction::GetPosition(){return myRootFile;}

void ExN01EventAction::BeginOfEventAction(const G4Event*)
{
    // initialisation des donées
    Edep_1 = 0.;
    Edep_2 = 0.;
    Edep_3 = 0.;
    
    T_1 = -1.;
    T_2 = -1.;
    T_3 = -1.;
}

void ExN01EventAction::EndOfEventAction(const G4Event* evt)
{
    // On sauvegarde seulement si il a deposer de l'énergie dans le scint 
    if (Edep_1 > 0. || Edep_2 > 0. || Edep_3 > 0.) {
        
        // On envoie les valeurs à la classe ROOT
        myRootFile->SetEvent(evt->GetEventID());
        
        myRootFile->SetEdep1(Edep_1);
        myRootFile->SetEdep2(Edep_2);
        myRootFile->SetEdep3(Edep_3);
        
        myRootFile->SetT1(T_1);
        myRootFile->SetT2(T_2);
        myRootFile->SetT3(T_3);
        

        // on remplis le tree :
        myRootFile->FillTree();
    }
}