import telebot
import main
import variable

bot = telebot.TeleBot(main.TOKEN)


# Hello button
@bot.message_handler(func=lambda message: True)
def start_button(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton('Школьник', callback_data=variable.school),
        telebot.types.InlineKeyboardButton('Студент', callback_data=variable.student)
    )

    bot.send_message(message.chat.id, '*Кто ты?*', parse_mode='MarkdownV2', reply_markup=keyboard)


# Help hello button
@bot.message_handler(func=lambda message: True)
def start_button_2(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton('Школьник', callback_data=variable.school),
        telebot.types.InlineKeyboardButton('Студент', callback_data=variable.student)
    )

    # Edit text and button
    bot.edit_message_text(
        chat_id=message.chat.id, message_id=message.message_id,
        text='*Кто ты?*', parse_mode='MarkdownV2', reply_markup=keyboard
    )


# School button
@bot.message_handler(func=lambda message: True)
def school_button(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton('Контрольная работа', callback_data='Контрольная работа'),
        telebot.types.InlineKeyboardButton('Домашняя работа', callback_data='Домашняя работа')
    )

    keyboard.row(telebot.types.InlineKeyboardButton('Назад', callback_data='Назад_start'))

    # Edit text and button
    bot.edit_message_text(
        chat_id=call.message.chat.id, message_id=call.message.message_id,
        text='*Выберите предмет:*', parse_mode='MarkdownV2', reply_markup=keyboard
    )


# Student button
@bot.message_handler(func=lambda message: True)
def student_button(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(telebot.types.InlineKeyboardButton('Экзамены', callback_data=variable.exam))
    keyboard.row(telebot.types.InlineKeyboardButton('Курсовая работа', callback_data='Курсовая работа'))
    keyboard.row(telebot.types.InlineKeyboardButton('Контрольная работа', callback_data='Контрольная работа'))
    keyboard.row(telebot.types.InlineKeyboardButton('Домашняя работа', callback_data='Домашняя работа'))

    keyboard.row(telebot.types.InlineKeyboardButton('Назад', callback_data='Назад_start'))

    # Edit text and button
    bot.edit_message_text(
        chat_id=call.message.chat.id, message_id=call.message.message_id,
        text='*Студент➡\nВыберите вид работы:*', parse_mode='MarkdownV2', reply_markup=keyboard
    )


# Exam button
@bot.message_handler(func=lambda message: True)
def student_button_exam(call):
    variable.counter_performers = 0
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(telebot.types.InlineKeyboardButton('⭐ Высшая математика', callback_data=variable.higher_mathematics))
    keyboard.row(
        telebot.types.InlineKeyboardButton('⭐ Математисекий анализ', callback_data=variable.mathematical_analysis))
    keyboard.row(telebot.types.InlineKeyboardButton('⭐ Физика', callback_data=variable.physics_student))

    keyboard.row(telebot.types.InlineKeyboardButton('Назад', callback_data=variable.student))

    # Edit text and button
    bot.edit_message_text(
        chat_id=call.message.chat.id, message_id=call.message.message_id,
        text='*Студент➡Экзамены➡\nВыберите предмет:*', parse_mode='MarkdownV2', reply_markup=keyboard
    )


# List of performers (right swipe)
@bot.message_handler(func=lambda message: True)
def list_of_performer_right(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    dictionary_length = len(variable.list_people)
    for i in range(variable.person_on_page):
        x = variable.list_people.pop(f'var{variable.counter_performers}')
        keyboard.row(telebot.types.InlineKeyboardButton(x, callback_data=x))
        print('счетчик 1 - ' + str(variable.counter_performers))
        print('длина словаря - ' + str(dictionary_length))
        if variable.counter_performers < dictionary_length - 1:
            variable.counter_performers += 1
        else:
            if variable.counter_performers < variable.person_on_page or \
                    dictionary_length == variable.person_on_page and variable.counter_performers == dictionary_length:
                keyboard.row(telebot.types.InlineKeyboardButton('Назад к предметам', callback_data=variable.exam))
            else:
                keyboard.row(telebot.types.InlineKeyboardButton('⬅', callback_data='Предыдущая страница'),
                             telebot.types.InlineKeyboardButton('Назад к предметам', callback_data=variable.exam)
                             )
            break
        if variable.counter_performers % variable.person_on_page == 0 or variable.counter_performers == dictionary_length:
            if variable.counter_performers < variable.person_on_page or \
                    dictionary_length == variable.person_on_page and variable.counter_performers == dictionary_length:
                keyboard.row(telebot.types.InlineKeyboardButton('Назад к предметам', callback_data=variable.exam))
            elif variable.counter_performers <= variable.person_on_page:
                keyboard.row(telebot.types.InlineKeyboardButton('Назад к предметам', callback_data=variable.exam),
                             telebot.types.InlineKeyboardButton('➡', callback_data='Следующая страница')
                             )
            elif dictionary_length - variable.counter_performers <= 0:
                keyboard.row(telebot.types.InlineKeyboardButton('⬅', callback_data='Предыдущая страница'),
                             telebot.types.InlineKeyboardButton('Назад к предметам', callback_data=variable.exam)
                             )
            elif variable.person_on_page < variable.counter_performers:
                keyboard.row(telebot.types.InlineKeyboardButton('⬅', callback_data='Предыдущая страница'),
                             telebot.types.InlineKeyboardButton('Назад к предметам', callback_data=variable.exam),
                             telebot.types.InlineKeyboardButton('➡', callback_data='Следующая страница')
                             )
    bot.edit_message_text(
        chat_id=call.message.chat.id, message_id=call.message.message_id,
        text='*Студент➡Экзамены➡Высшая мактематика\nИсполнители:*', parse_mode='MarkdownV2', reply_markup=keyboard
    )
    return variable.counter_performers


# List of performers (left swipe)
@bot.message_handler(func=lambda message: True)
def list_of_performer_left(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    dictionary_length = len(variable.list_people_2)
    variable.counter_performers = variable.counter_performers - variable.person_on_page
    for i in range(variable.person_on_page):
        x = variable.list_people_2.pop(f'var{variable.counter_performers}')
        keyboard.row(telebot.types.InlineKeyboardButton(x, callback_data=x))
        print(variable.counter_performers)
        if variable.counter_performers < dictionary_length - 1:
            variable.counter_performers += 1
        else:
            if variable.counter_performers < variable.person_on_page or \
                    dictionary_length == variable.person_on_page and variable.counter_performers == dictionary_length:
                keyboard.row(telebot.types.InlineKeyboardButton('Назад к предметам', callback_data=variable.exam))
            else:
                keyboard.row(telebot.types.InlineKeyboardButton('⬅', callback_data='Предыдущая страница'),
                             telebot.types.InlineKeyboardButton('Назад к предметам', callback_data=variable.exam)
                             )
            break
        if variable.counter_performers % variable.person_on_page == 0 or variable.counter_performers == dictionary_length:
            if variable.counter_performers < variable.person_on_page or \
                    dictionary_length == variable.person_on_page and variable.counter_performers == dictionary_length:
                keyboard.row(telebot.types.InlineKeyboardButton('Назад к предметам', callback_data=variable.exam))
            elif variable.counter_performers <= variable.person_on_page:
                keyboard.row(telebot.types.InlineKeyboardButton('Назад к предметам', callback_data=variable.exam),
                             telebot.types.InlineKeyboardButton('➡', callback_data='Следующая страница')
                             )
            elif dictionary_length - variable.counter_performers <= 0:
                keyboard.row(telebot.types.InlineKeyboardButton('⬅', callback_data='Предыдущая страница'),
                             telebot.types.InlineKeyboardButton('Назад к предметам', callback_data=variable.exam)
                             )
            elif variable.person_on_page < variable.counter_performers:
                keyboard.row(telebot.types.InlineKeyboardButton('⬅', callback_data='Предыдущая страница'),
                             telebot.types.InlineKeyboardButton('Назад к предметам', callback_data=variable.exam),
                             telebot.types.InlineKeyboardButton('➡', callback_data='Следующая страница')
                             )
    bot.edit_message_text(
        chat_id=call.message.chat.id, message_id=call.message.message_id,
        text='*Студент➡Экзамены➡Высшая мактематика\nИсполнители:*', parse_mode='MarkdownV2', reply_markup=keyboard
    )
