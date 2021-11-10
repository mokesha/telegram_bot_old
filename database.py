import button
import sqlite3
import variable


# Withdrawal exam
def performers(call):
    conn = sqlite3.connect('button_user.db')
    with conn:
        cur = conn.cursor()
    cur.execute(f"SELECT * FROM button_user WHERE {variable.x} == 1")
    rows = cur.fetchall()
    i = 0
    variable.list_people = {}
    for row in rows:
        variable.list_people['var{}'.format(i)] = row[1]
        i += 1
    conn.commit()
    cur.close()
    button.list_of_performer_right(call)
    return variable.list_people


# Withdrawal exam
def performers_2(call):
    conn = sqlite3.connect('button_user.db')
    with conn:
        cur = conn.cursor()
    cur.execute(f"SELECT * FROM button_user WHERE {variable.x} == 1")
    rows = cur.fetchall()
    i = 0
    variable.list_people_2 = {}
    for row in rows:
        variable.list_people_2['var{}'.format(i)] = row[1]
        i += 1
    conn.commit()
    cur.close()
    button.list_of_performer_left(call)
    return variable.list_people_2
