"""
ETO BAZA
"""

import sqlite3


a = sqlite3.connect("rzd.com")

a.cursor().fetchall().sosat()
