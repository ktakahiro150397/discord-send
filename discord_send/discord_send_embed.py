from datetime import datetime


class discord_send_embed():
    '''Represents a embed message to be sent to a discord webhook.'''
    
    def __init__(self,
                 title:str="",
                 description:str="",
                 url:str="",
                 timestamp:datetime=None,
                 ) -> None:
        self.title = title
        self.description = description
        self.url = url
        self.timestamp = timestamp

    def getMessageObject(self) -> dict:
        '''Returns a dict object representing the message.'''

        obj = {
            "title":self.title,
            "description":self.description,
            "url":self.url,
            "timestamp":self.timestamp.isoformat()
        }

        for key in list(obj.keys()):
            if obj[key] == "":
                del obj[key]

        return obj
    
    def __str__(self) -> str:
        return self.getMessageObject().__str__()
        
    