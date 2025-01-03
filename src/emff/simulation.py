import argparse
import torch
import numpy as np
import matplotlib.pyplot as plt
from rdkit import Chem
from rdkit.Chem import AllChem
from ase import Atoms
from ase.calculators.calculator import Calculator
from nequip.ase import NequIPCalculator

class AtomisticSimulator:
    def __init__(self, atoms, model_path):
        self.atoms = atoms
        self.calculator = NequIPCalculator.from_deployed_model(model_path)
        self.atoms.set_calculator(self.calculator)
        
    def run_md(self, steps=1000, dt=0.001, temperature=300):
        from ase.md.verlet import VelocityVerlet
        from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
        
        # Set initial velocities
        MaxwellBoltzmannDistribution(self.atoms, temperature_K=temperature)
        
        # Run MD
        dyn = VelocityVerlet(self.atoms, timestep=dt*ase.units.fs)
        positions_history = []
        
        def save_positions(atoms=self.atoms):
            positions_history.append(atoms.get_positions())
            
        dyn.attach(save_positions, interval=10)
        
        for step in range(steps):
            dyn.run(1)
            if step % 100 == 0:
                print(f"Step {step}: Energy = {self.atoms.get_potential_energy():.4f} eV")
                
        return np.array(positions_history)
    
    def visualize(self, positions_history):
        fig, ax = plt.subplots()
        for i in range(positions_history.shape[1]):
            ax.plot(positions_history[:, i, 0], positions_history[:, i, 1])
        plt.show()

def create_system_from_smiles(smiles, box_size=20.0):
    # Create molecule from SMILES
    mol = Chem.MolFromSmiles(smiles)
    mol = Chem.AddHs(mol)
    AllChem.EmbedMolecule(mol)
    AllChem.MMFFOptimizeMolecule(mol)
    
    # Get atomic positions and numbers
    positions = mol.GetConformer().GetPositions()
    atomic_numbers = [atom.GetAtomicNum() for atom in mol.GetAtoms()]
    
    # Create ASE Atoms object with periodic boundary conditions
    atoms = Atoms(numbers=atomic_numbers, positions=positions)
    atoms.set_cell([box_size, box_size, box_size])
    atoms.set_pbc(True)
    
    return atoms

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run MD simulation using NEQUIP model')
    parser.add_argument('smiles', type=str, help='SMILES string of the molecule')
    parser.add_argument('model_path', type=str, help='Path to the deployed NEQUIP model')
    args = parser.parse_args()
    
    # Create system from SMILES
    atoms = create_system_from_smiles(args.smiles)
    
    # Initialize simulator with NEQUIP model
    simulator = AtomisticSimulator(atoms, args.model_path)
    
    # Run molecular dynamics simulation
    positions_history = simulator.run_md(steps=1000)
    
    # Visualize results
    simulator.visualize(positions_history)