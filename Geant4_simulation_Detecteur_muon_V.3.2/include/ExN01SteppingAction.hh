#ifndef ExN01SteppingAction_h
#define ExN01SteppingAction_h 1
#include "G4UserSteppingAction.hh"
#include "G4TrackStatus.hh"


//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......
class ExN01EventAction;
class G4VPhysicalVolume;
class G4Track;

class ExN01SteppingAction : public G4UserSteppingAction
{
  public:
  ExN01SteppingAction(ExN01EventAction*);
  ~ExN01SteppingAction();
  
  void UserSteppingAction(const G4Step*);
private:
  ExN01EventAction* event_action;
};

//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......

#endif
