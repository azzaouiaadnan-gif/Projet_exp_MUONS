#include "RootFile_evt.hh"
#include "TROOT.h"
#include "TSystem.h"
#include "TFile.h"
#include "TTree.h"
#include <iostream>

// Constructeur : On initialise tout à 0 (ou -1 pour les temps pour pouvoir les prendre apres comparaison simple)
RootFile_evt::RootFile_evt()
{
    hfile = nullptr; 
    tree = nullptr; 

    fevent = 0;

    fEdep1 = 0.;
    fEdep2 = 0.;
    fEdep3 = 0.;

    fT1 = -1.;
    fT2 = -1.;
    fT3 = -1.;

    fX1 = 0.; fY1 = 0.; fZ1 = 0.;
    fX2 = 0.; fY2 = 0.; fZ2 = 0.;
    fX3 = 0.; fY3 = 0.; fZ3 = 0.;
}

// Destructeur
RootFile_evt::~RootFile_evt()
{
}

void RootFile_evt::Create()
{
    std::cout << ">>> Creation de Results.root" << std::endl;
    
    // RECREATE écrase l'ancien fichier s'il existe déjà 
    hfile = new TFile("Results.root", "RECREATE", "ROOT file with telescope data");
    tree = new TTree("tree", "Muon Telescope Data"); 

    // Creation des branches pour l'analyse avec python
    tree->Branch("EventID", &fevent, "fevent/I"); 
    //Energie
    tree->Branch("Edep_1", &fEdep1, "fEdep1/D"); 
    tree->Branch("Edep_2", &fEdep2, "fEdep2/D"); 
    tree->Branch("Edep_3", &fEdep3, "fEdep3/D"); 
    
    //Temps de vol dans le scint
    tree->Branch("T_1", &fT1, "fT1/D"); 
    tree->Branch("T_2", &fT2, "fT2/D"); 
    tree->Branch("T_3", &fT3, "fT3/D");
    
    // Position du point de contact
    tree->Branch("X_1", &fX1, "fX1/D");
    tree->Branch("Y_1", &fY1, "fY1/D");
    tree->Branch("Z_1", &fZ1, "fZ1/D");

    tree->Branch("X_2", &fX2, "fX2/D"); 
    tree->Branch("Y_2", &fY2, "fY2/D");
    tree->Branch("Z_2", &fZ2, "fZ2/D");

    tree->Branch("X_3", &fX3, "fX3/D");
    tree->Branch("Y_3", &fY3, "fY3/D");
    tree->Branch("Z_3", &fZ3, "fZ3/D");
}

void RootFile_evt::FillTree() 
{
    // on s'assure que l'arbre existe avant de le remplir
    if (tree) {
        tree->Fill();
    }
}

void RootFile_evt::EndOfAction()
{
    if (hfile && tree) {
        hfile->cd(); // 
        tree->Write("", TObject::kOverwrite); // force l'écriture de la RAM vers le disque
        hfile->Close();
        std::cout << ">>> .root creer, ok cool " << std::endl;
    }
}