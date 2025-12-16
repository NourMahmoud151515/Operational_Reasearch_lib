# This file is the entry point when launched from library.py
# It sets up the Python path and imports the main window class

def _setup_environment():
    """Setup the Python path for proper imports"""
    import sys
    import os
    
    # Get the absolute path of src_adem directory
    _current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Remove src_adem from sys.path if it exists (to re-add at front)
    if _current_dir in sys.path:
        sys.path.remove(_current_dir)
    
    # Insert at the very beginning to take priority over other paths
    # This ensures our 'solver' package is found before any 'solver.py' module
    sys.path.insert(0, _current_dir)
    
    # Clear any cached 'solver' module that might conflict with our package
    if 'solver' in sys.modules:
        # Check if it's not our solver package
        solver_module = sys.modules['solver']
        if not hasattr(solver_module, '__path__'):
            # It's a module, not a package - remove it
            del sys.modules['solver']

# Setup environment before any imports
_setup_environment()

# Import after path is set
from gui.main_window import MainWindow
