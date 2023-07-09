from datetime import datetime
import json
import logging
from pathlib import Path
import pathlib
import traceback
from zoneinfo import ZoneInfo
import requests
from discord_send.discord_send_author import discord_send_author
from discord_send.discord_send_embed import discord_send_embed
from discord_send.discord_send_footer import discord_send_footer

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

    def sendExceptionMessage(self,author:discord_send_author,ex:Exception) -> None:
        japan_timezone = ZoneInfo(key="Asia/Tokyo")

        if author.icon_url == "":
            author.icon_url = "https://raw.githubusercontent.com/ktakahiro150397/discord-send/main/icons/warning.png"

        footer = discord_send_footer(text="from エラー通知ライブラリ discord_send")

        embed = discord_send_embed(title=ex.__class__.__name__ + "が発生しました :face_with_open_eyes_and_hand_over_mouth:",
                                    description="以下のエラーが発生しました。"+ "\r\r" + str(ex) + "\r" + traceback.format_exc(),
                                    sidebarColorCode="#ff0000",
                                    author=author,
                                    footer=footer,
                                    timestamp=datetime.now(tz=japan_timezone)
                                    )
        
        iconFilePath = [pathlib.Path("attach_test.jpg")]

        message = discord_send_message(message="",
                                        username="例外通知ちゃん",
                                        embed=embed)
        self.sendMessage(message)