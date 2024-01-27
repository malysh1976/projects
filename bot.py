import telebot 
import requests
 
 
token='6365100027:AAESUZPeAmVhDtcAPwSGJPl7IS8LINciRIs' 
 
bot=telebot.TeleBot(token) 
 
def reqapi(ip): 
    url=f'https://ipinfo.io/{ip}/geo' 
    r=requests.get(url).json() 
    return(r) 
 
@bot.message_handler(commands=['start']) 
def start(message): 
    msg=bot.send_message(message.chat.id,f'Привет, {message.from_user.username}\n  Введи ip:  ') 
    bot.register_next_step_handler(msg, getip) 
 
 
 
def getip(message): 
    ip = message.text 
    res=reqapi(ip)
    msg=f' По вашему ip - {res["ip"]}\
    \n Город - {res["city"]}\
    \n Регион - {res["region"]}\
    \n Страна - {res["country"]}\
    \n Координаты - {res["loc"]}\
    \n Часовой пояс - {res["timezone"]}'
    
    bot.send_message(message.chat.id,msg) 

if __name__=='__main__': 
    bot.infinity_polling()

