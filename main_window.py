from PySide6.QtWidgets import QMessageBox, QStackedWidget, QVBoxLayout, QWidget

from views.create_page import CreatePage
from views.detail_page import DetailPage
from views.edit_page import EditPage
from views.list_page import ListPage


class MainWindow(QWidget):
    def __init__(self, db):
        super().__init__()

        self.db = db
        self.stack = QStackedWidget()

        self.list_page = ListPage(db)
        self.detail_page = DetailPage(db)
        self.create_page = CreatePage(db)
        self.edit_page = EditPage(db)

        self.list_page.postSelected.connect(self.show_detail)
        self.list_page.postBtnClicked.connect(self.show_create)

        self.detail_page.editBtnClicked.connect(self.show_edit)
        self.detail_page.postDeleted.connect(self.update_post_list)
        self.detail_page.postDeleted.connect(self.show_list)
        self.detail_page.backBtnClicked.connect(self.show_list)

        self.edit_page.saveBtnClicked.connect(self.update_post_list)
        self.edit_page.saveBtnClicked.connect(self.show_detail)
        self.edit_page.cancelBtnClicked.connect(self.show_detail)
        self.edit_page.loadFailed.connect(self.show_list)

        self.create_page.saveBtnClicked.connect(self.update_post_list)
        self.create_page.saveBtnClicked.connect(self.show_detail)
        self.create_page.cancelBtnClicked.connect(self.show_list)

        self.stack.addWidget(self.list_page)
        self.stack.addWidget(self.detail_page)
        self.stack.addWidget(self.create_page)
        self.stack.addWidget(self.edit_page)

        layout = QVBoxLayout(self)
        layout.addWidget(self.stack)

        self.stack.setCurrentWidget(self.list_page)

    def show_list(self):
        self.stack.setCurrentWidget(self.list_page)

    def show_create(self):
        self.stack.setCurrentWidget(self.create_page)

    def show_edit(self, post_id):
        if not self.edit_page.load(post_id):
            QMessageBox.warning(self, "오류", "게시글을 찾을 수 없습니다.")
            self.show_list()
            return

        self.stack.setCurrentWidget(self.edit_page)

    def show_detail(self, post_id):
        if not self.detail_page.load(post_id):
            QMessageBox.warning(self, "오류", "게시글을 찾을 수 없습니다.")
            self.show_list()
            return

        self.stack.setCurrentWidget(self.detail_page)

    def update_post_list(self):
        self.list_page.set_posts()
