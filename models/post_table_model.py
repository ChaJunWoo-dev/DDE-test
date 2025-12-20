from datetime import datetime

from PySide6.QtCore import QAbstractTableModel, QModelIndex, Qt

from utils.date_converter import date_converter

class PostTableModel(QAbstractTableModel):
    def __init__(self):
        super().__init__()
        self.posts = None
        self.column_count = 3
        self.row_count = 15

    def rowCount(self, parent=QModelIndex()):
        return len(self. posts)

    def columnCount(self, parent=QModelIndex()):
        return self.column_count

    def headerData(self, section, orientation, role):
        if role != Qt.ItemDataRole.DisplayRole:
            return None

        if orientation == Qt.Orientation.Horizontal:
            headers = ["제목", "작성자", "작성일"]

            return headers[section]

        return None

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if not index.isValid():
            return None

        if index.row() >= len(self.posts) or index.row() < 0:
            return None

        if role == Qt.ItemDataRole.DisplayRole:
            post = self.posts[index.row()]
            col = index.column()

            if col == 0:
                return post.title
            elif col == 1:
                return post.author
            elif col == 2:
                date = date_converter(post.created_at)

                if not self.isToday(date):
                    return date.split(" ")[0]
                else:
                    return date.split(" ")[1]

        return None

    def isToday(self, date):
        date_str = date.split(" ")[0]
        today = datetime.now().strftime("%Y-%m-%d")

        return date_str == today

    def refresh(self, new_posts):
        self.beginResetModel()
        self.posts = new_posts
        print(new_posts)
        self.endResetModel()