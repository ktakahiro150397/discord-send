import json
import logging
from pathlib import Path
import requests

from discord_send.discord_send_message import discord_send_message

class discord_sender():
    '''Send messages to a discord webhook.'''

    def __init__(self,webhookUrl:str) -> None:
        self.webhookUrl = webhookUrl
        
        self._logger = logging.getLogger(__name__)
        self._logger.addHandler(logging.NullHandler())
        self._logger.setLevel(logging.DEBUG)
        self._logger.propagate = True


    def sendMessage(self,message:discord_send_message) -> None:
        self._logger.debug(f"sendMessage: {message}")

        response = requests.post(
            url=self.webhookUrl,
            json=message.getMessageObject(),
        )

        self._logger.debug(f"Response status code: {response.status_code}")
        self._logger.debug(f"Response text: {response.text}")

    def sendAttachFiles(self,filePath:list[Path]) -> None:
        self._logger.debug(f"sendAttachFiles: {filePath}")

        # ファイルパスの内容を読み込み
        file_payload = {}
        for path in filePath:
            with open(path.resolve(),"rb") as f:
                file_payload[path.name] = (path.name,f.read())

        response = requests.post(
            url=self.webhookUrl,
            files = file_payload
        )

        self._logger.debug(f"Response status code: {response.status_code}")
        self._logger.debug(f"Response text: {response.text}")