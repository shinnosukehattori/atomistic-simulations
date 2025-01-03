# EMFF - Efficient Molecular Force Fields

EMFF is a Python package for molecular dynamics simulations using NEQUIP models.

## Installation

You can install EMFF using pip:

```bash
pip install git+https://github.com/your-username/emff.git
```

## Usage

EMFF provides a command-line interface for running simulations:

```bash
emff-simulate "CCO" path/to/nequip_model.pth
```

Arguments:
- SMILES string of the molecule
- Path to the deployed NEQUIP model

## Project Structure

```
emff/
├── src/
│   └── emff/
│       ├── __init__.py
│       ├── simulation.py
│       └── nequip_model/
├── tests/
│   └── test_simulation.py
├── docs/
│   └── index.md
├── scripts/
│   └── run_simulation.py
├── requirements.txt
├── setup.py
└── README.md
```

## Contributing

Contributions are welcome! Please open an issue or pull request on GitHub.