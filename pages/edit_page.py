from PySide6.QtCore import Signal, Qt
from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLineEdit, QLabel, QTextEdit, QPushButton


class EditPage(QWidget):
    backBtnClicked = Signal()

    def __init__(self, db):
        super().__init__()

        self.db = db
        self.post = None
        self.init_ui()

    def load(self, post_id):
        self.post = self.db.get_post(post_id)
        self.update_ui()

    def init_ui(self):
        self.title_edit = QLineEdit()
        self.author = QLabel()
        self.author.setStyleSheet("padding-left: 3px")
        self.content_edit = QTextEdit()

        self.cancel_btn = QPushButton("취소")
        self.cancel_btn.clicked.connect(self.backBtnClicked.emit)
        self.save_btn = QPushButton("저장")

        footer_layout = QHBoxLayout()
        footer_layout.addStretch()
        footer_layout.addWidget(self.cancel_btn)
        footer_layout.addWidget(self.save_btn)

        layout = QVBoxLayout(self)
        layout.addWidget(self.title_edit)
        layout.addWidget(self.author)
        layout.addWidget(self.content_edit)
        layout.addLayout(footer_layout)

    def update_ui(self):
        if self.post:
            self.title_edit.setText(self.post["title"])
            self.author.setText(self.post["author"])
            self.content_edit.setText(self.post["content"])
