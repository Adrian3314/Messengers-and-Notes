import sqlite3
from datetime import datetime

predefineUser = [
    (1, 'user1', '123'),
    (2, 'user2', '123')
]

predefineRoom = [
    (1, 1, 2)
]

predefineMessage = [
    (1, datetime)
]

if __name__ == "__main__":
    db = sqlite3.connect('MessengerAndNotes.db')
    cursor = db.cursor()
    cursor.executemany("INSERT INTO user VALUES(?, ?, ?)", predefine)
    db.commit()