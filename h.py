from config import Config
from pyrogram import Client

api_id = Config.APP_ID
api_hash = Config.API_HASH
bot_token = Config.TG_BOT_TOKEN

app = Client(
    "my_bot",
    api_id=api_id, api_hash=api_hash,
    bot_token=bot_token
)

app.run()
