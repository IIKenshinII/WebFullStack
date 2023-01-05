from flask import Flask,request
from flask_cors import CORS
from jwt_utils import *
from dbGestion import *
from participation import *

app = Flask(__name__)
CORS(app)

@app.route('/quiz-info', methods=['GET'])
def GetQuizInfo():
	scores=get_all_participations()
	return {"size": get_number_questions(), "scores": scores}, 200

@app.route('/')
def hello_world():
	x = 'world'
	return f"Hey, {x}"

@app.route('/login', methods=['POST'])
def PostPassword():
	payload = request.get_json()
	password="flask2023"
	token=build_token()
	if password!=payload['password']:
		return 'Unauthorized', 401
	else :
		return {'token':token},200


@app.route('/rebuild-db', methods=['POST'])
def RebuildDb():
	#Récupérer le token envoyé en paramètre
	token=request.headers.get('Authorization')
	result=verifyToken(token)
	if result=="quiz-app-admin":
		database_create()
		return "Ok",200
	else :
		return result,401


@app.route('/questions', methods=['POST'])
def PostQuestion():
	#Récupérer le token envoyé en paramètre
	token=request.headers.get('Authorization')
	payload = request.get_json()
	result=verifyToken(token)
	pos=payload['position']
	#si le token est valide on retourn l'id de la question ajouté et le message http 200
	if result=="quiz-app-admin":
		if type(get_question_position(pos))==Question:
			val_update=update_all_positions(pos)
			if val_update!="update successfull":
				return val_update,400
		question=Question()
		question.JsonToPy(payload)
		test=insert_question(question)
		equilibrate()
		return {'id':test},200
	else :
		return result,401

@app.route('/questions/<int:idQuestion>', methods=['PUT'])
def PutQuestion(idQuestion):
	token=request.headers.get('Authorization')
	payload = request.get_json()
	result=verifyToken(token)
	#si le token est valide on retourn l'id de la question ajouté et le message http 200
	if result=="quiz-app-admin":
		question=get_question(idQuestion)
		if type(question)==Question:
			add=0
			if(getattr(question,'position')==1):
				add=1
			question.JsonToPy(payload)
			var=getattr(question,'position')
			setattr(question,'position',getattr(question,'position')+add)
			val=update_all_positions(getattr(question,'position'))
			if type(val)==int:
				setattr(question,'position',getattr(question,'position')+val)
			result_update=update_question(question)
			equilibrate()
			if result_update=="update successfull":
				return '',204
			else:
				return result_update,404
		else:
			return "Request not found",404
		
	else :
		return result,401	


@app.route('/questions/<int:idQuestion>', methods=['GET'])
def GetQuestion(idQuestion):
	#Récupérer le token envoyé en paramètre
	question_result=get_question(idQuestion)
	if type(question_result)==str:
		return question_result,404
	else :
		return question_result.PyToJson(),200

@app.route('/questions', methods=['GET'])
def GetQuestionByPosition():
	position:int = request.args.get('position')
	question_result=get_question_position(position)
	if type(question_result)==str:
		return question_result,404
	else :
		return question_result.PyToJson(),200

@app.route('/questions/<int:idQuestion>', methods=['DELETE'])
def DeleteQuestion(idQuestion):
	#Récupérer le token envoyé en paramètre
	token=request.headers.get('Authorization')
	result=verifyToken(token)
	if result=="quiz-app-admin":
		question_result=delete_question(idQuestion)
		if type(question_result)==str:
			return question_result,404
		else :
			equilibrate()
			return "sucess",204	
	else :
		return result,401

@app.route('/questions/all', methods=['DELETE'])
def DeleteAllQuestion():
	#Récupérer le token envoyé en paramètre
	token=request.headers.get('Authorization')
	result=verifyToken(token)
	if result=="quiz-app-admin":
		question_result=delete_all_questions()
		if type(question_result)==str:
			return question_result,404
		else :
			return "sucess",204	
	else :
		return result,401

@app.route('/participations', methods=['POST'])
def PostParticipation():
	payload = request.get_json()
	if len(payload['answers'])!=get_number_questions():
		return "Bad request",400
	else :
		participation=Participation(payload['playerName'],payload['answers'])
		score,answersSummaries=calculate_score(participation)
		setattr(participation,'score',score)
		setattr(participation,'answersSummaries',answersSummaries)
		result=add_participation(participation)
		if type(result)==int:
			return participation.PyToJson2(),200	
		else:
			return "error",404


@app.route('/participations/all', methods=['DELETE'])
def DeleteAllParticipations():
	token=request.headers.get('Authorization')
	question_result=delete_all_participations()
	result=verifyToken(token)
	if result=="quiz-app-admin":
		if type(question_result)==str:
			return question_result,404
		else :
			return "sucess",204	
	else :
		return result,401

def verifyToken(token):
	#on vérifie qu'il y ai bien un token valide
	result=1
	if token is not None:
		token=token.split("Bearer ",1)[1]
		result=decode_token(token)
	else:
		return 'Unauthorized'

	return result

if __name__ == "__main__":
    app.run()