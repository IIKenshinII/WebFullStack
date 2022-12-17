from answer import *
class Question():
    def __init__(self,pos:int=None,title: str=None,image:str=None,text: str=None,id:int=None):
        self.title = title
        self.position = pos
        self.image = image
        self.text = text
        self.possibleAnswers=[]
        self.id=id

    def PyToJson(self):
        response={"title":self.title,"text":self.text,"id":self.id,"position":self.position,"image":self.image,"possibleAnswers":self.possibleAnswers}
        return response

    def JsonToPy(self,payload):
       setattr(self,'image',payload['image'])
       setattr(self,'text',payload['text'])
       setattr(self,'title',payload['title'])
       setattr(self,'position',payload['position'])
       for answer in payload['possibleAnswers']:
            ans=Answer()
            setattr(ans,'isCorrect',answer['isCorrect'])
            setattr(ans,'text',answer['text'])
            self.possibleAnswers.append(ans)

    