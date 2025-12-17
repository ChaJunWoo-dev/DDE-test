from PySide6.QtWidgets import QWidget, QLabel, QHBoxLayout, QVBoxLayout

class DetailPage(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def load(self, post_id):
        print("글 로딩:", post_id)

    def init_ui(self):
        test_label = QLabel("상세페이지")

        layout = QVBoxLayout(self)
        layout.addWidget(test_label)