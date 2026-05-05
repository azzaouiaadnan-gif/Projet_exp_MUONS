#ifndef VetoAna_h
#define VetoAna_h 1

#include "LVD1tAnalisiManager.hh"
#include "G4UserEventAction.hh"
#include "G4UserRunAction.hh"
#include "globals.hh"
#include "RootFile_evt.hh"

class G4VPhysicalVolume;
class G4Event;
class G4Run;
class G4Track;
class G4Step;
class G4HCofThisEvent;


// class VetoAna : public LVD1tAnalisiManager {
class VetoAna : public G4UserEventAction, public G4UserRunAction {
  
public:
  VetoAna();
  virtual ~VetoAna();
  
public:
 virtual void BeginOfRunAction(const G4Run*);
virtual  void EndOfRunAction(const G4Run*);
  
  // using LVD1tAnalisiManager::BeginOfEventAction;
virtual  void BeginOfEventAction(const G4Event*);
  //  using LVD1tAnalisiManager::EndOfEventAction;

virtual  void EndOfEventAction(const G4Event*);
virtual  void UserSteppingAction(const G4Step*);
 
public:
 G4int event_id;
  G4double edeptot0;
  G4double edeptotH0;
  G4double edeptotH1;
  G4double LTot0;
  G4double LTot1;
  G4double ekin0;
  G4double  ekin1;
  G4int vol0;
  G4int vol1;
   G4double E0;
 G4double E1;
 G4double E2;
 G4double E3;

 RootFile_evt *test;

  G4double IDCurrent;
 G4int gPb, nPb, ePb,muPb,otherPb;
  G4double Edep_gPb, Edep_nPb, Edep_ePb, Edep_otherPb,Edep_muPb;
 
//G4double totEPb;
 
private:
 G4int trackerCollID1;
 G4int trackerCollID2; 
 G4int trackerCollID3; 
 
  G4int event;
};

#endif
