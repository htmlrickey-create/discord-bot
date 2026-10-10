import os
import random
import time

import discord
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

# Discordから受け取るイベントを設定
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


REACTIONS = [
    "うおｗｗｗｗ",
    "かっけーっすｗｗ",
    "お、おう。😅",
    "落ち着けってｗ😅",
    "そういうところ尊敬してます！😅",
    "どわーーｗｗ",
    "きちーーｗｗ😅",
    "ちょ、君必死やんｗｗｗ",
    "ちょ、だれか言ってやれよｗｗ😅😅😅",
    "ど、どした？笑"
]

REPLY_CHANCE = 0.45

last_reply_time = {}


@client.event
async def on_ready():
    print(f"ログイン成功: {client.user}")


@client.event
async def on_message(message):
    # Bot同士の反応ループを防ぐ
    if message.author.bot:
        return

    # サーバー内の発言だけを対象にする
    if message.guild is None:
        return

    # 空のメッセージには反応しない
    if not message.content.strip():
        return

    # チャンネルごとのクールダウンを確認
    now = time.monotonic()
    channel_id = message.channel.id

    previous_time = last_reply_time.get(channel_id, 0)

    # 10%の確率で反応
    if random.random() > REPLY_CHANCE:
        return

    # 冷笑コメントをランダムに選択
    response = random.choice(REACTIONS)

    # 元の発言に返信する
    await message.reply(
        response,
        mention_author=False
    )

    last_reply_time[channel_id] = time.monotonic()


if not TOKEN:
    raise RuntimeError("DISCORD_TOKENが設定されていません")

client.run(TOKEN)