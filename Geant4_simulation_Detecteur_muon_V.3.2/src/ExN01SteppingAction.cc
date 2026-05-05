#include "G4SystemOfUnits.hh"
#include "ExN01SteppingAction.hh"
#include "G4SteppingManager.hh"
#include "ExN01EventAction.hh"
#include "RootFile_evt.hh"
ExN01SteppingAction::ExN01SteppingAction(ExN01EventAction* myevent) : event_action(myevent)
{ }

ExN01SteppingAction::~ExN01SteppingAction()
{ }


void ExN01SteppingAction::UserSteppingAction(const G4Step *aStep)
{ 
    G4double Edep = aStep->GetTotalEnergyDeposit();
    
    // si la particule passe dans du vide ou de l'air sans déposer d'énergie, on l'ignore, logique
    if (Edep == 0.) return; 

    // Récupère le nom du volume que le muons traverse (genre scint haut ou bas)
    G4VPhysicalVolume* volume = aStep->GetPreStepPoint()->GetTouchableHandle()->GetVolume();
    G4String volName = volume->GetName();

    G4double time = aStep->GetPreStepPoint()->GetGlobalTime();

    G4ThreeVector pos = aStep->GetPreStepPoint()->GetPosition();

    RootFile_evt* position = event_action->GetPosition();

    if (volName == "Scint_Haut") {
        event_action->Edep_1 += Edep;
        if (event_action->T_1 < 0.){ 
            event_action->T_1 = time;
            if (position) position->SetPoint1(pos.x(), pos.y(), pos.z());
        }
    }
    else if (volName == "Scint_Milieu") {
        event_action->Edep_2 += Edep;
        if (event_action->T_2 < 0.){ 
            event_action->T_2 = time;
            if (position) position->SetPoint2(pos.x(), pos.y(), pos.z());
        }
    }
    else if (volName == "Scint_Bas") {
        event_action->Edep_3 += Edep;
        if (event_action->T_3 < 0.){ 
            event_action->T_3 = time;
            if (position) position->SetPoint3(pos.x(), pos.y(), pos.z());
        }
    }
}