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
	#si le token est valide on retourn l'id de la question ajouté et le message http 200
	if result=="quiz-app-admin":
		question=Question()
		question.JsonToPy(payload)
		test=insert_question(question)
		return {'id':test},200
	else :
		return result,401

# @app.route('/questions/<int:idQuestion>', methods=['PUT'])
# def PutQuestion(idQuestion):
# 	#Récupérer le token envoyé en paramètre
# 	token=request.headers.get('Authorization')
# 	payload = request.get_json()
# 	#on vérifie qu'il y ai bien un token valide
# 	if token is not None:
# 		token=token.split("Bearer ",1)[1]
# 		result=decode_token(token)
# 	else:
# 		return 'Unauthorized', 401

# 	return 200


@app.route('/questions/<int:idQuestion>', methods=['GET'])
def GetQuestion(idQuestion):
	#Récupérer le token envoyé en paramètre
	question_result=get_question(idQuestion)
	if question_result=="get question failed":
		return question_result,404
	else :
		return question_result.PyToJson(),200
	


def verifyToken(token):
	#on vérifie qu'il y ai bien un token valide
	if token is not None:
		token=token.split("Bearer ",1)[1]
		result=decode_token(token)
	else:
		return 'Unauthorized', 401

	return result

if __name__ == "__main__":
    app.run()