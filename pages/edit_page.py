from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLineEdit, QLabel, QTextEdit, QPushButton


class EditPage(QWidget):
    cancelBtnClicked = Signal()

    def __init__(self, detail_page):
        super().__init__()

        self.detail_page = detail_page
        self.init_ui()

    def init_ui(self):
        title_edit = QLineEdit()
        title_edit.setText("기존 제목입니다.")
        author_edit = QLabel("작성자명")
        content_edit = QTextEdit()
        content_edit.setText("기존 내용입니다.")

        self.cancel_btn = QPushButton("취소")
        self.cancel_btn.clicked.connect(self.cancelBtnClicked.emit)
        self.save_btn = QPushButton("저장")

        footer_layout = QHBoxLayout()
        footer_layout.addStretch()
        footer_layout.addWidget(self.cancel_btn)
        footer_layout.addWidget(self.save_btn)

        layout = QVBoxLayout(self)
        layout.addWidget(title_edit)
        layout.addWidget(author_edit)
        layout.addWidget(content_edit)
        layout.addLayout(footer_layout)
