import sqlite3
def is_palindrome(s):
   return s == s[::-1]

def sort_list(numbers):
   return sorted(numbers)

def init_db():
   conn = sqlite3.connect(':memory:')
   cur = conn.cursor()
   cur.execute('''
      CREATE TABLE IF NOT EXISTS user
      (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)
   ''')
   conn.commit()
   return conn

def add_user(conn, name, age):
   cur = conn.cursor()
   cur.execute('INSERT INTO user(name, age) VALUES(?, ?)', (name, age))
   conn.commit()

def get_user(conn, name):
   cur = conn.cursor()
   cur.execute('SELECT * FROM user WHERE name = ?', (name,))
   return cur.fetchone()