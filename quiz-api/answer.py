class Answer():
    id=None
    def __init__(self,idQuestion=None,text=None,isCorrect=None):
        self.idQuestion=idQuestion
        self.text=text
        self.isCorrect=isCorrect

    def PyToJson(self):
        response={"text":self.text,"id":self.id,"idQuestion":self.idQuestion,"isCorrect":self.isCorrect}
        return response

    def JsonToPy(self,payload):
       setattr(self,'isCorrect',payload['isCorrect'])
       setattr(self,'text',payload['text'])
       setattr(self,'idQuestion',payload['idQuestion'])
