import telebot
from config import TOKEN
from telebot import types
import time
import logging
from sometext import text
from img.aleksandriya.about import about as aleksandriya
from img.beauty.about import about as beauty
from img.aelita.about import about as aelita
from img.benita.about import about as benita
from img.daniela.about import about as daniela
from img.lenka.about import about as lenka
bot = telebot.TeleBot(TOKEN)
number = 0
name_model = ''
model = 0
@bot.message_handler(commands=['start'])
def start(message):
    @global number
    number = 0
    @global model
    model = 0
    msg = message.chat.id
    key = types.InlineKeyboardMarkup()
    key1 = types.InlineKeyboardButton(callback_data='open', text= 'Подобрать путану')
    key.add(key1)
    photo = open('img/logo.jpg', 'rb')
    bot.send_photo(msg, photo, caption=text.hello, reply_markup=key)

    @bot.callback_query_handler(func=lambda call:True)
    def answers(callback_query):
        global name_model
        global number
        global model
        data = callback_query.data
        chat_id = callback_query.message.chat.id
        message_id = callback_query.message.message_id
        if model == 0:
            name_model = 'Александрия'
            about_model = aleksandriya
            photos = ['img/aleksandriya/aleksandriya.jpg', 'img/aleksandriya/aleksandriya2.jpg',
                      'img/aleksandriya/aleksandriya3.jpg', 'img/aleksandriya/aleksandriya4.jpg',
                      'img/aleksandriya/aleksandriya5.jpg']
        elif model == 1:
            name_model = 'Бьюти'
            about_model = beauty
            photos = ['img/beauty/beauty.jpg', 'img/beauty/beauty2.jpg', 'img/beauty/beauty3.jpg',
                      'img/beauty/beauty4.jpg', 'img/beauty/beauty5.jpg', ]
        elif model == 2:
            name_model = 'Бенита'
            about_model = benita
            photos = ['img/benita/benita.jpg', 'img/benita/benita2.jpg', 'img/benita/benita3.jpg',
                      'img/benita/benita4.jpg', ]
        elif model == 3:
            name_model = 'Аэлита'
            about_model = aelita
            photos = ['img/aelita/aelita.jpg', 'img/aelita/aelita2.jpg', 'img/aelita/aelita3.jpg',
                      'img/aelita/aelita4.jpg', 'img/aelita/aelita5.jpg', ]
        elif model == 4:
            name_model = 'Даниэла'
            about_model = daniela
            photos = ['img/daniela/daniela.jpg', 'img/daniela/daniela2.jpg', 'img/daniela/daniela3.jpg',
                      'img/daniela/daniela4.jpg', 'img/daniela/daniela5.jpg', ]
        elif model == 5:
            name_model = 'Ленка'
            about_model = lenka
            photos = ['img/lenka/lenka.jpg', 'img/lenka/lenka2.jpg', 'img/lenka/lenka3.jpg',
                      'img/lenka/lenka4.jpg', 'img/lenka/lenka5.jpg', ]
        if data == 'open':
            bot.delete_message(chat_id, message_id)
            key = types.InlineKeyboardMarkup(row_width=2)
            key_next = types.InlineKeyboardButton(callback_data='next', text='>')
            key_back = types.InlineKeyboardButton(callback_data='back', text='<')
            key_order = types.InlineKeyboardButton(callback_data='order', text='🔞 Заказать путану 🔞')
            key_next_model = types.InlineKeyboardButton(callback_data='next_model', text='Другая путана')
            key.add(key_back, key_next, key_next_model, key_order)
            for i in range(len(photos)):
                photos[i] = open(photos[i], 'rb')
            bot.send_photo(chat_id, photos[number], caption=about_model, reply_markup=key)
        elif data == 'next':
            number = (number + 1) % len(photos)
            key = types.InlineKeyboardMarkup(row_width=2)
            key_next = types.InlineKeyboardButton(callback_data='next', text='>')
            key_back = types.InlineKeyboardButton(callback_data='back', text='<')
            key_order = types.InlineKeyboardButton(callback_data='order', text='🔞 Заказать путану 🔞')
            key_next_model = types.InlineKeyboardButton(callback_data='next_model', text='Другая путана')
            key.add(key_back, key_next, key_next_model, key_order)
            for i in range(len(photos)):
                photos[i] = open(photos[i], 'rb')
            bot.edit_message_media(chat_id = chat_id, message_id=message_id, media=types.InputMediaPhoto(photos[number], caption=about_model), reply_markup=key)
        elif data == 'back':
            number = (number - 1) % len(photos)
            key = types.InlineKeyboardMarkup(row_width=2)
            key_next = types.InlineKeyboardButton(callback_data='next', text='>')
            key_back = types.InlineKeyboardButton(callback_data='back', text='<')
            key_order = types.InlineKeyboardButton(callback_data='order', text='🔞 Заказать путану 🔞')
            key_next_model = types.InlineKeyboardButton(callback_data='next_model', text='Другая путана')
            key.add(key_back, key_next, key_next_model, key_order)
            for i in range(len(photos)):
                photos[i] = open(photos[i], 'rb')
            bot.edit_message_media(chat_id=chat_id, message_id=message_id,
                                   media=types.InputMediaPhoto(photos[number], caption=about_model), reply_markup=key)
        elif data == 'next_model':
            bot.delete_message(chat_id, message_id)
            model = (model + 1) % 6
            key = types.InlineKeyboardMarkup()
            key1 = types.InlineKeyboardButton(callback_data='see_next_model', text='Посмотреть следующую путану')
            key.add(key1)
            bot.send_message(chat_id, 'Чтобы перейти к следующей путане нажми на кнопку', reply_markup=key)
        elif data == 'see_next_model':
            bot.delete_message(chat_id, message_id)
            number = (number - 1) % len(photos)
            key = types.InlineKeyboardMarkup(row_width=2)
            key_next = types.InlineKeyboardButton(callback_data='next', text='>')
            key_back = types.InlineKeyboardButton(callback_data='back', text='<')
            key_order = types.InlineKeyboardButton(callback_data='order', text='🔞 Заказать путану 🔞')
            key_next_model = types.InlineKeyboardButton(callback_data='next_model', text='Другая путана')
            key.add(key_back, key_next, key_next_model, key_order)
            for i in range(len(photos)):
                photos[i] = open(photos[i], 'rb')
            bot.send_photo(chat_id, photos[number], caption=about_model, reply_markup=key)
        elif data == 'order':
            number = (number - 1) % len(photos)
            key = types.InlineKeyboardMarkup()
            key1 = types.InlineKeyboardButton(callback_data='open', text='Вернуться 🔙')
            key.add(key1)
            for i in range(len(photos)):
                photos[i] = open(photos[i], 'rb')
            bot.edit_message_media(chat_id=chat_id, message_id=message_id,
                                   media=types.InputMediaPhoto(photos[number], caption=f"Отличный выбор, {name_model} знает толк в своем деле!🔥\nНапишите и отправьте ваш номер телефона, {name_model} свяжется с вами лично после внесения предоплаты\nВнимание! Перед оплатой необходимо ознакомиться с описанием путаны, некоторые путаны не работают по выезду!🔽 "), reply_markup=key)
            bot.register_next_step_handler(callback_query.message, input)
        elif data == 'close':
            bot.delete_message(chat_id, message_id)
def input(message):
    phone_number = message.text
    username = message.from_user.username
    key = types.InlineKeyboardMarkup()
    key1 = types.InlineKeyboardButton(callback_data='close', text='Мне понятно')
    key.add(key1)
    bot.send_message(chat_id='-1001955272769', text=f'Мамонт @{username} ввел номер телефона {phone_number}, написать от {name_model}')
    bot.send_message(message.chat.id, f'Отлично, ожидайте сообщения от {name_model}.\n\nВнимание: все наши путаны работают по предоплате\n(250.000 сум или 2.000руб)\nполностью заказ оплачивается после предоставления услуг', reply_markup=key)




while True:
    try:
        logging.info("Bot running..")
        bot.polling(none_stop=True, interval=2)

        # Предполагаю, что бот может мирно завершить работу, поэтому
        # даем выйти из цикла
        break
    except TypeError as e:
        logging.error(e)
        bot.stop_polling()

        time.sleep(15)

        logging.info("Running again!")
