#include "ExN01PrimaryGeneratorAction.hh"
#include "G4SystemOfUnits.hh"
#include "G4Event.hh"
#include "G4ParticleGun.hh"
#include "G4ParticleTable.hh"
#include "G4ParticleDefinition.hh"
#include "globals.hh"
#include "Randomize.hh"
#include "TROOT.h"
#include "TH1.h"
#include "TFile.h"

G4double rand2 = G4UniformRand();

ExN01PrimaryGeneratorAction::ExN01PrimaryGeneratorAction()
{
  G4int n_particle = 1;
  particleGun = new G4ParticleGun(n_particle);
}

ExN01PrimaryGeneratorAction::~ExN01PrimaryGeneratorAction()
{
  delete particleGun;
}

void ExN01PrimaryGeneratorAction::GeneratePrimaries(G4Event* anEvent)
{
  G4ParticleTable* particleTable = G4ParticleTable::GetParticleTable();
  G4String particleName;
  
  particleGun->SetParticleDefinition(particleTable->FindParticle(particleName="mu-"));
    
  TFile *run = new TFile("Mu.root");
  TH1D *distE = (TH1D*)run->Get("Emu");

  // ---- 1. GESTION DE L'ÉNERGIE  ----
  G4double E0 = 0.*MeV;
  E0 = distE->GetRandom()*GeV; 
  
  //while(E0 > 150.*MeV || E0 < 80.*MeV ) { E0 = distE->GetRandom()*GeV; }
  //while(E0 > 150000.*MeV || E0 < 1000.*MeV ) { E0 = distE->GetRandom()*GeV; }
  //while(E0 < 1.*GeV ) { E0 = distE->GetRandom()*GeV; }
  while(E0 < 4.*GeV ) { E0 = distE->GetRandom()*GeV; }
  
  particleGun->SetParticleEnergy(E0);

  // ----- 2. POSITION ---- 
  G4double x = 2 * G4UniformRand() - 1.0; 
  G4double z = 2 * G4UniformRand() - 1.0; 
  particleGun->SetParticlePosition(G4ThreeVector(x*m, 0.25*m, z*m));

  //---- 3. ANGLE THETA, BOUCLE DE PROBABILITÉ + REJET VON NEUMAN-----
  
  G4double tetha = 0.;
  while (true) {
      // tire un angle au hasard entre 0 et 90° (1.57 rad pour la convertion)
      tetha = G4UniformRand() * 1.570796; 
      
      // calcule sa probabilité d'exister dans la nature
      G4double probabilite = pow(cos(tetha), 2) * cos(tetha) * sin(tetha);
      //G4double probabilite = pow(cos(tetha), 2);
      // Puis on décide de le garder ou de le rejeter
      if (G4UniformRand() < probabilite) {
          break; // L'angle est validé, on break
      }
  }

  // ------ 4. DIRECTION FINALE ---- 
  // angle azimutal Phi (cercle complet) 
  G4double phi = 6.283185 * G4UniformRand(); 
  
  particleGun->SetParticleMomentumDirection(G4ThreeVector(cos(phi)*sin(tetha), -cos(tetha), sin(phi)*sin(tetha))); // -y 
  
  // ----- 5. LE TIR FINAL ----
  particleGun->GeneratePrimaryVertex(anEvent);
    
  run->Close();
  delete run;
}