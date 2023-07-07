class discord_send_field_element():
    def __init__(self,name:str,value:str="",inline:bool=False) -> None:
        self.name = name
        self.value = value
        self.inline = inline

    def getMessageObject(self) -> dict:
        '''Returns a dict object representing the message.'''

        obj = {
            "name":self.name,
            "value":self.value,
            "inline":self.inline,
        }

        for key in list(obj.keys()):
            if obj[key] == "":
                del obj[key]

        return obj
    
    def __str__(self) -> str:
        return self.getMessageObject().__str__()

class discord_send_fields():
    def __init__(self) -> None:
        self.fields:list[discord_send_field_element] = []

    def pushFieldElement(self,name:str,value:str="",inline:bool=False) -> None:
        self.fields.append(discord_send_field_element(name,value,inline))
    
    def getMessageObject(self) -> list[dict]:
        '''Returns a dict object representing the message.'''
        array = []
        for field in self.fields:
            obj = {
                "name":field.name,
                "value":field.value,
                "inline":field.inline,
            }

            for key in list(obj.keys()):
                if obj[key] == "":
                    del obj[key]

            array.append(obj)

        return array
    
    def __str__(self) -> str:
        return self.getMessageObject().__str__()
    

    