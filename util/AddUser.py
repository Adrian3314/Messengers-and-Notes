import sqlite3

predefine = [

]

if __name__ == "__main__":
    db = sqlite3.connect('MessengerAndNotes.db')
    cursor = db.cursor()
    cursor.executemany("INSERT INTO courses VALUES(?, ?, ?)", predefine)
    db.commit()