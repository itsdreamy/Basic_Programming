import sys
from PyQt6.QtWidgets import QApplication
from widget import FloatingOrb

def main():
    # Initialize the OS core application engine
    app = QApplication(sys.argv)
    
    # Fire up our floating custom widget
    orb_widget = FloatingOrb()
    orb_widget.show()
    
    # Maintain a clean exit loop when window is closed
    sys.exit(app.exec())

if __name__ == "__main__":
    main()