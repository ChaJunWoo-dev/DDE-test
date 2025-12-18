from PySide6.QtWidgets import QWidget, QStackedWidget, QVBoxLayout

from pages.create_page import CreatePage
from pages.detail_page import DetailPage
from pages.edit_page import EditPage
from pages.list_page import ListPage


class MainWindow(QWidget):
    def __init__(self, db):
        super().__init__()

        self.db = db
        self.stack = QStackedWidget()

        self.list_page = ListPage(db)
        self.detail_page = DetailPage(db)
        self.create_page = CreatePage(db)
        self.edit_page = EditPage(db)

        for page in [self.detail_page, self.create_page]:
            page.backBtnClicked.connect(self.show_list)

        self.list_page.postSelected.connect(self.show_detail)
        self.list_page.postBtnClicked.connect(self.show_create)
        self.detail_page.editBtnClicked.connect(self.show_edit)
        self.detail_page.postDeleted.connect(self.update_post_list)
        self.detail_page.postDeleted.connect(self.show_list)
        self.edit_page.doneClicked.connect(self.show_detail)
        self.edit_page.postChanged.connect(self.update_post_list)

        self.stack.addWidget(self.list_page)
        self.stack.addWidget(self.detail_page)
        self.stack.addWidget(self.create_page)
        self.stack.addWidget(self.edit_page)

        layout = QVBoxLayout(self)
        layout.addWidget(self.stack)

        self.stack.setCurrentWidget(self.list_page)

    def show_detail(self, post_id):
        self.detail_page.load(post_id)
        self.stack.setCurrentWidget(self.detail_page)

    def show_list(self):
        self.stack.setCurrentWidget(self.list_page)

    def show_create(self):
        self.stack.setCurrentWidget(self.create_page)

    def show_edit(self, post_id):
        self.edit_page.load(post_id)
        self.stack.setCurrentWidget(self.edit_page)

    def update_post_list(self):
        self.list_page.refresh_list()
