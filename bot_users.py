import telebot
import main_users
import button_users
import database_users

bot = telebot.TeleBot(main_users.TOKEN)


# Reaction to start command
@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, "Добро пожаловать, " + message.from_user.first_name)
    button_users.start_button(message)


# Inquiry name
@bot.message_handler(func=lambda call: True)
def name(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(telebot.types.InlineKeyboardButton('Назад', callback_data='назад'))
    bot.edit_message_text(
        chat_id=message.chat.id, message_id=message.message_id,
        text='*Как вас будут видеть покупатели? Отправьте ответным сообщением.*', reply_markup=keyboard
    )
    bot.register_next_step_handler(message, database_users.start_button_database)


# Treatment start button
@bot.callback_query_handler(func=lambda call: True)
def start_button_call(call):

    if call.data == 'Пройти регистрацию':
        name(call.message)
    elif call.data == 'математика':
        database_users.math_logic_subject(call.message)
        button_users.reg_button(call.message)
    elif call.data == 'физика':
        database_users.fiz_logic_subject(call.message)
        button_users.reg_button(call.message)
    elif call.data == 'русский':
        database_users.rus_logic_subject(call.message)
        button_users.reg_button(call.message)


bot.polling()

try:
    bot.polling(none_stop=True)
except:
    pass
