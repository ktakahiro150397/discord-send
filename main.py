import asyncio
from datetime import datetime, timedelta, timezone
import json
from logging import config,getLogger
import os
import pathlib
import traceback
from dotenv import load_dotenv

import discord_send

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
    sender = discord_send.discord_sender(webhookUrl)

    # logger.debug("sendMessage")
    # test_message = discord_send_message("This is test message")
    # sender.sendMessage(test_message)

    japan_timezone = timezone(timedelta(hours=9))

    footer = discord_send.discord_send_footer(text="Sent by discord_send",icon_url="https://avatars.githubusercontent.com/u/58302085?v=4")
    provider = discord_send.discord_send_provider(name="provider",url="https://qiita.com/")
    image = discord_send.discord_send_image(url="https://avatars.githubusercontent.com/u/58302085?v=4",height=50,width=50)
    thumbnail = discord_send.discord_send_image(url="https://avatars.githubusercontent.com/u/58302085?v=4",height=20,width=20)
    author = discord_send.discord_send_author(name="@discord_send",url="https://www.google.com",icon_url="https://avatars.githubusercontent.com/u/58302085?v=4")
    fields = discord_send.discord_send_fields()
    fields.pushFieldElement("field1", "いい感じに並べて表示",True)
    fields.pushFieldElement("field2", "これは横並び",True)
    fields.pushFieldElement("field3", "これも横並び",True)
    fields.pushFieldElement("field4", "これは1行で表示する",False)
    # fields.pushFieldElement("field4", "value4",True)
    # fields.pushFieldElement("field5", "value5",True)
    # fields.pushFieldElement("field6", "value6",True)
    # fields.pushFieldElement("field7", "value7",True)
    # fields.pushFieldElement("field8", "value8",True)
    # fields.pushFieldElement("field9", "value9",True)
    # fields.pushFieldElement("field10", "value10",False)


    jpgTestPath = pathlib.Path("attach_test.jpg")
    zipTestPath = pathlib.Path("Cassava2_5_1_64.zip")

    attachTestFiles = [jpgTestPath,zipTestPath]


    embed_message = discord_send.discord_send_embed(title="タイトル",
                                       description="embed description\rembed使うとよく見るアレみたいなオシャレ表示ができる",
                                       url="https://qiita.com/Qiita/items/c686397e4a0f4f11683d",
                                       timestamp=datetime.now(japan_timezone),
                                       sidebarColorCode="#f27009",
                                       footer=footer,
                                       provider=provider,
                                       image=image,
                                       thumbnail=thumbnail,
                                       author=author,
                                       fields=fields)
    avatar_username_message = discord_send.discord_send_message("Webhook テストメッセージ送信確認",
                                                   username="Webhookユーザー",
                                                   avatar_url="https://avatars.githubusercontent.com/u/58302085?v=4",
                                                   embed=embed_message)
    # sender.sendMessage(avatar_username_message)
    # sender.sendAttachFiles(filePath=attachTestFiles)

    try:
        raise Exception("テストエラー")
    except Exception as ex:
        # エラー内容をDiscordに送信
        author = discord_send.discord_send_author(name="weather-forecast.py エラー通知",
                                                  icon_url="")
        sender = discord_send.discord_sender(webhookUrl)
        # sender.sendMessage(message)
        sender.sendExceptionMessage(author=author,ex=ex)

if __name__ == '__main__':
    main()