from datetime import datetime
import logging


class discord_send_embed():
    '''Represents a embed message to be sent to a discord webhook.'''
    
    def __init__(self,
                 title:str="",
                 description:str="",
                 url:str="",
                 timestamp:datetime=None,
                 sidebarColorCode:str=""
                 ) -> None:
        self.title = title
        self.description = description
        self.url = url
        self.timestamp = timestamp
        self.sidebarColorCode = sidebarColorCode

        self._logger = logging.getLogger(__name__)
        self._logger.addHandler(logging.NullHandler())
        self._logger.setLevel(logging.DEBUG)
        self._logger.propagate = True

    def getMessageObject(self) -> dict:
        '''Returns a dict object representing the message.'''

        obj = {
            "title":self.title,
            "description":self.description,
            "url":self.url,
            "timestamp":self.timestamp.isoformat(),
            "color":self.getColorCode()
        }

        for key in list(obj.keys()):
            if obj[key] == "":
                del obj[key]

        return obj
    
    def getColorCode(self) -> str:
        if self.sidebarColorCode == "":
            return ""
        else:
            code = self.sidebarColorCode.replace("#","")
            
            try:
                int_code = int(code,base=16)
                return int_code
            except ValueError:
                self._logger.error(f"Invalid color code: {self.sidebarColorCode}")
                return ""
    
    def __str__(self) -> str:
        return self.getMessageObject().__str__()
        
    