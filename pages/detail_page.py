from PySide6.QtWidgets import QWidget, QLabel, QHBoxLayout, QVBoxLayout, QTextBrowser, QPushButton
from PySide6.QtGui import QFont

from const.constant import FONT


class DetailPage(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def load(self, post_id):
        print("글 로딩:", post_id)

    def init_ui(self):
        self.back_btn = QPushButton("목록")
        self.edit_btn = QPushButton("수정")
        self.delete_btn = QPushButton("삭제")

        title = QLabel("제목")
        title.setFont(QFont(FONT, 11, QFont.Bold))
        author = QLabel("작성자")
        date = QLabel("작성일")
        date.setStyleSheet("color: #777;")
        updated_date = QLabel("수정일") # 수정한 경우 표시
        updated_date.setStyleSheet("color: #777;")
        content = QTextBrowser()
        content.setAcceptRichText(True)
        content.setText("내용입니다.내용입니다.내용입니다.내용입니다.내용입니다.")

        header_layout = QHBoxLayout()
        header_layout.addWidget(self.back_btn)
        header_layout.addStretch()
        header_layout.addWidget(self.edit_btn)
        header_layout.addWidget(self.delete_btn)

        date_layout = QHBoxLayout()
        date_layout.addWidget(date)
        date_layout.addWidget(updated_date)

        layout = QVBoxLayout(self)
        layout.addLayout(header_layout)
        layout.addWidget(title)
        layout.addWidget(author)
        layout.addLayout(date_layout)
        layout.addWidget(content)