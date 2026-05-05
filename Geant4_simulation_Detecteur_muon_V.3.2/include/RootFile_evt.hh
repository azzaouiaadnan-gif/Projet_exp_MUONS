#ifndef RootFileRootFile_evt_h
#define RootFileRootFile_evt_h 1

class TFile;
class TTree;

#include "globals.hh" 

class RootFile_evt
{
public:
  RootFile_evt();
  ~RootFile_evt();

public:
  void Create();
  void EndOfAction();
  void FillTree();

  TTree* GetTree() const {return tree;} 
  TFile* GetFileRoot() const {return hfile;}

  // --- VARIABLES PUBLIQUE-----
  
  // Setters et getters pour les Energies 
  void SetEdep1(G4double val) { fEdep1 = val; }
  void SetEdep2(G4double val) { fEdep2 = val; }
  void SetEdep3(G4double val) { fEdep3 = val; }
  
  // Setters et getters pour les Temps de vol
  void SetT1(G4double val) { fT1 = val; }
  void SetT2(G4double val) { fT2 = val; }
  void SetT3(G4double val) { fT3 = val; }

  // Setters et getters pour l'Event ID
  void SetEvent(G4int val) { fevent = val; }
  G4int GetEvent() const { return fevent; }

  // Setters et getters pour la Position du point de contact
  void SetPoint1(G4double x, G4double y, G4double z) { fX1 = x; fY1 = y; fZ1 = z; }
  void SetPoint2(G4double x, G4double y, G4double z) { fX2 = x; fY2 = y; fZ2 = z; }
  void SetPoint3(G4double x, G4double y, G4double z) { fX3 = x; fY3 = y; fZ3 = z; }

private:
  TFile* hfile;
  TTree* tree;

  // --- VARIABLES PRIVE ---
  G4int fevent;
  
  G4double fEdep1;
  G4double fEdep2;
  G4double fEdep3;

  G4double fT1;
  G4double fT2;
  G4double fT3;

  G4double fX1, fY1, fZ1;
  G4double fX2, fY2, fZ2;
  G4double fX3, fY3, fZ3;

  
};

#endif