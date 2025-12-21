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
        app_title_label = QLabel("DDE 게시판")
        create_btn = QPushButton("글쓰기")
        create_btn.clicked.connect(self.on_create_clicked)

        header_layout = QHBoxLayout()
        header_layout.addWidget(app_title_label)
        header_layout.addStretch()
        header_layout.addWidget(create_btn)

        self.table_view.setShowGrid(False)

        table_header = self.table_view.horizontalHeader()
        table_header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)

        self.table_view.clicked.connect(self.on_cell_clicked)

        layout = QVBoxLayout(self)
        layout.addLayout(header_layout)
        layout.addWidget(self.table_view)

    def on_cell_clicked(self, index):
        row = index.row()
        post = self.model.posts[row]

        self.postSelected.emit(post.id)

    def on_create_clicked(self):
        self.postBtnClicked.emit()

    def set_posts(self):
        posts = self.db.get_posts()

        self.model.refresh(posts)
