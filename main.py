import asyncio
from datetime import datetime, timedelta, timezone
import json
from logging import config,getLogger
import os
from dotenv import load_dotenv

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
    embed_message = discord_send_embed(title="embed_title",
                                       description="embed_description",
                                       url="https://qiita.com/Qiita/items/c686397e4a0f4f11683d",
                                       timestamp=datetime.now(japan_timezone),
                                       sidebarColorCode="#f27009",
                                       footer=footer)
    avatar_username_message = discord_send_message("This is test message.(username/avater)",
                                                   username="test_username",
                                                   avatar_url="https://avatars.githubusercontent.com/u/58302085?v=4",
                                                   embed=embed_message)
    sender.sendMessage(avatar_username_message)

if __name__ == '__main__':
    main()