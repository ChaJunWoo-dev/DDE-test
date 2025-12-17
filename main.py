import sys

from PySide6 import QtWidgets

from main_window import MainWindow

APP_SIZE = {"WIDTH": 800, "HEIGHT": 600}

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MainWindow()
    widget.resize(APP_SIZE["WIDTH"], APP_SIZE["HEIGHT"])
    widget.show()

    sys.exit(app.exec())