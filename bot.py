import telebot
from telebot import types
from parsing import parsing
from decouple import config


bot = telebot.TeleBot(config('TOKEN'))


'''Старт'''
@bot.message_handler(commands=['start'])
def start_message(message):
    '''Информация о пользователе'''
    chat_id = message.chat.id
    username = message.from_user.first_name

    '''Создание кнопок'''
    inline_keyboard_see_quit = types.InlineKeyboardMarkup()
    start_botton = types.InlineKeyboardButton('Посмотреть', callback_data='see')
    quit_botton = types.InlineKeyboardButton('Закрыть', callback_data='quit')
    inline_keyboard_see_quit.add(start_botton, quit_botton)

    bot.send_message(chat_id, f'Здравствуйте, {username}! Этот бот может оправить вам: "кодекс кыргызской республики о нарушениях от 13 апреля 2017 года № 58".', reply_markup=inline_keyboard_see_quit)


# '''Кнопки для заголовков'''
# from parsing import titles
# inline_keyboard_titles = types.InlineKeyboardMarkup()
# for i, title in enumerate(titles):
#     print(i, title)
#     btn = types.InlineKeyboardButton(title, callback_data=i)
#     inline_keyboard_titles.add(btn)

'''Реакция на кнопки'''
@bot.callback_query_handler(func=lambda c: True)
def inline(c):
    chat_id = c.message.chat.id
    message_id = c.message.id
    if c.data=='quit':
        bot.delete_message(chat_id, message_id)
    if c.data=='see':
        from parsing import titles
        titles_ = '\n'.join(titles)
        bot.send_message(chat_id, titles_)
        
bot.polling()