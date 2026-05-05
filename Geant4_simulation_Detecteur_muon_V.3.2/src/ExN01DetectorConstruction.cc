//
// ExN01DetectorConstruction.cc
//

#include "ExN01DetectorConstruction.hh"
#include "B2TrackerSD.hh"

#include "G4Material.hh"
#include "G4Box.hh"
#include "G4Tubs.hh"
#include "G4LogicalVolume.hh"
#include "G4ThreeVector.hh"
#include "G4PVPlacement.hh"
#include "globals.hh"
#include "G4SDManager.hh"
#include "G4SystemOfUnits.hh"
#include "G4VisAttributes.hh"
#include "G4Colour.hh"
#include "G4RotationMatrix.hh"

ExN01DetectorConstruction::ExN01DetectorConstruction(G4double angle)
 : G4VUserDetectorConstruction(),
   experimentalHall_log(0), tonneau_log(0), paroi_log(0), scint_log(0),
   experimentalHall_phys(0), tonneau_phys(0),fAngle(angle)
{}

ExN01DetectorConstruction::~ExN01DetectorConstruction() {}

G4VPhysicalVolume* ExN01DetectorConstruction::Construct()
{
  // ===============
  // 1. MATERIAUX
  // ===============
  G4double density;
  G4Element* H  = new G4Element("Hydrogene", "H", 1., 1.00*g/mole);
  G4Element* C  = new G4Element("Carbone", "C", 6., 12.00*g/mole);
  G4Element* N  = new G4Element("Azote", "N", 7., 14.01*g/mole);
  G4Element* O  = new G4Element("Oxygene", "O", 8., 16.00*g/mole);
  G4Element* Al = new G4Element("Aluminium", "Al", 13., 26.98*g/mole);

  // Scintillateur
  G4Material* Scint_Mat = new G4Material("C9H10", density= 1.032*g/cm3, 2);
  Scint_Mat->AddElement(C, 9); Scint_Mat->AddElement(H, 10);

  // Aluminium
  G4Material* Alu_Mat = new G4Material("Aluminium", density= 2.699*g/cm3, 1);
  Alu_Mat->AddElement(Al, 1);

  // Air
  G4Material* Air = new G4Material("Air", density= 1.29*mg/cm3, 2);
  Air->AddElement(N, 70*perCent); Air->AddElement(O, 30*perCent);

  // =========================
  // 2. DIMENSIONS & REGLAGES
  // =========================
  // --- ANGLE DU TONNEAU ---
  G4double angle_telescope = fAngle ; 

  G4double expHall_size = 5.0*m; //Taille du world
  
  // Dimensions Scintillateur 
  G4double scint_L = 73.5*cm; //Geant prends seulement la demi-longueur
  G4double scint_l = 8.5*cm; 
  G4double scint_h = 4*cm;
  
  // Dimensions Tonneau
  G4double tonneau_R_in = 44*cm; 
  G4double tonneau_R_out = 45*cm; // 5mm d'alu
  G4double tonneau_L = 75.6*cm;     // Longueur du tube
  
  // Espacement des plaques
  G4double distance_inter_scint = 19.0*cm; //+2 cm de scint +  2cm scint + 15cm distance inter = 19cm, G4 positione le cm des scints

  // =============
  // 3. GEOMETRIE
  // =============
  
  // --- A. World ---
  G4Box* experimentalHall_box = new G4Box("expHall_box", expHall_size, expHall_size, expHall_size);
  experimentalHall_log = new G4LogicalVolume(experimentalHall_box, Air, "expHall_log");
  experimentalHall_phys = new G4PVPlacement(0, G4ThreeVector(), experimentalHall_log, "expHall", 0, false, 0);

  // --- B. TONNEAU ---
  
  // On crée une rotation pour le tonneau entier
  G4RotationMatrix* rotTelescope = new G4RotationMatrix();
  rotTelescope->rotateZ(angle_telescope);

  G4Tubs* tonneau_box = new G4Tubs("tonneau_box", 0.*cm, tonneau_R_out/2.0 , tonneau_L/2.0, 0.*deg, 360.*deg);
  tonneau_log = new G4LogicalVolume(tonneau_box, Air, "tonneau_log");
  
  // Placement du tonneau 
  tonneau_phys = new G4PVPlacement(rotTelescope, G4ThreeVector(0,0,0), tonneau_log, "Tonneau_Phys", experimentalHall_log, false, 0);

  // --- C. PAROI ALU  ---
  G4Tubs* paroi_box = new G4Tubs("paroi_box", tonneau_R_in/2.0, tonneau_R_out/2.0, tonneau_L/2.0, 0.*deg, 360.*deg);
  paroi_log = new G4LogicalVolume(paroi_box, Alu_Mat, "paroi_log");
  new G4PVPlacement(0, G4ThreeVector(), paroi_log, "Paroi_Alu", tonneau_log, false, 0);

  // --- D. SCINTILLATEURS  ---
  G4Box* scint_box = new G4Box("scint_box", scint_l/2.0, scint_h/2.0, scint_L/2.0); 
  scint_log = new G4LogicalVolume(scint_box, Scint_Mat, "scint_log");

  // Placement des 3 scintillateurs dans le tonneau

  new G4PVPlacement(0, G4ThreeVector(0, distance_inter_scint, 0), scint_log, "Scint_Haut", tonneau_log, false, 0);
  new G4PVPlacement(0, G4ThreeVector(0, 0, 0), scint_log, "Scint_Milieu", tonneau_log, false, 1);
  new G4PVPlacement(0, G4ThreeVector(0, -distance_inter_scint, 0), scint_log, "Scint_Bas", tonneau_log, false, 2);

  // =================
  // 4. VISUALISATION
  // =================
  
  // Monde :
  experimentalHall_log->SetVisAttributes(G4VisAttributes::GetInvisible());

  // Scintillateurs : 
  G4VisAttributes* scintVisAtt = new G4VisAttributes(G4Colour(0.9, 0.0, 0.7)); // violet R + B styler
  scintVisAtt->SetForceSolid(true);
  scint_log->SetVisAttributes(scintVisAtt);

  // Tonneau + Air interieur 
  G4VisAttributes* tonneauVisAtt = new G4VisAttributes(G4Colour(1.0, 1.0, 1.0)); // Blanc
  tonneauVisAtt->SetForceWireframe(true); 
  //tonneauVisAtt->SetForceSolid(true);
  tonneau_log->SetVisAttributes(tonneauVisAtt);

  // Paroi Alu 
  G4VisAttributes* paroiVisAtt = new G4VisAttributes(G4Colour(0.5, 0.5, 0.5)); // Gris
  paroiVisAtt->SetForceWireframe(true);
  paroiVisAtt->SetForceSolid(true);
  paroi_log->SetVisAttributes(paroiVisAtt);

  return experimentalHall_phys;
}

void ExN01DetectorConstruction::ConstructSDandField()
{
  G4SDManager* SDman = G4SDManager::GetSDMpointer();
  G4String SDname = "B2/TrackerChamberSD";
  
  B2TrackerSD* aTrackerSD = new B2TrackerSD(SDname, "TrackerHitsCollection_det2");
  SDman->AddNewDetector(aTrackerSD);
  
  SetSensitiveDetector("scint_log", aTrackerSD);
}