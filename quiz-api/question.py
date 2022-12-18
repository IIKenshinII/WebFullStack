from answer import *
import json
class Question():
    def __init__(self,pos:int=None,title: str=None,image:str=None,text: str=None,id:int=None,possibleAnswers=None):
        self.title = title
        self.position = pos
        self.image = image
        self.text = text
        self.possibleAnswers=[]
        self.id=id
        if possibleAnswers!=None:
            for answer in possibleAnswers:
                ans=Answer(answer[0],answer[1],answer[2],answer[3])
                self.possibleAnswers.append(ans)

    def PyToJson(self):
        response={"title":self.title,"text":self.text,"id":self.id,"position":self.position,"image":self.image,"possibleAnswers":[Answer.PyToJson(i) for i in self.possibleAnswers]}
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

    