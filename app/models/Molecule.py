from rdkit import Chem
from rdkit.Chem import Descriptors, Draw
from rdkit.Chem.Fragments import fr_SH
from rdkit.Chem.FragmentMatcher import FragmentMatcher

from app.models.FunctionalGroups import Group


class Molecule():
    name : str
    weight : float
    mol : Chem.Mol
    group : Group
    diagram : str
    
    def __init__(self, smiles : str, name : str):
        self.mol = Chem.MolFromSmiles(smiles)
        if (self.isValid()):
            self.name = name
            self.weight = "%.3f" % Descriptors.ExactMolWt(self.mol)
            self.diagram = Draw.MolToImage(self.mol)
            self.set_functional_group()

    # SETTERS
    def set_diagram(self, image_url: str):
        self.diagram = image_url

    def set_functional_group(self):
        self.group = Group.OTHER

        # Identifies Thiol Groups (-SH)
        if (fr_SH(self.mol) > 0):
            self.group = Group.THIOL

        # Identifies Alkenes Groups (C=C)
        p = FragmentMatcher(); p.Init('C=C')
        if (len(p.GetMatches(self.mol)) > 0):
            self.group = Group.ALKENE

    # SMILE VALIDATION
    def isValid(self) -> bool:
        if (self.mol != None): return True
        else: return False
    

    # SPECIAL METHODS
    def __repr__(self):
        if (self.isValid()): return f"Molecule('{self.name}', '{self.diagram}', {self.weight}, '{self.group}')"
        else: return "Invalid SMILES"
        
    
    def __str__(self):
        if (self.isValid()): return f"""
        Molecule Name: {self.name}
        Image: {self.diagram}
        Weight: {self.weight}
        Functional Group: {self.group.name}
        """
        else: return "Invalid SMILES"
    
    def to_dict(self) -> dict:
        return {
            'name' : self.name,
            'weight' : self.weight,
            'group' : self.group.name,
            'diagram' : self.diagram
        }