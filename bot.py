import telebot
import main
import button
import database
import variable

bot = telebot.TeleBot(main.TOKEN)


# Reaction to start command
@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, "Добро пожаловать, " + message.from_user.first_name)
    button.start_button(message)


# Treatment start button
@bot.callback_query_handler(func=lambda call: True)
def start_button_call(call):
    if call.data == variable.school:
        button.school_button(call)
    if call.data == variable.student:
        button.student_button(call)
    if call.data == 'Назад_start':
        button.start_button_2(call.message)

    # Student buttons
    if call.data == variable.exam:
        button.student_button_exam(call)
    if call.data == variable.higher_mathematics:
        variable.x = 'math'
        variable.counter_performers = 0
        database.performers(call)
    if call.data == variable.physics_student:
        variable.x = 'fiz'
        database.performers(call)
#    if call.data == variable.mathematical_analysis:
#       variable.x = 'anal'
#      database.performers(call)
    if call.data == 'Предыдущая страница':
        variable.counter_performers = variable.counter_performers - variable.person_on_page
        if variable.counter_performers < 0:
            variable.counter_performers = 0
        database.performers(call)
    if call.data == 'Следующая страница':
        database.performers(call)
    for x in variable.list_people.values():
        if call.data == x:
            print(call.data)
            break
    bot.answer_callback_query(call.id)
    return variable.x


'''
@bot.callback_query_handler(func=lambda c: c.data == 'start_button')
async def process_callback_start_button(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query_id)
    await bot.send_message(callback_query.from_user.id, 'нажата кнопка')
'''
'''
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.send_message(message.chat.id, f'Добро пожаловать, {message.text}')
    pass
    return


@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)
'''

bot.polling()

try:
    bot.polling(none_stop=True)
except:
    pass
