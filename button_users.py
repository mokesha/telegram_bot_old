import telebot
import main_users
import variable_users
import sqlite3

bot = telebot.TeleBot(main_users.TOKEN)


# Hello button
@bot.message_handler(func=lambda message: True)
def start_button(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(telebot.types.InlineKeyboardButton('Пройти регистрацию', callback_data='Пройти регистрацию'))

    bot.send_message(message.chat.id, '*Пройдите регистрацию*', parse_mode='MarkdownV2', reply_markup=keyboard)


# Registration button12
@bot.message_handler(func=lambda message: True)
def reg_button1(message):
    start_logic_subject(message)
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton(variable_users.math, callback_data='математика'),
        telebot.types.InlineKeyboardButton(variable_users.fiz, callback_data='физика')
    )
    keyboard.row(telebot.types.InlineKeyboardButton(variable_users.rus, callback_data='русский'))

    # Edit text and button
    bot.send_message(message.chat.id, '*Выберите предметы*', parse_mode='MarkdownV2', reply_markup=keyboard)


# Registration button
@bot.message_handler(func=lambda message: True)
def reg_button(message):
    start_logic_subject(message)
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton(variable_users.math, callback_data='математика'),
        telebot.types.InlineKeyboardButton(variable_users.fiz, callback_data='физика')
    )
    keyboard.row(telebot.types.InlineKeyboardButton(variable_users.rus, callback_data='русский'))

    # Edit text and button
    bot.edit_message_text(
        chat_id=message.chat.id, message_id=message.message_id,
        text='*Выберите предметы*', parse_mode='MarkdownV2', reply_markup=keyboard
    )


# Check name buttons
@bot.message_handler(func=lambda message: True)
def start_logic_subject(message):
    conn = sqlite3.connect('button_user.db')
    with conn:
        cur = conn.cursor()
        cur.execute(f"SELECT `{variable_users.math1}` FROM button_user WHERE userid = {message.chat.id}")
        if cur.fetchall() == [(0,)]:
            variable_users.math = 'Математика ⬜'
        else:
            variable_users.math = 'Математика ✅'
        cur.execute(f"SELECT `{variable_users.fiz1}` FROM button_user WHERE userid = {message.chat.id}")
        if cur.fetchall() == [(0,)]:
            variable_users.fiz = 'Физика ⬜'
        else:
            variable_users.fiz = 'Физика ✅'
        cur.execute(f"SELECT `{variable_users.rus1}` FROM button_user WHERE userid = {message.chat.id}")
        if cur.fetchall() == [(0,)]:
            variable_users.rus = 'Русский ⬜'
        else:
            variable_users.rus = 'Русский ✅'
    conn.commit()
    cur.close()
    return variable_users.math
