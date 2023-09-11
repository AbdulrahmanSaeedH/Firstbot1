from telebot import TeleBot
import random

token = "6694854796:AAFLAnIpjOS5Md14Kv7Ux3oSNf3migOa4O0" # توكنك هنا
idd = 6547238290 #ايديك هنا
bot = TeleBot(token=token,num_threads=45,threaded=True,skip_pending=True,parse_mode='html', disable_web_page_preview=True)

letters = 'abcdefghijklmnopqrstuvwxyz'
letter = 'abcd_efghijkl_mnopqrstuvwxy_z1234567890'

seen_bots = []

for _ in range(1500):
 try:
  letters = 'abcdefghijklmnopqrstuvwxyz'
  hhk = ''.join(random.sample(letters, 1))
  letter = 'abcd_efghijkl_mnopqrstuvwxy_z1234567890'
  hhkk = ''.join(random.sample(letter, 2))
  bots = f"@{hhk}{hhkk}bot"
  if bots not in seen_bots:
   us = bot.get_chat(bots)
   seen_bots.append(bots)
   
 except Exception as a:
  error_message = str(a)
  if "Bad Request: chat not found" in error_message:
   bot.send_message(chat_id=idd, text=f'{bots}')

bot.infinity_polling()

