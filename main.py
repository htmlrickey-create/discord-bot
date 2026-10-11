
import os
import random
import time

import discord
from dotenv import load_dotenv
from discord import app_commands

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

# Discordから受け取るイベントを設定
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

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
    "ど、どした？笑",
    "そうっすねｗｗ",
    "そうなんだねｗｗｗ",
    "がんばっちゃってるー！ｗｗ",
]

REPLY_CHANCE = 0.50
last_reply_time = {}


@client.event
async def on_ready():
    await tree.sync()
    print(f"ログイン成功: {client.user}")
    print("スラッシュコマンドを同期しました")


# 冷笑コメント一覧
@tree.command(
    name="command",
    description="冷笑のレパートリーを紹介します"
)
async def command(interaction: discord.Interaction):
    reactions_text = "\n".join(
        f"・{reaction}" for reaction in REACTIONS
    )

    await interaction.response.send_message(
        f"**冷笑のレパートリー一覧**\n{reactions_text}"
    )


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

    # 50%の確率で反応
    if random.random() > REPLY_CHANCE:
        return

    # 冷笑コメントをランダムに選択
    response = random.choice(REACTIONS)

    # 元の発言に返信する
    await message.reply(
        response,
        mention_author=False
    )

    last_reply_time[message.channel.id] = time.monotonic()


if not TOKEN:
    raise RuntimeError("DISCORD_TOKENが設定されていません")

client.run(TOKEN)
