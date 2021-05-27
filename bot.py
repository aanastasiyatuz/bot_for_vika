import telebot
from telebot import types
from .parsing import parsing
from decouple import config

bot = telebot.TeleBot(config('TOKEN'))


'''Старт'''
@bot.message_handler(commands=['start'])
def start_message(message):
    '''Информация о пользователе'''
    chat_id = message.chat.id
    username = message.from_user.first_name

    '''Создание кнопок'''
    inline_keyboard = types.InlineKeyboardMarkup()
    start_botton = types.InlineKeyboardButton('See', callback_data='see')
    quit_botton = types.InlineKeyboardButton('Quit', callback_data='quit')
    inline_keyboard.add(start_botton, quit_botton)

    bot.send_message(chat_id, f"Hello {username}, I'm Kyrgyzstan news bot! Let's see what's happening now in Kyrgyzstan:", reply_markup=inline_keyboard)


# '''Реакция на кнопки'''
# @bot.callback_query_handler(func=lambda c: True)
# def inline(c):
#     chat_id = c.message.chat.id
#     message_id = c.message.id
#     if c.data=='quit':
#         bot.delete_message(chat_id, message_id)
#     if c.data=='see':
#         main()    #parsing
#         '''Cоздание кнопок'''
#         news = []
#         inline_keyboard_news = types.InlineKeyboardMarkup()
#         for new in main_data:
#             new = new['news']
#             news.append(new)
#         for i,n in enumerate(news, 1):
#             botton = types.InlineKeyboardButton(f'{i} : {n}', callback_data=f'{i}')
#             btn_photo = types.InlineKeyboardButton('See photo', callback_data=f'see_photo{i}') 
#             inline_keyboard_news.add(botton)
#             inline_keyboard_news.add(btn_photo)
#         '''Отправка новостей'''
#         msg = bot.send_message(chat_id, 'news:', reply_markup=inline_keyboard_news)

#     '''Отправить ссылку на новость'''
#     enumerate_ = [str(i) for i in range(1,17)]
#     if c.data in enumerate_:
#         try:
#             msg = main_data[int(c.data)-1]['link']
#             bot.send_message(chat_id, f'{msg}')
#         except IndexError:
#             pass
        
#     '''Отправить фотографию'''
#     for i in [str(i) for i in range(1,17)]:
#         if c.data==f'see_photo{i}':
#             try:
#                 msg = main_data[int(i)-1]['photo']
#                 if msg:
#                     bot.send_photo(chat_id, f'{msg}')
#                 else:
#                     bot.send_message(chat_id, 'Sorry, can\'t send you photo')
#             except IndexError:
#                 pass


bot.polling()