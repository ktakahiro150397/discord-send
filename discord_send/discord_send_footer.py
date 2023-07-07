class discord_send_footer():
    def __init__(self,text:str,icon_url:str="",proxy_icon_url:str="") -> None:
        self.text = text
        self.icon_url = icon_url
        self.proxy_icon_url = proxy_icon_url

    
    def getMessageObject(self) -> dict:
        '''Returns a dict object representing the message.'''

        obj = {
            "text":self.text,
            "icon_url":self.icon_url,
            "proxy_icon_url":self.proxy_icon_url,
        }

        for key in list(obj.keys()):
            if obj[key] == "":
                del obj[key]

        return obj
    
    def __str__(self) -> str:
        return self.getMessageObject().__str__()