import sqlite3
from sqlite3 import IntegrityError


class Database:
    def __init__(self):
        self.connection = sqlite3.connect("database/database.db")
        self.cursor = self.connection.cursor()

    def get_all_templates_names(self) -> list:
        templates = self.cursor.execute("SELECT name FROM text;").fetchall()
        result = [i[0] for i in templates]
        return result

    def save_lyrics(self, text):
        try:
            self.cursor.execute("INSERT INTO SavedText (name) VALUES(?)", (text, )).fetchall()
        except IntegrityError:
            pass

        self.connection.commit()

    def delete_lyrics(self, id):
        self.cursor.execute("DELETE FROM SavedText WHERE id = ?;", (id, ))

    def get_data_for_generating(self, name) -> str:
        data = self.cursor.execute("SELECT data FROM text WHERE name = ?", (name,)).fetchall()
        result = data[0][0]
        return result
