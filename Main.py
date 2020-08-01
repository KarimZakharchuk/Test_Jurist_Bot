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

    bot.send_message(message.chat.id, "Привет, <b>{0.first_name}</b>".format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)

@bot.message_handler(commands=['help'])
def userHelp(message):
    bot.send_message(message.chat.id, "Я помогу тебе с законом :)")

@bot.message_handler(content_types=["text"])
def userText(message):
    if message.text == "Гражданский кодекс Украины":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        item1 = types.KeyboardButton("Общие положения Гражданского кодекса")
        item2 = types.KeyboardButton("Личные неимущественные права физического лица")
        item3 = types.KeyboardButton("Право собственности и прочие вещные права")
        item4 = types.KeyboardButton("Право интеллектуальной собственности")
        item5 = types.KeyboardButton("Обязательственное право")
        item6 = types.KeyboardButton("Наследственное право")

        markup.add(item1,item2,item3,item4,item5,item6)
        bot.send_message(message.chat.id, "Выберете категорию", reply_markup=markup)

    if message.text == "Общие положения Гражданского кодекса":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        item1 = types.KeyboardButton("Основные положения")
        item2 = types.KeyboardButton("Лица")
        item3 = types.KeyboardButton("Объекты гражданских прав")
        item4 = types.KeyboardButton("Сделки. Представительство")
        item5 = types.KeyboardButton("Сроки. Исковая давность")
        markup.add(item1,item2,item3,item4,item5)
        bot.send_message(message.chat.id, "Какой раздел интересен?", reply_markup=markup)

    if message.text == "Основные положения":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        item1 = types.KeyboardButton("Гражданское законодательство Украины")
        item2 = types.KeyboardButton("Основания возникновения гражданских прав и обязанностей. Осуществление гражданских прав и выполнение обязанностей")
        item3 = types.KeyboardButton("Защита гражданских прав и интересов")
        markup.add(item1,item2,item3)
        bot.send_message(message.chat.id, "Раздел 1 - Основные положения. Какая глава интересна?", reply_markup=markup)

    if message.text == "Лица":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        item1 = types.KeyboardButton("Физическое лицо")
        item2 = types.KeyboardButton("Юридическое лицо")
        item3 = types.KeyboardButton("Участие государства, АР Крым, территориальных общин в гражданских отношениях")
        markup.add(item1,item2,item3)
        bot.send_message(message.chat.id, "Раздел 2 - Лица. Какой Подраздел интересен?", reply_markup=markup)

    if message.text == "Физическое лицо":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        item1 = types.KeyboardButton("Общие положения о физическом лице")
        item2 = types.KeyboardButton("Физическое лицо - предприниматель")
        item3 = types.KeyboardButton("Опека и попечительство")
        markup.add(item1,item2,item3)
        bot.send_message(message.chat.id, "Подраздел 1 - Физическое лицо. Какая глава интересна?", reply_markup=markup)

    if message.text == "Юридическое лицо":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        item1 = types.KeyboardButton("Общие положения о юридическом лице")
        item2 = types.KeyboardButton("Предпринимательские общества")
        markup.add(item1,item2)
        bot.send_message(message.chat.id, "Подраздел 2 - Юридическое лицо. Какая глава интересна?", reply_markup=markup)

    if message.text == "Участие государства, АР Крым, территориальных общин в гражданских отношениях":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        item1 = types.KeyboardButton("Правовые формы Участия государства, АР Крым, территориальных общин в гражданских отношениях")
        item2 = types.KeyboardButton("Органы и представители, через которые действуют государство, АР Крым, территориальные общины в гражданских отношениях")
        item3 = types.KeyboardButton("Ответственность по обязательствам государства, АР Крым, территориальных общин")
        markup.add(item1,item2,item3)
        bot.send_message(message.chat.id, "Подраздел 3 - Участие государства, АР Крым, территориальных общин в гражданских отношениях. Какая глава интересна?", reply_markup=markup)

    if message.text == "Объекты гражданских прав":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        item1 = types.KeyboardButton("Общие положения об объектах гражданских прав")
        item2 = types.KeyboardButton("Вещи. Имущество")
        item3 = types.KeyboardButton("Ценные бумаги")
        item4 = types.KeyboardButton("Нематериальные блага")
        markup.add(item1,item2,item3,item4)
        bot.send_message(message.chat.id, "Раздел 3 - Объекты гражданских прав. Какая глава интересна?", reply_markup=markup)

    if message.text == "Сделки. Представительство":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        item1 = types.KeyboardButton("Сделки")
        item2 = types.KeyboardButton("Представительство")
        markup.add(item1,item2)
        bot.send_message(message.chat.id, "Раздел 4 - Сделки. Представительство. Какая глава интересна?", reply_markup=markup)

    if message.text == "Сроки. Исковая давность":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        item1 = types.KeyboardButton("Определение и вычисление сроков")
        item2 = types.KeyboardButton("Исковая давность")
        markup.add(item1,item2)
        bot.send_message(message.chat.id, "Раздел 5 - Сроки. Исковая давность. Какая глава интересна?", reply_markup=markup)


        

    elif message.text == "Гражданский процессуальный кодекс":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        item1 = types.KeyboardButton("Общие положения")
        item2 = types.KeyboardButton("Приказное производство")
        item3 = types.KeyboardButton("Исковое производство")
        item4 = types.KeyboardButton("Отдельное производство")
        item5 = types.KeyboardButton("Пересмотр судебных решений")
        item6 = types.KeyboardButton("Процессуальные вопросы связанные с выполнением судебных решений по гражданским делам и решений других органов (должностных лиц)")
        item7 = types.KeyboardButton("Судебный контроль за исполнением судебных решений")
        item8 = types.KeyboardButton("Производство по делам об обжаловании решений третейских судов и о выдаче исполнительных листов на принудительное выполнение решений третейских судов")
        item9 = types.KeyboardButton("О признании и исполнении решений иностранных судов в Украине")
        item10 = types.KeyboardButton("Восстановление утраченного судебного производства")
        item11 = types.KeyboardButton("Производство по делам при участии иностранных лиц")
        item12 = types.KeyboardButton("Заключительные и переходные положения")


        markup.add(item1,item2,item3,item4,item5,item6,item7,item8,item9,item10,item11,item12)
        bot.send_message(message.chat.id, "Выберете категорию", reply_markup=markup)

    elif message.text == "Жилищный кодекс Украины":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        item1 = types.KeyboardButton("Общие положения")
        item2 = types.KeyboardButton("Управление жилым фондом")
        item3 = types.KeyboardButton("Обеспечение граждан жилыми помещениями. Пользование жилыми помещениями")
        item4 = types.KeyboardButton("Обеспечение сохранности жилищного фонда, его эксплуатация и ремонт")
        item5 = types.KeyboardButton("Ответственность за нарушение жилищного законодательства")
        item6 = types.KeyboardButton("Решение жилищных споров")
        item6 = types.KeyboardButton("Заключительные положения")

        markup.add(item1,item2,item3,item4,item5,item6,item7)
        bot.send_message(message.chat.id, "Выберете категорию", reply_markup=markup)

    elif message.text == "Земельный кодекс Украины":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        item1 = types.KeyboardButton("Основная часть")
        item2 = types.KeyboardButton("Земли Украины")
        item3 = types.KeyboardButton("Права на землю")
        item4 = types.KeyboardButton("Получение и реализация права на землю")
        item5 = types.KeyboardButton("Гарантии прав на землю")
        item6 = types.KeyboardButton("Охрана земель")
        item7 = types.KeyboardButton("Управление в области использования и охраны земель")
        item8 = types.KeyboardButton("Ответственность за нарушение земельного законодательства")
        item9 = types.KeyboardButton("Заключительные положения")
        item10 = types.KeyboardButton("Переходные положения")

        markup.add(item1,item2,item3,item4,item5,item6,item7,item8,item9,item10)
        bot.send_message(message.chat.id, "Выберете категорию", reply_markup=markup)

    elif message.text == "Семейный кодекс Украины":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        item1 = types.KeyboardButton("Общие положения")
        item2 = types.KeyboardButton("Брак. Права и обязанности супругов")
        item3 = types.KeyboardButton("Права и обязанности матери, отца и ребенка")
        item4 = types.KeyboardButton("Устройство детей сирот и детей, лишенных родительской опеки")
        item5 = types.KeyboardButton("Права и обязанности других членов семьи и родственников")
        item6 = types.KeyboardButton("Особенности усыновления детей гражданами Украины, которые проживают за ее пределами, и иностранцами")
        item7 = types.KeyboardButton("Окончательные положения")

        markup.add(item1,item2,item3,item4,item5,item6,item7)
        bot.send_message(message.chat.id, "Выберете категорию", reply_markup=markup)

    elif message.text == "Лесной кодекс Украины":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        item1 = types.KeyboardButton("Общие положения")
        item2 = types.KeyboardButton("Государственное управление и государственный контроль в области охраны, защиты, использования и воссоздания лесов")
        item3 = types.KeyboardButton("Государственное регулирование и управление в сфере лесных отношений")
        item4 = types.KeyboardButton("Организация Лесного хозяйства")
        item5 = types.KeyboardButton("Ведение лесного хозяйства")
        item6 = types.KeyboardButton("Решение споров и ответственность за нарушение лесного законодательства")
        item7 = types.KeyboardButton("Международные отношения")
        item8 = types.KeyboardButton("Заключительные положения")

        markup.add(item1,item2,item3,item4,item5,item6,item7,item8)
        bot.send_message(message.chat.id, "Выберете категорию", reply_markup=markup)

    elif message.text == "Уголовный кодекс Украины":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        item1 = types.KeyboardButton("Общая часть")
        item2 = types.KeyboardButton("Особенная часть")
        item3 = types.KeyboardButton("Заключительные и переходные положения")

        markup.add(item1,item2,item3)
        bot.send_message(message.chat.id, "Выберете категорию", reply_markup=markup)

    elif message.text == "КЗоТ - Кодекс законов о труде":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        item1 = types.KeyboardButton("")
        item2 = types.KeyboardButton("")
        item3 = types.KeyboardButton("")
        item4 = types.KeyboardButton("")
        item5 = types.KeyboardButton("")
        item6 = types.KeyboardButton("")

        markup.add(item1,item2,item3,item4,item5,item6)
        bot.send_message(message.chat.id, "Выберете категорию", reply_markup=markup)

    elif message.text == "Кодекс Украины о недрах":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        item1 = types.KeyboardButton("")
        item2 = types.KeyboardButton("")
        item3 = types.KeyboardButton("")
        item4 = types.KeyboardButton("")
        item5 = types.KeyboardButton("")
        item6 = types.KeyboardButton("")

        markup.add(item1,item2,item3,item4,item5,item6)
        bot.send_message(message.chat.id, "Выберете категорию", reply_markup=markup)

    elif message.text == "Водный кодекс Украины":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        item1 = types.KeyboardButton("")
        item2 = types.KeyboardButton("")
        item3 = types.KeyboardButton("")
        item4 = types.KeyboardButton("")
        item5 = types.KeyboardButton("")
        item6 = types.KeyboardButton("")

        markup.add(item1,item2,item3,item4,item5,item6)
        bot.send_message(message.chat.id, "Выберете категорию", reply_markup=markup)

    elif message.text == "Воздушный кодекс Украины":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        item1 = types.KeyboardButton("")
        item2 = types.KeyboardButton("")
        item3 = types.KeyboardButton("")
        item4 = types.KeyboardButton("")
        item5 = types.KeyboardButton("")
        item6 = types.KeyboardButton("")

        markup.add(item1,item2,item3,item4,item5,item6)
        bot.send_message(message.chat.id, "Выберете категорию", reply_markup=markup)

    elif message.text == "Налоговый кодекс Украины":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        item1 = types.KeyboardButton("")
        item2 = types.KeyboardButton("")
        item3 = types.KeyboardButton("")
        item4 = types.KeyboardButton("")
        item5 = types.KeyboardButton("")
        item6 = types.KeyboardButton("")

        markup.add(item1,item2,item3,item4,item5,item6)
        bot.send_message(message.chat.id, "Выберете категорию", reply_markup=markup)

    else:
        bot.send_message(message.chat.id, "Сделайте свой выбор!")

bot.polling()
