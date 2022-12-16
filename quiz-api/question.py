class Question():
    id=None
    possibleAnswers=None
    def __init__(self,pos:int=None,title: str=None,image:str=None,text: str=None):
        self.title = title
        self.position = pos
        self.image = image
        self.text = text

    def PyToJson(self):
        response={"title":self.title,"text":self.text,"id":self.id,"position":self.position,"image":self.image,"possibleAnswers":self.possibleAnswers}
        return response

    def JsonToPy(self,payload):
       setattr(self,'image',payload['image'])
       setattr(self,'text',payload['text'])
       setattr(self,'title',payload['title'])
       setattr(self,'position',payload['position'])
       setattr(self,'possibleAnswers',payload['possibleAnswers'])