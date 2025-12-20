from PySide6.QtWidgets import QWidget, QLabel, QHBoxLayout, QVBoxLayout, QPushButton, QListView, QStyledItemDelegate, QStyle
from PySide6.QtCore import Signal
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QFont
from PySide6.QtGui import QStandardItemModel, QStandardItem

from const.constant import FONT
from utils.date_converter import date_converter


class ListPage(QWidget):
    postSelected = Signal(int)
    postBtnClicked = Signal()

    def __init__(self, db):
        super().__init__()

        self.db = db
        self.list_view = QListView()
        self.model = QStandardItemModel()
        self.list_view.setModel(self.model)
        self.refresh_list()
        self.init_ui()

    def init_ui(self):
        title = QLabel("DDE 게시판")
        post_btn = QPushButton("글쓰기")
        post_btn.clicked.connect(self.create_post)

        header_layout = QHBoxLayout()
        header_layout.addWidget(title)
        header_layout.addStretch()
        header_layout.addWidget(post_btn)

        self.list_view.setItemDelegate(PostDelegate())
        self.list_view.setUniformItemSizes(True)
        self.list_view.setEditTriggers(QListView.NoEditTriggers)
        self.list_view.clicked.connect(self.open_post)

        layout = QVBoxLayout(self)
        layout.addLayout(header_layout)
        layout.addWidget(self.list_view)

    def open_post(self, index):
        post_id = index.data(Qt.UserRole)
        self.postSelected.emit(post_id)

    def create_post(self):
        self.postBtnClicked.emit()

    def refresh_list(self):
        posts = self.db.get_posts()
        self.model.clear()

        for row in posts:
            item = QStandardItem(row["title"])
            item.setData(row["id"], Qt.UserRole)
            item.setData(row["author"], Qt.UserRole + 1)
            item.setData(date_converter(row["created_at"]), Qt.UserRole + 2)

            self.model.appendRow(item)
