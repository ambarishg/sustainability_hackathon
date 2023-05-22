ncert_biology_dict = {"Animal Kingdom": "CHAP04AnimalKingdom.pkl",
                         "Structural Organisation": "StructuralOrganization.pkl",
                         "Structural Organisation in Animals": "StructuralOrganizationAnimals.pkl",
                         "Cell Structure": "CellStructure.pkl",
                         "Biomolecules": "Biomolecules.pkl",
                         "Cell Cycle": "CellCycle.pkl",
                         "Anatomy Flowering Plants": "AnatomyFloweringPlants.pkl",
                         "Photosynthesis in Higher Plants": "PlantPhysiology.pkl",
                         "Respiration in Plants": "RespirationInPlants.pkl",
                         "Plant Growth Development": "PlantGrowthAndDevelopment.pkl",
                         "Breathing": "Breathing.pkl",
                         "Excretion": "Excretion.pkl",
                         "Neural Control and Coordination": "NeuralControl.pkl",
                         "Chemical Coordination and Integration": "ChemicalCoordination.pkl",
                        "Locomotion": "Locomotion.pkl"}
                      
sustainability_report_dict = {"Kolkata Sustainability Report": "KolkataSustainabilityReport.pkl",
                              "Varanasi Sustainability Report": "VaranasiSustainabilityReport.pkl",
                              "Nestle Sustainability Report": "Nestle.pkl",
                              "Novartis Sustainability Report": "Novartis.pkl"}

def get_ncert_biology_filename(ncert_biology_chapter):
    return ncert_biology_dict[ncert_biology_chapter]

def get_sustainability_report_filename(sustainability_report):
    return sustainability_report_dict[sustainability_report]
