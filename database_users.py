import telebot
import button_users
import main_users
import sqlite3
import variable_users

bot = telebot.TeleBot(main_users.TOKEN)

userid = 0


# First user data
@bot.message_handler(func=lambda message: True)
def start_button_database(message):
    conn = sqlite3.connect('button_user.db')
    with conn:
        cur = conn.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS button_user(
        userid INT PRIMARY KEY,
        name TEXT,
        math BOOLEAN,
        fiz BOOLEAN,
        rus BOOLEAN)
    """)

    # Filling a database row for the first time
    global userid
    userid = message.chat.id
    name = message.text
    math = 0
    fiz = 0
    rus = 0

    cur.execute(f"INSERT OR IGNORE INTO 'button_user' VALUES ('{userid}','{name}','{math}', '{fiz}', '{rus}')")
    cur.execute(f"UPDATE button_user SET name = '{name}' WHERE userid = {message.chat.id}")

    cur.execute("SELECT * FROM button_user")
    rows = cur.fetchall()
    for row in rows:
        print(row[0], row[1], row[2], row[3], row[4])

    conn.commit()
    cur.close()
    button_users.reg_button1(message)


# Change boolean math
@bot.message_handler(func=lambda message: True)
def math_logic_subject(message):
    conn = sqlite3.connect('button_user.db')
    with conn:
        subject = 'math'
        cur = conn.cursor()
        cur.execute(f"SELECT `{subject}` FROM button_user WHERE userid = {message.chat.id}")
        if cur.fetchall() == [(0,)]:
            cur.execute(f"UPDATE button_user SET {subject} = 1 WHERE {subject} = 0 AND userid = {message.chat.id}")
            variable_users.math = variable_users.space_mark + 'Математика'
        else:
            cur.execute(f"UPDATE button_user SET {subject} = 0 WHERE {subject} = 1 AND userid = {message.chat.id}")
            variable_users.math = variable_users.check_mark + 'Математика'
    conn.commit()
    cur.close()
    return variable_users.math


# Change boolean physics
@bot.message_handler(func=lambda message: True)
def fiz_logic_subject(message):
    conn = sqlite3.connect('button_user.db')
    with conn:
        subject = 'fiz'
        cur = conn.cursor()
        cur.execute(f"SELECT `{subject}` FROM button_user WHERE userid = {message.chat.id}")
        if cur.fetchall() == [(0,)]:
            cur.execute(f"UPDATE button_user set {subject} = 1 WHERE {subject} = 0 AND userid = {message.chat.id}")
            variable_users.fiz = variable_users.space_mark + 'Физика'
        else:
            cur.execute(f"UPDATE button_user set {subject} = 0 WHERE {subject} = 1 AND userid = {message.chat.id}")
            variable_users.fiz = 'Физика ✅'
    conn.commit()
    cur.close()
    return variable_users.fiz


# Change boolean russian
@bot.message_handler(func=lambda message: True)
def rus_logic_subject(message):
    conn = sqlite3.connect('button_user.db')
    with conn:
        subject = variable_users.rus1
        cur = conn.cursor()
        cur.execute(f"SELECT `{subject}` FROM button_user WHERE userid = {message.chat.id}")
        if cur.fetchall() == [(0,)]:
            cur.execute(f"UPDATE button_user set {subject} = 1 WHERE {subject} = 0 AND userid = {message.chat.id}")
            variable_users.fiz = variable_users.space_mark + 'Русский'
        else:
            cur.execute(f"UPDATE button_user set {subject} = 0 WHERE {subject} = 1 AND userid = {message.chat.id}")
            variable_users.fiz = 'Русский ✅'
    conn.commit()
    cur.close()
    return variable_users.rus
