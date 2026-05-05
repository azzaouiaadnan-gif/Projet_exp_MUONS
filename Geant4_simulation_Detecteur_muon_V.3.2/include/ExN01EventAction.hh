#ifndef ExN01EventAction_h
#define ExN01EventAction_h 1

#include "G4UserEventAction.hh"
#include "globals.hh"

class G4Event;
class RootFile_evt;
class ExN01EventAction : public G4UserEventAction
{
  public:
    ExN01EventAction();
    ~ExN01EventAction();

  public:
    void BeginOfEventAction(const G4Event*);
    void EndOfEventAction(const G4Event*);
   
    // variables pour le root (en plublic hein)
    RootFile_evt* GetPosition();
    
    G4double Edep_1;
    G4double Edep_2;
    G4double Edep_3;
    
    G4double T_1;
    G4double T_2;
    G4double T_3;
};

#endif  

