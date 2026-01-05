import  telebot
from telebot import types
bot = telebot.TeleBot('8577236396:AAE8xgu6J9IayQnLGrzi6vwsZPZVjW_NIuw')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Перейти на сайт')
    btn2 = types.KeyboardButton('Иди нахуй')
    markup.row(btn1, btn2)
    markup.add()

    bot.send_message(message.chat.id,'Салам брат, пришли фоточку🥰😘',reply_markup=markup)
    bot.register_next_step_handler(message,on_click)
def on_click(message):
    if message.text == 'Перейти на сайт':
        bot.send_message(message.chat.id, 'https://clck.ru/3RAATL')
    elif message.text == 'Иди нахуй':
        bot.send_message(message.chat.id,f'Слыш {message.from_user.first_name} ты че охуел')
@bot.message_handler(commands=['start','gey'])
def send(message):
    bot.send_message(message.chat.id, f'{message.from_user.first_name} ,а ты знал что тамик гей!?')

@bot.message_handler(commands=['help'])
def send(message):
    bot.send_message(message.chat.id, 'Я не буду тебе помогать 8=D')
@bot.message_handler(commands=['ID'])
def send(message):
    bot.send_message(message.chat.id,f'ID:{message.from_user.id}')
@bot.message_handler(content_types=['photo','video','audio'])
def send(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Удалить фото',callback_data='delete')
    btn2 = types.InlineKeyboardButton('Иди нахуй', callback_data='edit')
    markup.row(btn1, btn2)
    markup.add()

    bot.reply_to(message,'Я в ахуе, ну ты и урод',reply_markup=markup)
@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id,callback.message.message_id - 1)
    elif callback.data == 'edit':
        bot.edit_message_text('Ладно прости',callback.message.chat.id,callback.message.message_id)
bot.polling(none_stop=True)
