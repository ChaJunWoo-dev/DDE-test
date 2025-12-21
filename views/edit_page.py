from PySide6.QtCore import Signal
from PySide6.QtWidgets import QHBoxLayout, QLabel, QMessageBox, QVBoxLayout

from const.constant import Message
from utils.validator import validate_post_input
from views.base_form_page import BaseFormPage


class EditPage(BaseFormPage):
    cancelBtnClicked = Signal(int)
    saveBtnClicked = Signal(int)
    loadFailed = Signal()

    def __init__(self, db):
        super().__init__(db)

        self.post = None

    def load(self, post_id):
        self.post = self.db.get_post(post_id)
        if self.post:
            self.set_init_data()

        return self.post

    def set_init_data(self):
        if self.post:
            self.title_edit.setText(self.post.title)
            self.author.setText(self.post.author)
            self.content_edit.setText(self.post.content)

    def init_specific_ui(self):
        self.author = QLabel()
        self.author.setStyleSheet("padding-left: 3px")

        footer_layout = QHBoxLayout()
        footer_layout.addStretch()
        footer_layout.addWidget(self.cancel_btn)
        footer_layout.addWidget(self.save_btn)

        layout = QVBoxLayout(self)
        layout.addWidget(self.title_edit)
        layout.addWidget(self.author)
        layout.addWidget(self.content_edit)
        layout.addLayout(footer_layout)

    def on_cancel(self):
        if self.post:
            self.cancelBtnClicked.emit(self.post.id)

    def on_save(self):
        new_title = self.title_edit.text()
        new_content = self.content_edit.toPlainText()

        error_message = validate_post_input(new_title, new_content)
        if error_message:
            QMessageBox.warning(self, Message.ERROR, error_message)
            return

        self.db.update_post(new_title, new_content, self.post.id)
        self.saveBtnClicked.emit(self.post.id)
