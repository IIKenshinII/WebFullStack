from flask import Flask,request
from flask_cors import CORS
from jwt_utils import *

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
	if token is not None:
		token=token.split("Bearer ",1)[1]
		result=decode_token(token)
	else:
		return "No token"
	if result=="quiz-app-admin":
		return token
	else :
		return "Token expired",401
	

if __name__ == "__main__":
    app.run()