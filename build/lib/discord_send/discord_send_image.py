class discord_send_image():
    def __init__(self,url:str,proxy_url:str="",height:int="",width:int="") -> None:
        self.url = url
        self.proxy_url = proxy_url
        self.height = height
        self.width = width

    
    def getMessageObject(self) -> dict:
        '''Returns a dict object representing the message.'''

        obj = {
            "url":self.url,
            "proxy_url":self.proxy_url,
            "height":self.height,
            "width":self.width,
        }

        for key in list(obj.keys()):
            if obj[key] == "":
                del obj[key]

        return obj
    
    def __str__(self) -> str:
        return self.getMessageObject().__str__()