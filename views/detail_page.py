from PySide6.QtCore import Signal
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (QHBoxLayout, QLabel, QMessageBox, QPushButton,
                               QTextBrowser, QVBoxLayout, QWidget)

from const.constant import FONT
from utils.date_converter import date_converter


class DetailPage(QWidget):
    backBtnClicked = Signal()
    editBtnClicked = Signal(int)
    postDeleted = Signal(int)

    def __init__(self, db):
        super().__init__()

        self.db = db
        self.post = None
        self.init_ui()

    def load(self, post_id):
        self.post = self.db.get_post(post_id)
        if self.post:
            self.set_init_data()

        return self.post

    def init_ui(self):
        self.back_btn = QPushButton("목록")
        self.back_btn.clicked.connect(self.backBtnClicked.emit)
        self.edit_btn = QPushButton("수정")
        self.edit_btn.clicked.connect(self.on_edit_clicked)
        self.delete_btn = QPushButton("삭제")
        self.delete_btn.clicked.connect(self.on_delete_clicked)

        self.title = QLabel()
        self.title.setFont(QFont(FONT, 11, QFont.Bold))
        self.author = QLabel()
        self.date = QLabel()
        self.date.setStyleSheet("color: #777;")
        self.updated_date = QLabel()
        self.updated_date.setStyleSheet("color: #777;")
        self.content = QTextBrowser()
        self.content.setAcceptRichText(True)

        header_layout = QHBoxLayout()
        header_layout.addWidget(self.back_btn)
        header_layout.addStretch()
        header_layout.addWidget(self.edit_btn)
        header_layout.addWidget(self.delete_btn)

        date_layout = QHBoxLayout()
        date_layout.addWidget(self.date)
        date_layout.addWidget(self.updated_date)

        layout = QVBoxLayout(self)
        layout.addLayout(header_layout)
        layout.addWidget(self.title)
        layout.addWidget(self.author)
        layout.addLayout(date_layout)
        layout.addWidget(self.content)

    def set_init_data(self):
        if self.post:
            self.title.setText(self.post.title)
            self.author.setText(self.post.author)
            self.date.setText(f"작성일: {date_converter(self.post.created_at)}")
            self.content.setText(self.post.content)

            if self.post.updated_at is not None:
                self.updated_date.setText(f"수정일: {date_converter(self.post.updated_at)}")
                self.updated_date.show()
            else:
                self.updated_date.hide()

    def on_edit_clicked(self):
        if not self.post:
            return

        self.editBtnClicked.emit(self.post.id)

    def on_delete_clicked(self):
        if not self.post:
            return

        reply = QMessageBox.question(self, '삭제 확인', '정말 삭제하시겠습니까?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.db.delete_post(self.post.id)
            self.postDeleted.emit(self.post.id)
