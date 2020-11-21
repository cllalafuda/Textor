import sys

from PyQt5.QtWidgets import QApplication, QWidget
from app.ui import Ui_Generator
from app.favourites_widget_ui import Ui_Favourites

from .generator import generate_lyrics
from .db import Database


class MainWindow(QWidget, Ui_Generator):
    def __init__(self):
        super(MainWindow, self).__init__()
        super(MainWindow, self).setupUi(self)

        self.database = Database()
        self.favourites = FavouritesLyricsWidget(self.database)
        self.templates = []
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Generator")

        self.generate_button.clicked.connect(self.generate_lyrics)
        self.save_results_button.clicked.connect(self.save_result)
        self.add_template_button.clicked.connect(self.add_template)
        self.remove_template_button.clicked.connect(self.remove_template)
        self.templates_combo_box.addItems(self.database.get_all_templates_names())
        self.show_favourites_button.clicked.connect(self.show_favourites)

    def show_favourites(self):
        self.favourites.show()

    def save_result(self):
        self.database.save_lyrics(self.text_browser.toPlainText())
        self.favourites.update_combo_box()

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


class FavouritesLyricsWidget(QWidget, Ui_Favourites):
    def __init__(self, database):
        super(FavouritesLyricsWidget, self).__init__()
        super(FavouritesLyricsWidget, self).setupUi(self)
        self.data_storage = None
        self.database = database
        self.mapping = {}
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Favourites")
        self.remove_button.clicked.connect(self.remove_lyrics)
        self.show_button.clicked.connect(self.show_lyrics)
        self.update_combo_box()

    def show_lyrics(self):
        header = self.favourite_lyrics_combo_box.currentText()
        id_unique = int(header.split("~")[-1])

        for id, text in self.data_storage:
            if id == id_unique:
                self.textBrowser.setText(text)

    def update_combo_box(self):
        self.favourite_lyrics_combo_box.addItems(self._get_headers_for_lyrics())

    def _get_headers_for_lyrics(self) -> list:
        data = self.database.get_favourite_lyrics()
        self.data_storage = data
        headers = []
        for id, text in data:
            header = text[:20] + f"... ~{id}"
            headers.append(header)
        return headers

    def remove_lyrics(self):
        header = self.favourite_lyrics_combo_box.currentText()
        id_unique = int(header.split("~")[-1])
        self.database.delete_lyrics(id_unique)
        self.favourite_lyrics_combo_box.clear()
        self.data_storage = self.database.get_favourite_lyrics()
        self.update_combo_box()


def run():
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())
