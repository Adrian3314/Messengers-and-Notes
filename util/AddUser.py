import sqlite3
from datetime import datetime

predefineUser = [
    (1, 'user1', '123'),
    (2, 'user2', '123'),
    (3, 'user3', '123'),
    (4, 'user4', '123'),
    (5, 'user5', '123')
]

predefineRoom = [
    (1, 1, 2)
]

predefineMessage = [
    # (1, datetime(???), "Hi"), 
    (1, datetime(), "Hello"),
    (1, datetime(), "Hey")
]

if __name__ == "__main__":
    db = sqlite3.connect('MessengerAndNotes.db')
    cursor = db.cursor()
    cursor.executemany("INSERT INTO user VALUES(?, ?, ?)", predefineUser)
    cursor.executemany("INSERT INTO room VALUES(?, ?, ?)", predefineRoom)
    cursor.executemany("INSERT INTO message VALUES(?, ?, ?)", predefineMessage)
    db.commit()