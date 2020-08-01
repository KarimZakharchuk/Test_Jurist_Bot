import telebot
from telebot import types

TOKEN = '1331485304:AAEZ4Ufg58rwOxov0MuyxlUF_JAoufyBT-Y'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
	item1 = types.KeyboardButton("Гражданский кодекс Украины")
	item2 = types.KeyboardButton("Гражданский процессуальный кодекс")
	item3 = types.KeyboardButton("Жилищный кодекс Украины")

	item4 = types.KeyboardButton("Земельный кодекс Украины")
	item5 = types.KeyboardButton("Семейный кодекс Украины")
	item6 = types.KeyboardButton("Лесной кодекс Украины")

	item7 = types.KeyboardButton("Уголовный кодекс Украины")
	item8 = types.KeyboardButton("КЗоТ - Кодекс законов о труде")
	item9 = types.KeyboardButton("Кодекс Украины о недрах")

	item10 = types.KeyboardButton("Водный кодекс Украины")
	item11 = types.KeyboardButton("Воздушный кодекс Украины")
	item12 = types.KeyboardButton("Налоговый кодекс Украины")

	markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12)

	bot.send_message(message.chat.id, "Hello <b>{0.first_name}</b>".format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)

@bot.message_handler(commands=['help'])
def userHelp(message):
	bot.send_message(message.chat.id, "I am Jurist Bot. I help you in your question :)")



bot.polling()
