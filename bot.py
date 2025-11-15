import telebot
import random
import os

from bot_logic import gen_pass, gen_emodji, flip_coin
from bot_token import BOT_TOKEN 
    
    # Замени 'BOT_TOKEN' на токен твоего бота
    # Этот токен ты получаешь от BotFather, чтобы бот мог работать
bot = telebot.TeleBot(BOT_TOKEN)
    
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши что-нибудь!\nИспользуй /help чтобы узнать мои команды.")
    
@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")
    
@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")

@bot.message_handler(commands=['mem'])
def send_mem(message):
   # А вот так можно подставить имя файла из переменной!
    print(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:  
        bot.send_photo(message.chat.id, f)  


@bot.message_handler(commands=['eco'])
def send_eco(messege):
    bot.reply_to(message,"Привет вот твой сайте:  https://free-eco.ru/articles/top-20-ekologicheskih-saytov ")


@bot.message_handler(commands=['pass'])
def send_bye(message):  
    bot.reply_to(message, "Привет вот твой пароль:" +  gen_pass(10))


@bot.message_handler(commands=['emodji'])
def send_emodji(message):
    emodji = gen_emodji()
    bot.reply_to(message, f"Вот эмоджи': {emodji}")

@bot.message_handler(commands=['coin'])
def send_coin(message):
    coin = flip_coin()
    bot.reply_to(message, f"Монетка выпала так: {coin}")

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "Вот список команд, которые я понимаю:\n /start - начать общение с ботом\n /hello - поздороваться с ботом\n /bye - попрощаться с ботом\n /pass - сгенерировать пароль\n /emodji - получить случайный эмоджи\n /coin - подбросить монетку\n /mem - получить мем")


# Handle '/start' and '/help'
@bot.message_handler(commands=['say'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()


    


