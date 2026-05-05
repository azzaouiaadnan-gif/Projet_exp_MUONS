#ifndef LVD1tAnalisiManager_h
#define LVD1tAnalisiManager_h 1

class G4VPhysicalVolume;
class G4Event;
class G4Run;
class G4Track;
class G4Step;

#include "G4ClassificationOfNewTrack.hh"
#include "G4TrackStatus.hh"
#include "G4Types.hh"
#include "G4UserEventAction.hh"
#include "globals.hh"
#include "G4SDManager.hh"


class LVD1tAnalisiManager;
extern LVD1tAnalisiManager *gLVD1tAnalisiManager; // global LVD1tAnalisiManager

class LVD1tAnalisiManager {
  
public:
  LVD1tAnalisiManager() {
    if (gLVD1tAnalisiManager)
      delete gLVD1tAnalisiManager;
    gLVD1tAnalisiManager = this;
  }
  
  virtual ~LVD1tAnalisiManager() {
    if (gLVD1tAnalisiManager == this)
      gLVD1tAnalisiManager = (LVD1tAnalisiManager *)0;
  }
  
  static LVD1tAnalisiManager *GetAnalysisManager() {
    return gLVD1tAnalisiManager;
  }
  
public:
  // G4UserRunAction
  virtual void BeginOfRunAction(const G4Run */*aRun*/) {;}
  virtual void EndOfRunAction(const G4Run */*aRun*/) {;}
  
  // G4UserEventAction
  virtual void BeginOfEventAction(const G4Event */*anEvent*/) {;}
  virtual void EndOfEventAction(const G4Event */*anEvent*/) {;}

  // G4UserSteppingAction
  virtual void UserSteppingAction(const G4Step */*anEvent*/) {;}
};

#endif
