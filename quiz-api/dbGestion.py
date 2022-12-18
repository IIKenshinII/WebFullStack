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


def get_question(id):
    conn=create_connection()
    cur = conn.cursor()
    cur.execute("begin")
    get_question = ''' SELECT position,title,image,text,id FROM Question WHERE id=? '''
    get_answers=''' SELECT idQuestion,text,isCorrect,id FROM Answer WHERE idQuestion=? ORDER BY ROWID '''
    id_data=(id,)
    try:
        cur.execute(get_question, id_data)
        rowsQuestion=cur.fetchall()
        cur.execute(get_answers, id_data)
        rowsAnswer=cur.fetchall()
        cur.close()
        conn.close()
        if len(rowsQuestion)==0 or len(rowsAnswer)==0:
            return "get question failed"
        q=None
        for row in rowsQuestion:
            q=Question(row[0],row[1],row[2],row[3],row[4],rowsAnswer)
        return q
    except Error as e:
        conn.rollback()
        cur.close()
        conn.close()
        return "get question failed"