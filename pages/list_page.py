from PySide6.QtWidgets import QWidget, QLabel, QHBoxLayout, QVBoxLayout, QPushButton, QListView, QStyledItemDelegate, QStyle
from PySide6.QtCore import Signal
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QFont
from PySide6.QtGui import QStandardItemModel, QStandardItem

from const.constant import FONT

posts = [
    ["글 제목 1", "홍길동", "2025-12-17"],
    ["글 제목 2", "김철수", "2025-12-16"],
    ["글 제목 3", "이영희", "2025-12-15"],
    ["글 제목 4", "박영수", "2025-12-14"],
    ["글 제목 5", "홍길동", "2025-12-14"],
    ["글 제목 6", "김철수", "2025-12-13"],
    ["글 제목 7", "이영희", "2025-12-13"],
    ["글 제목 8", "박영수", "2025-12-13"],
    ["글 제목 9", "박영수", "2025-12-13"],
    ["글 제목 10", "박영수", "2025-12-13"],
    ["글 제목 11", "박영수", "2025-12-13"],
]

class ListPage(QWidget):
    postSelected = Signal(int)
    postBtnClicked = Signal()

    def __init__(self):
        super().__init__()
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

        for title, author, created_at in posts:
            item = QStandardItem(title)
            item.setData(author, Qt.UserRole)
            item.setData(created_at, Qt.UserRole + 1)

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
