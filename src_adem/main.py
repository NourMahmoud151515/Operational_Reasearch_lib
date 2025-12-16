import sys
import os

# Add src_adem directory to path for absolute imports
project_dir = os.path.dirname(os.path.abspath(__file__))
if project_dir not in sys.path:
    sys.path.insert(0, project_dir)

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt
from gui.main_window import MainWindow

def main():
    # Créer l'application
    app = QApplication(sys.argv)
    app.setApplicationName("Surveillance Network Optimizer")
    app.setStyle('Fusion')  # Style moderne
    
    # Créer et afficher la fenêtre principale
    window = MainWindow()
    window.show()
    
    # Exécuter l'application
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()