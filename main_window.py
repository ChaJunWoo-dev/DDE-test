from PySide6.QtWidgets import QWidget, QStackedWidget, QVBoxLayout

from pages.detail_page import DetailPage
from pages.list_page import ListPage


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.stack = QStackedWidget()

        self.list_page = ListPage()
        self.detail_page = DetailPage(self.stack, self.list_page)

        self.list_page.postSelected.connect(self.show_detail)

        self.stack.addWidget(self.list_page)
        self.stack.addWidget(self.detail_page)

        layout = QVBoxLayout(self)
        layout.addWidget(self.stack)

        self.stack.setCurrentWidget(self.list_page)

    def show_detail(self, post_id):
        self.detail_page.load(post_id)
        self.stack.setCurrentWidget(self.detail_page)
