from PySide6.QtCore import Signal
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (QHBoxLayout, QLabel, QMessageBox, QPushButton,
                               QTextBrowser, QVBoxLayout, QWidget)

from const.constant import FONT, Message
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
        back_btn = QPushButton("목록")
        back_btn.clicked.connect(self.backBtnClicked.emit)
        edit_btn = QPushButton("수정")
        edit_btn.clicked.connect(self.on_edit_clicked)
        delete_btn = QPushButton("삭제")
        delete_btn.clicked.connect(self.on_delete_clicked)

        self.title_label = QLabel()
        self.title_label.setFont(QFont(FONT, 11, QFont.Bold))
        self.author_label = QLabel()
        self.date_label = QLabel()
        self.date_label.setStyleSheet("color: #777;")
        self.updated_date_label = QLabel()
        self.updated_date_label.setStyleSheet("color: #777;")
        self.content_browser = QTextBrowser()
        self.content_browser.setAcceptRichText(True)

        header_layout = QHBoxLayout()
        header_layout.addWidget(back_btn)
        header_layout.addStretch()
        header_layout.addWidget(edit_btn)
        header_layout.addWidget(delete_btn)

        date_layout = QHBoxLayout()
        date_layout.addWidget(self.date_label)
        date_layout.addWidget(self.updated_date_label)

        layout = QVBoxLayout(self)
        layout.addLayout(header_layout)
        layout.addWidget(self.title_label)
        layout.addWidget(self.author_label)
        layout.addLayout(date_layout)
        layout.addWidget(self.content_browser)

    def set_init_data(self):
        if self.post:
            self.title_label.setText(self.post.title)
            self.author_label.setText(self.post.author)
            self.date_label.setText(f"작성일: {date_converter(self.post.created_at)}")
            self.content_browser.setText(self.post.content)

            if self.post.updated_at is not None:
                self.updated_date_label.setText(f"수정일: {date_converter(self.post.updated_at)}")
                self.updated_date_label.show()
            else:
                self.updated_date_label.hide()

    def on_edit_clicked(self):
        if not self.post:
            return

        self.editBtnClicked.emit(self.post.id)

    def on_delete_clicked(self):
        if not self.post:
            return

        reply = QMessageBox.question(self, Message.CONFIRM, Message.DELETE_CONFIRM,
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.db.delete_post(self.post.id)
            self.postDeleted.emit(self.post.id)
