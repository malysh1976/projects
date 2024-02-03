import telebot
import requests
from environs import Env

env = Env()
env.read_env()
token = env('TOKEN')

bot = telebot.TeleBot(token)
def getinfo(ip: str) -> dict:
    url = f'https://ipinfo.io/{ip}/geo'
    r = requests.get(url).json()
    return r

def generator_keyboards(ListNameBTN, NumberColumns = 2):
    keyboards = telebot.types.ReplyKeyboardMarkup(row_width=NumberColumns, resize_keyboard=True)
    btn_names = [telebot.types.KeyboardButton(text=x) for x in ListNameBTN]
    keyboards.add(*btn_names)
    return keyboards

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'hello', reply_markup=generator_keyboards(['ip']))
 
@bot.message_handler(func= lambda m : m.text)
def text(message):
    text = message.text
    if text == 'ip':
        msg = bot.send_message(message.chat.id, 'Введите ip:')
        bot.register_next_step_handler(msg, getip)

def getip(message):
    ip = message.text
    info = str(getinfo(ip))
    bot.send_message(message.chat.id, info)

if __name__ == '__main__':
    bot.infinity_polling()






