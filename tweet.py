from pyrogram import Client,filters,idle
from pyrogram.types import Message
from pyrogram.types import (ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton)
from config import api_id,api_hash,bot_token,channel

bot = Client("OdinGame_Tweet",api_id,api_hash,bot_token)

async def odingame():
    dsh = InlineKeyboardMarkup([
            [InlineKeyboardButton(f'|📝| - بیانیه', callback_data='tw')]])
    return await dsh

@bot.on_message(filters.command(['/panel',"/start"],None))
async def panel(c,m):
	await bot.send_message(m.chat.id,f"**• بخش مورد نظرتون رو انتخاب کنین **",reply_markup=odingame(),reply_to_message_id=m.message_id)

@bot.on_callback_query(filters.regex(r"tw"))
async def p_q_c(c,query):
    await query.answer("Powered by OdinGame", show_alert=True)
    await query.edit_message_text(f"**• بیانیه خود را ارسال کنید **")

@bot.on_message(filters.group,group=0)
async def sendch(c, m):
    if m.reply_to_message and "بیانیه خود را ارسال کنید" in m.reply_to_message.text:
        mb_id = (m.forward(channel)).message_id
        await bot.send_message(m.chat.id,"**• انجام شد✔**")

print("OdinGame Tweet Bot Starting...")
bot.start()
print('OdinGame Bot Started !')
idle()