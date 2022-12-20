class Participation():
    def __init__(self,name:str=None,ansList=None,score:int=None):
        self.name=name
        self.ansList=ansList
        self.score=score
    
    def PyToJson(self):
        response={"playerName":self.name,"score":self.score}
        return response

