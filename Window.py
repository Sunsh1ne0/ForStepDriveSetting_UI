import sys

from PySide6 import QtWidgets
from Test import ForDrive

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = ForDrive()
    widget.show()
    sys.exit(app.exec())

