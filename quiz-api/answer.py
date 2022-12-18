class Answer():
    def __init__(self,idQuestion:int=None,text:str=None,isCorrect:int=None,id:int=None):
        self.idQuestion=idQuestion
        self.text=text
        self.isCorrect=isCorrect
        self.id=id

    def PyToJson(self):
        response={"text":self.text,"id":self.id,"idQuestion":self.idQuestion,"isCorrect":not not self.isCorrect}
        return response

    def JsonToPy(self,payload):
       setattr(self,'isCorrect',payload['isCorrect'])
       setattr(self,'text',payload['text'])
       setattr(self,'idQuestion',payload['idQuestion'])
