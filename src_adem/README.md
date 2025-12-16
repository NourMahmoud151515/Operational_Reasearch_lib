# Surveillance Network Optimizer - Problème 15

## Description
This project solves the Vertex Cover problem for surveillance network optimization. It determines the minimal number of monitoring nodes required to cover all connections in a network.

## Structure
```
src_adem/
├── launch.py           # Entry point for library integration
├── main.py            # Standalone application entry point
├── requirements.txt   # Python dependencies
├── gui/               # User interface components
│   ├── main_window.py
│   ├── graph_widget.py
│   ├── parameters_widget.py
│   ├── results_widget.py
│   └── styles.py
├── solver/            # Optimization algorithms
│   ├── vertex_cover_solver.py
│   ├── greedy_solver.py
│   └── worker.py
├── models/            # Data models
│   ├── data_models.py
│   └── graph.py
├── utils/             # Utility functions
│   └── file_io.py
└── exemples/          # Sample graph files
    └── grille_3x3.json
```

## Integration with Library
This project is integrated into the main Operational Research Library (`library.py`) as Problem 4. The `launch.py` file serves as the integration point, exposing a `MainWindow` class that can be dynamically loaded by the library.

## Running the Application

### From the Library
Run the main library and click on "Problem 4":
```bash
cd /home/adem/Desktop/projects/ro/Operational_Reasearch_lib
python3 library.py
```

### Standalone
Run directly from the src_adem directory:
```bash
cd /home/adem/Desktop/projects/ro/Operational_Reasearch_lib/src_adem
python3 main.py
```

## Dependencies
- PyQt5 >= 5.15.0
- gurobipy >= 10.0.0
- networkx >= 2.6.0
- matplotlib >= 3.5.0

Install dependencies:
```bash
pip install -r requirements.txt
```

## Features
- Interactive graph visualization
- Multiple solving algorithms (exact and greedy)
- Parameter configuration
- Solution export (JSON, CSV)
- Performance metrics and analysis

## Author
Adem
