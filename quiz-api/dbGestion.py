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

#insert a question in the database using the parameter
#return a string if error else return an int
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


#insert the possible answers of the questions
#return a string if error else return an int
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


# get a question from it's id
#return a question object if succes else string
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


# update a question using a question object
# return update succesful if success else  update question failed
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


# delete an answer using a question id
# return true if success else false
def delete_answer(cur,id):
    delete_ans = ''' DELETE FROM Answer WHERE idQuestion=?'''
    data_id=(id,)
    try:
        cur.execute(delete_ans,data_id)
        return True
    except Error as e:
            return False

# delete a question using id
# return string if failed else nothing
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

# delete all questions
# return int if successful else string
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


# get question from it's position
# return a question if success else string
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


# update all question's position from the given position
# to avoid having duplicate position and to reorder the questions
# return an int if success else string
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

# used after update_all_positions call to reset the positions following a natural order
# return an int if success else string 
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


# get the number of questions
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

# calculate the score of the player using the participations
# return the score of the player and a list containing the positions of the good answers and
# if the player's answers are good or not
def calculate_score(participation):
    score=0
    max_range=get_number_questions()+1
    index=0
    answList=getattr(participation,'ansList')
    goodAnswerList=[]
    for i in range(1,max_range):
        q=get_question_position(i)
        correctAnswerPosition=1
        for ans in getattr(q,'possibleAnswers'):
            if getattr(ans,'isCorrect')==1:
                break
            correctAnswerPosition=correctAnswerPosition+1
        if getattr(getattr(q,'possibleAnswers')[answList[index]-1],'isCorrect')==1:
            score=score+1
            wasCorrect=True
        else:
            wasCorrect=False
        index=index+1
        goodAnswerList.append({'correctAnswerPosition':correctAnswerPosition,'wasCorrect':wasCorrect})
    return score,goodAnswerList

# add a player's participation in the database
# return an int if success else string 
def add_participation(participation):
    conn=create_connection()
    cur = conn.cursor()
    cur.execute("begin")
    insert_to_part = ''' INSERT INTO Participation(name,score,date) VALUES(?,?,?) '''
    data_p=(getattr(participation,'name'),getattr(participation,'score'),getattr(participation,'date'))
    result=1
    try:
        cur.execute(insert_to_part, data_p)
        conn.commit()
    except Error as e:
        conn.rollback()
        result= "insert participation failed"
    cur.close()
    conn.close()
    return result


# get all participations of the quiz
# return a list of all the participations
def get_all_participations():
    conn=create_connection()
    cur = conn.cursor()
    cur.execute("begin")
    get_q=''' SELECT name,score,date FROM Participation ORDER BY score DESC'''
    participations_list=[]
    try:
        cur.execute(get_q)
        rows=cur.fetchall()
        for row in rows:
            p=Participation(row[0],[],row[1],row[2])
            participations_list.append(p.PyToJson())
    except Error as e:
        print(e)
    cur.close()
    conn.close()
    return participations_list


# delete all participations
# return an int if success else string 
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

# creat a database using the bdd.sql file
def database_create():
    with create_connection() as db:
        with open('bdd.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()