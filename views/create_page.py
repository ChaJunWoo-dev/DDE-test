from PySide6.QtCore import Signal
from PySide6.QtWidgets import QHBoxLayout, QLineEdit, QMessageBox, QVBoxLayout

from const.constant import Message
from utils.validator import validate_post_input
from views.base_form_page import BaseFormPage


class CreatePage(BaseFormPage):
    cancelBtnClicked = Signal()
    saveBtnClicked = Signal(int)

    def __init__(self, db):
        super().__init__(db)

    def init_specific_ui(self):
        self.author_edit = QLineEdit()

        self.author_edit.setPlaceholderText(Message.AUTHOR_REQUIRED)
        self.title_edit.setPlaceholderText(Message.TITLE_REQUIRED)
        self.content_edit.setPlaceholderText(Message.CONTENT_REQUIRED)

        footer_layout = QHBoxLayout()
        footer_layout.addStretch()
        footer_layout.addWidget(self.cancel_btn)
        footer_layout.addWidget(self.save_btn)

        layout = QVBoxLayout(self)
        layout.addWidget(self.title_edit)
        layout.addWidget(self.author_edit)
        layout.addWidget(self.content_edit)
        layout.addLayout(footer_layout)

    def on_cancel(self):
        self.cancelBtnClicked.emit()
        self.clear_editor()

    def on_save(self):
        title = self.title_edit.text()
        content = self.content_edit.toPlainText()
        author = self.author_edit.text()

        error_message = validate_post_input(title, content, author)
        if error_message:
            QMessageBox.warning(self, Message.ERROR, error_message)
            return

        post_id = self.db.create_post(title, content, author)

        self.saveBtnClicked.emit(post_id)
        self.clear_editor()

    def clear_editor(self):
        self.title_edit.clear()
        self.author_edit.clear()
        self.content_edit.clear()
