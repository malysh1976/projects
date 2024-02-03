import telebot 
import requests
 
 
token='6365100027:AAESUZPeAmVhDtcAPwSGJPl7IS8LINciRIs' 
 
bot=telebot.TeleBot(token) 
 
def reqapi(ip): 
    url=f'https://ipinfo.io/{ip}/geo' 
    r=requests.get(url).json() 
    return(r) 
 
def generator_keyboards(ListNameBTN, NumbersColumns=2):
    keyboards=telebot.types.ReplyKeyboardMarkup(row_width=NumbersColumns, resize_keyboard=True)
    btn_names=[telebot.types.KeyboardButton(text=x) for x in ListNameBTN]
    keyboards.add(*btn_names)
    return keyboards       



@bot.message_handler(commands=['start']) 
def start(message):
    bot.send_message(message.chat.id,f'Привет', reply_markup=generator_keyboards(['Информация об ip']))
    
    
@bot.message_handler(commands=['Информация об ip']) 
def info(message):
    def getip(message): 
        ip = message.text 
        res=reqapi(ip)
        msg=f'По вашему ip - {res["ip"]} \n Следущая информация: \n Город - {res["city"]}'
        msg=f' По вашему ip - {res["ip"]}\
        \n Город - {res["city"]}\
        \n Регион - {res["region"]}\
        \n Страна - {res["country"]}\
        \n Координаты - {res["loc"]}\
        \n Часовой пояс - {res["timezone"]}'









#


        



if __name__=='__main__': 
    bot.infinity_polling()




