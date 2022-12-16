import sqlite3
from sqlite3 import Error
from question import *


def create_connection():
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    path='quiz-bdd.db'
    try:
        # create a connection
        conn = sqlite3.connect(path)
        # set the sqlite connection in "manual transaction mode"
        # (by default, all execute calls are performed in their own transactions, not what we want)
        conn.isolation_level = None
    except Error as e:
        print(e)

    return conn

def insert_question(question):
    conn=create_connection()
    if conn is None:
        return "Database connexion error"
    cur = conn.cursor()
    cur.execute("begin")
    insert_to_question = ''' INSERT INTO Question(position,title,image,text)
              VALUES(?,?,?,?) '''
    insert_to_answer = ''' INSERT INTO Answer(texte,isCorrect,idQuestion)
              VALUES(?,?,?) '''
    data_insert=(getattr(question,'position'),getattr(question,'title'),getattr(question,'image'),getattr(question,'text'))
    try:
        cur.execute(insert_to_question, data_insert)
    except Error as e:
        cur.execute('rollback')
        return "insert failed"
    cur.execute("commit")
    cur.close()
    return cur.lastrowid