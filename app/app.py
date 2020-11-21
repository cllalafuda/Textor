import sys

from PyQt5.QtWidgets import QApplication, QWidget
from ui import Ui_Generator

from utils import generate_lyrics


class MainWindow(QWidget, Ui_Generator):
    def __init__(self):
        super(MainWindow, self).__init__()
        super(MainWindow, self).setupUi(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Generator")

        # UI elements bindings
        self.generate_button.clicked.connect(self.generate_lyrics)
        self.save_results_button.clicked.connect(self.save_result)
        self.add_template_button.clicked.connect(self.add_template)
        self.remove_template_button.clicked.connect(self.remove_template)

    def save_result(self):
        pass

    def generate_lyrics(self):
        lyrics = generate_lyrics()
        self.text_browser.setText(lyrics)

    def add_template(self):
        pass

    def remove_template(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())
