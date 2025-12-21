from PySide6.QtCore import Signal
from PySide6.QtWidgets import (QHBoxLayout, QHeaderView, QLabel, QPushButton,
                               QTableView, QVBoxLayout, QWidget)

from models.post_table_model import PostTableModel


class ListPage(QWidget):
    postSelected = Signal(int)
    postBtnClicked = Signal()

    def __init__(self, db):
        super().__init__()

        self.db = db
        self.model = PostTableModel()
        self.set_posts()
        self.table_view = QTableView()
        self.table_view.setModel(self.model)
        self.init_ui()

    def init_ui(self):
        title = QLabel("DDE 게시판")
        post_btn = QPushButton("글쓰기")
        post_btn.clicked.connect(self.create_post)

        header_layout = QHBoxLayout()
        header_layout.addWidget(title)
        header_layout.addStretch()
        header_layout.addWidget(post_btn)

        self.table_view.setShowGrid(False)

        header = self.table_view.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)

        self.table_view.clicked.connect(self.open_post)

        layout = QVBoxLayout(self)
        layout.addLayout(header_layout)
        layout.addWidget(self.table_view)

    def open_post(self, index):
        row = index.row()
        post = self.model.posts[row]

        self.postSelected.emit(post.id)

    def create_post(self):
        self.postBtnClicked.emit()

    def set_posts(self):
        posts = self.db.get_posts()

        self.model.refresh(posts)
