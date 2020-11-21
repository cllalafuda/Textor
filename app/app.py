import sys

from PyQt5.QtWidgets import QApplication, QWidget
from app.ui import Ui_Generator

from .generator import generate_lyrics
from .db import Database


class MainWindow(QWidget, Ui_Generator):
    def __init__(self):
        self.database = Database()
        self.templates = []
        super(MainWindow, self).__init__()
        super(MainWindow, self).setupUi(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Generator")

        self.generate_button.clicked.connect(self.generate_lyrics)
        self.save_results_button.clicked.connect(self.save_result)
        self.add_template_button.clicked.connect(self.add_template)
        self.remove_template_button.clicked.connect(self.remove_template)
        self.templates_combo_box.addItems(self.database.get_all_templates_names())

    def save_result(self):
        self.database.save_lyrics(self.text_browser.toPlainText())

    def generate_lyrics(self):
        is_song = bool(self.generate_song_checkbox.checkState())
        templates = [
            str(self.selected_templates_list_view.item(i).text())
            for i in range(self.selected_templates_list_view.count())
        ]
        lyrics = generate_lyrics(is_song, templates, self.database)
        self.text_browser.setText(lyrics)

    def add_template(self):
        template = self.templates_combo_box.currentText()
        if template not in self.templates:
            self.templates.append(template)
            self.selected_templates_list_view.addItem(template)

    def remove_template(self):
        template = self.templates_combo_box.currentText()
        if template in self.templates:
            self.templates.remove(template)
            self.selected_templates_list_view.clear()
            self.selected_templates_list_view.addItems(self.templates)


def run():
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())
