from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    Application,

    CallbackQueryHandler,

    CommandHandler,

    ContextTypes,

    ConversationHandler,

)

import requests

url = 'http://t.me/MontenegroDrive_bot'
APIToken = '5745195636:AAEFMDzOgCn2X78UNUX_kqo6JpBxkFayz9g'
data = requests.get(url) # requests data from API
#data = data.json() # converts return data to json

 

def driver_info():
    # initializing driver DB entry
    query = update.callback_query
    #here comes initial message "where are you coming from" Bar/Budva/Tivat/Podgorica/HN
    bot.send_message(chat_id=user_id, text='Откуда выезжаете?')
    keyboard = [
            [
                InlineKeyboardButton("Бар", callback_data="Bar"),
                InlineKeyboardButton("Будва", callback_data="Budva"),
                InlineKeyboardButton("Тиват", callback_data="Tivat"),
                InlineKeyboardButton("Герцег-Нови", callback_data="HN"),
                InlineKeyboardButton("Подгорица", callback_data="Podgorica")
            ]
        ]
    Driver_loc_start = CallbackQueryHandler(callback)
    #where are you going?
    bot.send_message(chat_id=user_id, text='Куда едете?')
    keyboard = [
            [
                InlineKeyboardButton("Босния (Требинье)", callback_data="Bosnia"),
                InlineKeyboardButton("Албания (Шкодер)", callback_data="Albania"),
            ]
        ]
    Driver_loc_end = CallbackQueryHandler(callback)

    #how many spaces?
    bot.send_message(chat_id=user_id, text='Сколько мест?')
    Driver_Space = update.Message.ReplyToMessage.Text 

    #date
    bot.send_message(chat_id=user_id, text='Когда и во сколько?')
    Driver_Date = update.Message.ReplyToMessage.Text 

    #Price?
    bot.send_message(chat_id=user_id, text='Стоимость 1 места?')
    Driver_Price = update.Message.ReplyToMessage.Text 

    #Quick?
    bot.send_message(chat_id=user_id, text='Быстрый визаран (туда и обратно?)')
    keyboard = [
            [
                InlineKeyboardButton("Да", callback_data="1"),
                InlineKeyboardButton("Нет", callback_data="0"),
            ]
        ]
    Driver_Quick_run = CallbackQueryHandler(callback)

    #заезд в другие города 
    bot.send_message(chat_id=user_id, text='Заезжаете в другие города по пути?')
    keyboard = [
            [
                InlineKeyboardButton("Да", callback_data="1"),
                InlineKeyboardButton("Нет", callback_data="0"),
            ]
        ]
    Driver_pickup_other_cities = CallbackQueryHandler(callback)

    #return info
    bot.send_message(chat_id=user_id, text='Проверим ваши данные?')
    check_info = f"Location start: {Driver_loc_start}, Location end: {Driver_loc_end}, Spaces: {Driver_Space}, Price: {Driver_Price}, Quick: {Driver_Quick_run}"

    bot.send_message(chat_id=user_id, text='Все верно?')

    keyboard = [
            [
                InlineKeyboardButton("Да", callback_data="1"),
                InlineKeyboardButton("Нет", callback_data="0"),
            ]
        ]


async def start(update, context):
    keyboard = [
        [
            InlineKeyboardButton("Водитель", callback_data="driver"),
            InlineKeyboardButton("Пассажир", callback_data="passenger"),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Пожалуйста выберите!", reply_markup=reply_markup)
    init_choice = CallbackQueryHandler(callback)
    if init_choice == "driver":
        driver_info()
    
def main():
    application = Application.builder().token(APIToken).build()
    application.add_handler(CommandHandler("start", start))
#    application.add_handler(CallbackQueryHandler())
    

if __name__ == '__main__':
    main()

