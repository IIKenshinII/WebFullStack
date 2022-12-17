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
        return "Database connexion error"

    return conn

def insert_question(question):
    conn=create_connection()
    cur = conn.cursor()
    cur.execute("begin")
    insert_to_question = ''' INSERT INTO Question(position,title,image,text) VALUES(?,?,?,?) '''
    data_insert=(getattr(question,'position'),getattr(question,'title'),getattr(question,'image'),getattr(question,'text'))
    try:
        cur.execute(insert_to_question, data_insert)
    except Error as e:
        conn.rollback()
        return "insert question failed"
    id=cur.lastrowid
    result_answer_insert=insert_answer(question,cur,id)
    if result_answer_insert!="insert answer failed":
        conn.commit()
    else:
        conn.rollback()
        cur.close()
        conn.close()
        return result_answer_insert
    cur.close()
    conn.close()
    return id

def insert_answer(question,cur,id):
    insert_to_answer = ''' INSERT INTO Answer(text,isCorrect,idQuestion) VALUES(?,?,?) '''
    answers=getattr(question,'possibleAnswers')
    ansList=[]
    test=1
    for answer in answers:
        data_insert=(getattr(answer,'text'),getattr(answer,'isCorrect'),id)
        ansList.append(data_insert)
    try:
        cur.executemany(insert_to_answer,ansList)
        setattr(answer,'idQuestion',id)
    except Error as e:
            return "insert answer failed"
    return cur.lastrowid