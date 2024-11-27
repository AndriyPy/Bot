import telebot
from telebot import types
from key import keyy
import requests

open_weather_token = "84e3bdd118d81b2da08999fafe081dc9"

bot = telebot.TeleBot(keyy)


###############################################################keyboard кнопки######################################################################################
@bot.message_handler(commands=['start'])
def keybatton(message):
    if message.text == "/start":
        m = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id,
                         f"Hello!,{message.from_user.first_name}, rite the city where you want to see the weather, for example, Kyiv, Dubai, Rome",
                         reply_markup=m)


###############################################################inline кнопки#########################################################################################
def butt():
    menu1 = telebot.types.InlineKeyboardMarkup()
    tempbutt = telebot.types.InlineKeyboardButton(text='temperature', callback_data='temp')
    humidity = telebot.types.InlineKeyboardButton(text='humidity', callback_data='vologa')
    pressure = telebot.types.InlineKeyboardButton(text='pressure', callback_data='tisk')
    maxtemp = telebot.types.InlineKeyboardButton(text='maxtemp', callback_data='maxtemp')
    mintemp = telebot.types.InlineKeyboardButton(text='mintemp', callback_data='mintemp')
    wind = telebot.types.InlineKeyboardButton(text='wind', callback_data='wind')
    menu1.add(tempbutt, humidity, pressure, maxtemp, mintemp, wind)
    return menu1


temp = 0
vologa = 0
tisk = 0
maxtemp = 0
mintemp = 0
wind = 0
humidity = 0
pressure = 0



@bot.message_handler(content_types=['text'])
def get_weathe(message: types.Message):
    global temp
    global vologa
    global tisk
    global maxtemp
    global mintemp
    global wind
    global humidity
    global pressure
    message_trigger = True


    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric")
        data = r.json()

        city = data["name"]
        temp = data["main"]["temp"]
        # вологість
        humidity = data["main"]["humidity"]
        # тиск
        pressure = data["main"]["pressure"]
        maxtemp = data["main"]["temp_max"]
        mintemp = data["main"]["temp_min"]
        # вітер
        wind = data["wind"]["speed"]


        if message.text and message_trigger == True:
            print(message.text)
            bot.send_message(message.chat.id, "what do you want to see?", reply_markup=butt())
            message_trigger = False



    except Exception as ex:
        bot.send_message(message.chat.id, "check the city name")


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == 'vologa':
        bot.send_message(call.from_user.id, f"humidity: {humidity}")
        msg = bot.send_message(call.from_user.id, "what else do you want to see?", reply_markup=butt())
        bot.register_next_step_handler(msg, get_weathe)

    if call.data == "temp":
        bot.send_message(call.from_user.id, f"temperature: {temp}")
        msg = bot.send_message(call.from_user.id, "what else do you want to see?", reply_markup=butt())
        bot.register_next_step_handler(msg, get_weathe)

    if call.data == "tisk":
        bot.send_message(call.from_user.id, f"pressure: {pressure}")
        msg = bot.send_message(call.from_user.id, "what else do you want to see?", reply_markup=butt())
        bot.register_next_step_handler(msg, get_weathe)

    if call.data == "maxtemp":
        bot.send_message(call.from_user.id, f"maxtemp: {maxtemp}")
        msg = bot.send_message(call.from_user.id, "what else do you want to see?", reply_markup=butt())
        bot.register_next_step_handler(msg, get_weathe)

    if call.data == "mintemp":
        bot.send_message(call.from_user.id, f"mintemp: {mintemp}")
        msg = bot.send_message(call.from_user.id, "what else do you want to see?", reply_markup=butt())
        bot.register_next_step_handler(msg, get_weathe)

    if call.data == "wind":
        bot.send_message(call.from_user.id, f"wind: {wind}")
        msg = bot.send_message(call.from_user.id, "what else do you want to see?", reply_markup=butt())
        bot.register_next_step_handler(msg, get_weathe)


bot.polling(none_stop=True)



