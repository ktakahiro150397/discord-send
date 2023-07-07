class discord_send_message():
    '''Represents a message to be sent to a discord webhook.'''

    def __init__(self,message:str) -> None:
        self.message = message

    def getMessageObject(self) -> dict:
        '''Returns a dict object representing the message.'''
        return {
            "content":self.message
        }
    
    def __str__(self) -> str:
        return self.getMessageObject().__str__()