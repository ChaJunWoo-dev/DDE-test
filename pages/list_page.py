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
            item.setData(row["id"], Qt.UserRole)
            item.setData(row["author"], Qt.UserRole + 1)
            item.setData(date_converter(row["created_at"]), Qt.UserRole + 2)

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
        post_id = index.data(Qt.UserRole)
        self.postSelected.emit(post_id)

    def create_post(self):
        self.postBtnClicked.emit()


class PostDelegate(QStyledItemDelegate):
    def sizeHint(self, option, index):
        return QSize(option.rect.width(), 56)

    def paint(self, painter, option, index):
        painter.save()

        title = index.data(Qt.DisplayRole)
        author = index.data(Qt.UserRole + 1)
        date = index.data(Qt.UserRole + 2)

        rect = option.rect

        # 제목
        title_font = QFont(FONT)
        title_font.setPointSize(11)
        title_font.setBold(True)
        painter.setFont(title_font)
        painter.drawText(rect.adjusted(10, 5, -10, -25), title)

        #작성자, 날짜
        meta_font = QFont(FONT)
        meta_font.setPointSize(9)
        meta_font.setBold(False)
        painter.setFont(meta_font)
        painter.drawText(
            rect.adjusted(10, 30, 0, -5),  # 왼쪽 여백만
            Qt.AlignLeft | Qt.AlignVCenter,
            author
        )
        painter.drawText(
            rect.adjusted(0, 30, -10, -5),  # 오른쪽 여백만
            Qt.AlignRight | Qt.AlignVCenter,
            date
        )

        painter.restore()
