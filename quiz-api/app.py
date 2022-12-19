from flask import Flask,request
from flask_cors import CORS
from jwt_utils import *
from dbGestion import *

app = Flask(__name__)
CORS(app)

@app.route('/quiz-info', methods=['GET'])
def GetQuizInfo():
	return {"size": 0, "scores": []}, 200

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
		return {"token":token},200


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
		return {'id':test},200
	else :
		return result

@app.route('/questions/<int:idQuestion>', methods=['PUT'])
def PutQuestion(idQuestion):
	token=request.headers.get('Authorization')
	payload = request.get_json()
	result=verifyToken(token)
	#si le token est valide on retourn l'id de la question ajouté et le message http 200
	if result=="quiz-app-admin":
		question=get_question(idQuestion)
		if type(question)==Question:
			question.JsonToPy(payload)
			update_all_positions(getattr(question,'position'))
			result_update=update_question(question)
			equilibrate()
			if result_update=="update successfull":
				return 'successfull',204
			else:
				return result_update,404
		else:
			return "Request not found",404
		
	else :
		return result,401	


# @app.route('/questions//<int:year>', methods=['PUT'])
# def PutQuestionAtPosition(year,month):
# 	token=request.headers.get('Authorization')
# 	payload = request.get_json()
# 	position = request.args.getlist()
# 	result=verifyToken(token)
# 	#si le token est valide on retourn l'id de la question ajouté et le message http 200
# 	if result=="quiz-app-admin":
# 		question=get_question(idQuestion)
# 		if question!="get question failed":
# 			question.JsonToPy(payload)
# 			result_update=update_question(question)
# 			if result_update=="update successfull":
# 				return result_update,204
# 		else:
# 			return "Request not found",404
		
# 	else :
# 		return result,401


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
	question_result=delete_question(idQuestion)
	result=verifyToken(token)
	if result=="quiz-app-admin":
		if type(question_result)==str:
			return question_result,404
		else :
			return "sucess",204	
	else :
		return result

@app.route('/questions/all', methods=['DELETE'])
def DeleteAllQuestion():
	#Récupérer le token envoyé en paramètre
	token=request.headers.get('Authorization')
	question_result=delete_all_questions()
	result=verifyToken(token)
	if result=="quiz-app-admin":
		if type(question_result)==str:
			return question_result,404
		else :
			return "sucess",204	
	else :
		return result

def verifyToken(token):
	#on vérifie qu'il y ai bien un token valide
	result=1
	if token is not None:
		token=token.split("Bearer ",1)[1]
		result=decode_token(token)
	else:
		return 'Unauthorized', 401

	return result

if __name__ == "__main__":
    app.run()