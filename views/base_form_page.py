from abc import abstractmethod, ABCMeta

from PySide6.QtWidgets import QLineEdit, QTextEdit, QPushButton, QWidget


class QABCMeta(type(QWidget), ABCMeta):
    pass

class BaseFormPage(QWidget, metaclass = QABCMeta):
    def __init__(self, db):
        super().__init__()

        self.db = db
        self.init_ui()
        self.init_specific_ui()

    def init_ui(self):
        self.title_edit = QLineEdit()
        self.content_edit = QTextEdit()

        self.cancel_btn = QPushButton("취소")
        self.cancel_btn.clicked.connect(self.on_cancel)
        self.save_btn = QPushButton("저장")
        self.save_btn.clicked.connect(self.on_save)

    @abstractmethod
    def init_specific_ui(self):
        pass

    @abstractmethod
    def on_cancel(self):
        pass

    @abstractmethod
    def on_save(self):
        pass