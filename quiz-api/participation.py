from datetime import datetime


class Participation():
    def __init__(self,name:str=None,ansList=None,score:int=None,date:str=None):
        self.name=name
        self.ansList=ansList
        self.score=score
        if date==None:
            now = datetime.now()
            self.date= now.strftime("%d-%m-%Y %H:%M:%S")
        else:
            self.date=date
        self.answersSummaries=[]
    
    def PyToJson(self):
        response={"playerName":self.name,"score":self.score,"date":self.date}
        return response

    def PyToJson2(self):
        response={"playerName":self.name,"score":self.score,"answersSummaries":self.answersSummaries}
        return response

