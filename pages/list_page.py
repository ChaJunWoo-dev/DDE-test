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
        self.posts = self.db.get_posts()
        print(self.posts)
        self.init_ui()

    def init_ui(self):
        title = QLabel("DDE 게시판")
        post_btn = QPushButton("글쓰기")
        post_btn.clicked.connect(self.create_post)

        header_layout = QHBoxLayout()
        header_layout.addWidget(title)
        header_layout.addStretch()
        header_layout.addWidget(post_btn)

        list_view = QListView()
        model = QStandardItemModel()

        for row in self.posts:
            item = QStandardItem(row["title"])
            item.setData(row["author"], Qt.UserRole)
            item.setData(date_converter(row["created_at"]), Qt.UserRole + 1)

            model.appendRow(item)

        list_view.setModel(model)
        list_view.setItemDelegate(PostDelegate())
        list_view.setUniformItemSizes(True)
        list_view.setEditTriggers(QListView.NoEditTriggers)

        list_view.clicked.connect(self.open_post)

        layout = QVBoxLayout(self)
        layout.addLayout(header_layout)
        layout.addWidget(list_view)

    def open_post(self, index):
        post_id = index.row()
        self.postSelected.emit(post_id)

    def create_post(self):
        self.postBtnClicked.emit()


class PostDelegate(QStyledItemDelegate):
    def sizeHint(self, option, index):
        return QSize(option.rect.width(), 56)

    def paint(self, painter, option, index):
        painter.save()

        title = index.data(Qt.DisplayRole)
        author = index.data(Qt.UserRole)
        date = index.data(Qt.UserRole + 1)

        rect = option.rect

        # 제목
        painter.setFont(QFont(FONT, 11, QFont.Bold))
        painter.drawText(rect.adjusted(10, 5, -10, -25), title)

        # 작성자 · 날짜
        painter.setFont(QFont(FONT, 9))
        painter.drawText(
            rect.adjusted(10, 30, -10, -5),
            f"{author} · {date}"
        )

        painter.restore()
