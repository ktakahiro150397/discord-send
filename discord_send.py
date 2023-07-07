


class discord_send_message():
    '''Represents a message to be sent to a discord webhook.'''

    def __init__(self,message:str) -> None:
        self.message = message






class discord_sender():
    '''Send messages to a discord webhook.'''

    def __init__(self,webhookUrl:str) -> None:
        pass


    def sendMessage(self,message:discord_send_message) -> None:
        pass








    