import sqlite3

def create_table():
    conn = sqlite3.connect('quotes.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS quotes (
        id INTEGER PRIMARY KEY,
        quote TEXT NOT NULL
    );
    ''')

    conn.commit()
    conn.close()

def insert_quote(quote):
    conn = sqlite3.connect('quotes.db')
    cursor = conn.cursor()

    cursor.execute('INSERT INTO quotes (quote) VALUES (?)', (quote,))

    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_table()

    quotes = [
        'Quote 1',
        'Quote 2',
        'Quote 3',
        # Add more quotes here
    ]

    for quote in quotes:
        insert_quote(quote)

    print('Database created and quotes inserted successfully.')
