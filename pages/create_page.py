from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLineEdit, QTextEdit, QPushButton


class CreatePage(QWidget):
    def __init__(self, stack, list_page):
        super().__init__()

        self.stack = stack
        self.list_page = list_page
        self.init_ui()

    def init_ui(self):
        title_edit = QLineEdit()
        title_edit.setPlaceholderText("제목을 입력하세요")
        author_edit = QLineEdit()
        author_edit.setPlaceholderText("작성자명을 입력하세요")
        content_edit = QTextEdit()
        content_edit.setPlaceholderText("내용을 입력하세요.")

        self.cancel_btn = QPushButton("취소")
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

    def cancel_post(self):
        self.stack.setCurrentWidget(self.list_page)
