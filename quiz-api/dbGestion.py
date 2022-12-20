import sqlite3
from sqlite3 import Error
from question import *
from participation import *


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

def update_question(question):
    conn=create_connection()
    cur = conn.cursor()
    cur.execute("begin")
    update_q = ''' UPDATE Question SET text=?, position=?, title=?,image=? WHERE id=? '''
    q_data=(getattr(question,'text'),getattr(question,'position'),getattr(question,'title'),getattr(question,'image'),getattr(question,'id'))
    if len(getattr(question,'possibleAnswers'))>0:
        if delete_answer(cur,getattr(question,'id')) :
            if type(insert_answer(question,cur,getattr(question,'id')))==str:
                cur.close()
                conn.close()
                return "update question failed"
        else:
            cur.close()
            conn.close()
            return "update question failed"
    try:
        cur.execute(update_q,q_data)
        conn.commit()
        cur.close()
        conn.close()
        return "update successfull"
    except Error as e:
        conn.rollback()
        cur.close()
        conn.close()
        return "update failed"

def delete_answer(cur,id):
    delete_ans = ''' DELETE FROM Answer WHERE idQuestion=?'''
    data_id=(id,)
    try:
        cur.execute(delete_ans,data_id)
        return True
    except Error as e:
            return False

def delete_question(id):
    conn=create_connection()
    cur = conn.cursor()
    cur.execute("begin")
    delete_q = ''' DELETE FROM Question WHERE id=?'''
    data_id=(id,)
    if type(get_question(id))==str:
         cur.close()
         conn.close()
         return "failed deleting question"
    try:
        cur.execute(delete_q,data_id)
        if not delete_answer(cur,id):
            cur.close()
            conn.close()
            return "failed deleting question"
        conn.commit()
        cur.close()
        conn.close()
    except Error as e:
            cur.close()
            conn.close()
            return "error while deleting question"

def delete_all_questions():
    conn=create_connection()
    cur = conn.cursor()
    cur.execute("begin")
    delete_q = ''' DELETE FROM Question'''
    delete_a = ''' DELETE FROM Answer'''
    result=1
    try:
        cur.execute(delete_q)
        cur.execute(delete_a)
        conn.commit()
    except Error as e:
        result="failed to delete all questions"
    cur.close()
    conn.close()
    return result


def get_question_position(position):
    conn=create_connection()
    cur = conn.cursor()
    cur.execute("begin")
    get_q = ''' SELECT id FROM Question WHERE position=? '''
    data_position=(position,)
    try:
        cur.execute(get_q,data_position)
        row=cur.fetchall()
        cur.close()
        conn.close()
        if(len(row)>0):
            id:int=row[0][0]
            return get_question(id)
        else:
            return "Non existing position"
    except Error as e:
            return "Failed get question by position"


def update_all_positions(position):
    conn=create_connection()
    cur = conn.cursor()
    cur.execute("begin")
    get_q=''' SELECT position,title,image,text,id FROM Question WHERE position>=? ORDER BY position DESC'''
    data_pos=(position,)
    result=1
    try:
        cur.execute(get_q,data_pos)
        rows=cur.fetchall()
        cur.close()
        conn.close()
        add=0
        if len(rows)>1:
            add=rows[0][0]
        for row in rows:
            q=Question(row[0],row[1],row[2],row[3],row[4],[])
            setattr(q,'position',getattr(q,'position')+add)
            result=update_question(q)
    except Error as e:
        cur.close()
        conn.close()
        result="Failed to add question"
    if len(rows)==1:
        result=rows[0][0]

    return result

def equilibrate():
    conn=create_connection()
    cur = conn.cursor()
    cur.execute("begin")
    get_q=''' SELECT position,title,image,text,id FROM Question ORDER BY position ASC'''
    result=1
    try:
        cur.execute(get_q)
        rows=cur.fetchall()
        cur.close()
        conn.close()
        add=1
        for row in rows:
            q=Question(row[0],row[1],row[2],row[3],row[4],[])
            setattr(q,'position',add)
            result=update_question(q)
            add=add+1
    except Error as e:
        cur.close()
        conn.close()
        result="Failed to equilibrate"

    return result


def get_number_questions():
    conn=create_connection()
    cur = conn.cursor()
    cur.execute("begin")
    get_q=''' SELECT * FROM Question'''
    nb_questions=0
    try:
        cur.execute(get_q)
        rows=cur.fetchall()
        nb_questions=len(rows)
    except Error as e:
        print(e)
    cur.close()
    conn.close()
    return nb_questions

def calculate_score(participation):
    score=0
    max_range=get_number_questions()+1
    index=0
    answList=getattr(participation,'ansList')
    for i in range(1,max_range):
        q=get_question_position(i)
        if getattr(getattr(q,'possibleAnswers')[answList[index]-1],'isCorrect')==1:
            score=score+1
        index=index+1
    return score

def add_participation(participation):
    conn=create_connection()
    cur = conn.cursor()
    cur.execute("begin")
    insert_to_part = ''' INSERT INTO Participation(name,score) VALUES(?,?) '''
    data_p=(getattr(participation,'name'),getattr(participation,'score'))
    result=1
    try:
        cur.execute(insert_to_part, data_p)
        conn.commit()
    except Error as e:
        conn.rollback()
        result= "insert question failed"
    cur.close()
    conn.close()
    return result

def get_all_participations():
    conn=create_connection()
    cur = conn.cursor()
    cur.execute("begin")
    get_q=''' SELECT name,score FROM Participation ORDER BY score DESC'''
    participations_list=[]
    try:
        cur.execute(get_q)
        rows=cur.fetchall()
        for row in rows:
            p=Participation(row[0],[],row[1])
            participations_list.append(p.PyToJson())
    except Error as e:
        print(e)
    cur.close()
    conn.close()
    return participations_list

def delete_all_participations():
    conn=create_connection()
    cur = conn.cursor()
    cur.execute("begin")
    delete_p = ''' DELETE FROM Participation'''
    result=1
    try:
        cur.execute(delete_p)
        conn.commit()
    except Error as e:
        result="failed to delete all participations"
    cur.close()
    conn.close()
    return result