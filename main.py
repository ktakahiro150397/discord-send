import asyncio
from datetime import datetime
import json
from logging import config,getLogger
import os
from dotenv import load_dotenv
from discord_send import discord_send_message,discord_sender

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
    message = discord_send_message("This is test message")
    sender = discord_sender(webhookUrl)

    sender.sendMessage(message)


if __name__ == '__main__':
    main()