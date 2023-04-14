import sqlite3
import random
from flask import Flask, render_template

app = Flask(__name__)


def get_random_quote():
    conn = sqlite3.connect('quotes.db')
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM quotes')
    total_quotes = cursor.fetchone()[0]
    random_id = random.randint(1, total_quotes)
    cursor.execute('SELECT quote FROM quotes WHERE id=?', (random_id,))
    quote = cursor.fetchone()[0]
    conn.close()
    return quote


@app.route('/')
def home():
    return "Hello, World!"


@app.route('/random_quote')
def random_quote():
    quote = get_random_quote()
    return render_template('quote.html', quotes=quote)


if __name__ == "__main__":
    app.run(debug=True)


