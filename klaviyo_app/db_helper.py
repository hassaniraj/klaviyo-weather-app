import sqlite3

WARM_WEATHER = "It's nice out! Enjoy a discount on us."
COOL_WEATHER = "Not so nice out? That's okay, enjoy a discount on us."
AVG_WEATHER = "Enjoy a discount on us."

conn = sqlite3.connect('subsciber.db', check_same_thread=False)
cursor = conn.cursor()


def get_users():
    subscribers = dict()
    cursor.execute('''SELECT  email, city FROM subscribers''')
    all_rows = cursor.fetchall()
    for row in all_rows:
        subscribers[row[0]] = row[1]
        print('{}  {}').format(row[0], row[1])
    return subscribers
