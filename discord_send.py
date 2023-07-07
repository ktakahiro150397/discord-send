import logging
import requests


class discord_send_message():
    '''Represents a message to be sent to a discord webhook.'''

    def __init__(self,message:str) -> None:
        self.message = message

    def getMessageObject(self) -> dict:
        '''Returns a dict object representing the message.'''
        return {
            "content":self.message
        }

class discord_sender():
    '''Send messages to a discord webhook.'''

    def __init__(self,webhookUrl:str) -> None:
        self.webhookUrl = webhookUrl
        
        self._logger = logging.getLogger(__name__)
        self._logger.addHandler(logging.NullHandler())
        self._logger.setLevel(logging.DEBUG)
        self._logger.propagate = True


    def sendMessage(self,message:discord_send_message) -> None:
        self._logger.debug(f"sendMessage: {message.message}")

        response = requests.post(
            url=self.webhookUrl,
            json=message.getMessageObject(),
        )

        self._logger.debug(f"Response status code: {response.status_code}")
        self._logger.debug(f"Response text: {response.text}")

        








    