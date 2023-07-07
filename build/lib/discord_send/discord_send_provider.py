class discord_send_provider():
    def __init__(self,name:str="",url:str="") -> None:
        self.name = name
        self.url = url
    
    def getMessageObject(self) -> dict:
        '''Returns a dict object representing the message.'''

        obj = {
            "name":self.name,
            "url":self.url,
        }

        for key in list(obj.keys()):
            if obj[key] == "":
                del obj[key]

        return obj
    
    def __str__(self) -> str:
        return self.getMessageObject().__str__()