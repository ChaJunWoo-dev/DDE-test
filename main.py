import sys

from PySide6 import QtWidgets

from const.constant import APP_SIZE
from db.db_manager import DBManager
from windows.main_window import MainWindow

if __name__ == "__main__":
    db = DBManager()
    app = QtWidgets.QApplication([])

    widget = MainWindow(db)
    widget.resize(APP_SIZE["WIDTH"], APP_SIZE["HEIGHT"])
    widget.show()

    exit_code = app.exec()
    db.close()
    sys.exit(exit_code)
