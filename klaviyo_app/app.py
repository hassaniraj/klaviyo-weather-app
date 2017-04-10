import sqlite3
import logging

from __init__ import cursor, setup_logging, conn
from flask import Flask, render_template, request
import cities

logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route('/', methods=['GET'])
def api_welcome():
    try:
        return render_template('index.html', cities=[c[1] for c in cities.cities])
    except Exception as e:
        return render_template('500.html', error=str(e))


@app.route('/subscribe', methods=['POST'])
def api_subscribe():
    try:
        email = request.form.get('email')
        location = request.form.get('location')
        msg = _add_user(email, location)
        return render_template('index.html', cities=[c[1] for c in cities.cities], message=msg, backgroundColor='rgba(0,128,0,0.2)')
    except Exception as e:
        return render_template('500.html', error=str(e))

@app.errorhandler(404)
def page_not_found():
    return render_template("404.html")


def _add_user(email, location):
    try:
        cursor.execute('''INSERT INTO subscribers(email, city)
                  VALUES(?,?)''', (email, location))
        logger.debug('User %s added', email)
        conn.commit()
    except sqlite3.IntegrityError as er:
        return "User already exists"
    return "User Added"

if __name__ == '__main__':
    setup_logging()
    app.run(debug=True)