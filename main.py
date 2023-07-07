import asyncio
from datetime import datetime, timedelta, timezone
import json
from logging import config,getLogger
import os
import pathlib
from dotenv import load_dotenv
from discord_send.discord_send_author import discord_send_author
from discord_send.discord_send_fields import discord_send_fields
from discord_send.discord_send_image import discord_send_image

from discord_send.discord_send_provider import discord_send_provider
from discord_send.discord_send_footer import discord_send_footer
from discord_send.discord_sender import discord_sender
from discord_send.discord_send_message import discord_send_message
from discord_send.discord_send_embed import discord_send_embed

# 現在のスクリプトファイルの絶対パスを取得する
script_dir = os.path.dirname(os.path.abspath(__file__))

# 設定ファイルのパスを作成する
settings_file_path = os.path.join(script_dir, "logsettings.json")

# ログ設定読込
with open(settings_file_path) as f:
    config.dictConfig(json.load(f))
logger = getLogger(__name__)

# 環境変数を読み込み
load_dotenv()

webhookUrl = os.getenv("DISCORD_SEND_URL")

def main():
    sender = discord_sender(webhookUrl)

    # logger.debug("sendMessage")
    # test_message = discord_send_message("This is test message")
    # sender.sendMessage(test_message)

    japan_timezone = timezone(timedelta(hours=9))

    footer = discord_send_footer(text="Sent by discord_send",icon_url="https://avatars.githubusercontent.com/u/58302085?v=4")
    provider = discord_send_provider(name="provider",url="https://qiita.com/")
    image = discord_send_image(url="https://avatars.githubusercontent.com/u/58302085?v=4",height=50,width=50)
    thumbnail = discord_send_image(url="https://avatars.githubusercontent.com/u/58302085?v=4",height=20,width=20)
    author = discord_send_author(name="author test name",url="https://www.google.com",icon_url="https://avatars.githubusercontent.com/u/58302085?v=4")
    fields = discord_send_fields()
    fields.pushFieldElement("field1", "value1",True)
    fields.pushFieldElement("field2", "value2",True)
    fields.pushFieldElement("field3", "value3",True)
    fields.pushFieldElement("field4", "value4",True)
    fields.pushFieldElement("field5", "value5",True)
    fields.pushFieldElement("field6", "value6",True)
    fields.pushFieldElement("field7", "value7",True)
    fields.pushFieldElement("field8", "value8",True)
    fields.pushFieldElement("field9", "value9",True)
    fields.pushFieldElement("field10", "value10",False)


    jpgTestPath = pathlib.Path("attach_test.jpg")
    zipTestPath = pathlib.Path("Cassava2_5_1_64.zip")

    attachTestFiles = [jpgTestPath,zipTestPath]


    embed_message = discord_send_embed(title="embed_title",
                                       description="embed_description\rThis is loooooooooooooong descriptiooooooooooooooooooooon",
                                       url="https://qiita.com/Qiita/items/c686397e4a0f4f11683d",
                                       timestamp=datetime.now(japan_timezone),
                                       sidebarColorCode="#f27009",
                                       footer=footer,
                                       provider=provider,
                                       image=image,
                                       thumbnail=thumbnail,
                                       author=author,
                                       fields=fields)
    avatar_username_message = discord_send_message("This is test message.(username/avater)\raaaaaaaaaaaaaa\rbbbbbbbbbbbb",
                                                   username="test_username",
                                                   avatar_url="https://avatars.githubusercontent.com/u/58302085?v=4",
                                                   embed=embed_message)
    # sender.sendMessage(avatar_username_message)
    # sender.sendMessageWithAttachFile(avatar_username_message,file_bin=file_jpg)
    sender.sendAttachFiles(filePath=attachTestFiles)

if __name__ == '__main__':
    main()