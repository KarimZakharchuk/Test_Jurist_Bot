import telebot
from telebot import types

from Jurist import *
#from stat import GKU_g_1

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
    #ГКУ(Гражданский кодекс Украины)
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

    if message.text == "Гражданское законодательство Украины":
        if len(GKU_g_1) > 4096:
            for x in range(0, len(GKU_g_1), 4096):
                bot.send_message(message.chat.id, GKU_g_1[x:x + 4096])
        else:
            bot.send_message(message.chat.id, GKU_g_1)

    if message.text == "Основания возникновения гражданских прав и обязанностей. Осуществление гражданских прав и выполнение обязанностей":
        if len(GKU_g_2) > 4096:
            for x in range(0, len(GKU_g_2), 4096):
                bot.send_message(message.chat.id, GKU_g_2[x:x + 4096])
        else:
            bot.send_message(message.chat.id, GKU_g_2)

    if message.text == "Защита гражданских прав и интересов":
        if len(GKU_g_3) > 4096:
            for x in range(0, len(GKU_g_3), 4096):
                bot.send_message(message.chat.id, GKU_g_3[x:x + 4096])
        else:
            bot.send_message(message.chat.id, GKU_g_3)
    
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

    if message.text == "Общие положения о физическом лице":
        if len(GKU_g_4) > 4096:
            for x in range(0, len(GKU_g_4), 4096):
                bot.send_message(message.chat.id, GKU_g_4[x:x + 4096])
        else:
            bot.send_message(message.chat.id, GKU_g_4)

    if message.text == "Физическое лицо - предприниматель":
        if len(GKU_g_5) > 4096:
            for x in range(0, len(GKU_g_5), 4096):
                bot.send_message(message.chat.id, GKU_g_5[x:x + 4096])
        else:
            bot.send_message(message.chat.id, GKU_g_5)

    if message.text == "Опека и попечительство":
        if len(GKU_g_6) > 4096:
            for x in range(0, len(GKU_g_6), 4096):
                bot.send_message(message.chat.id, GKU_g_6[x:x + 4096])
        else:
            bot.send_message(message.chat.id, GKU_g_6)

    if message.text == "Юридическое лицо":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        item1 = types.KeyboardButton("Общие положения о юридическом лице")
        item2 = types.KeyboardButton("Предпринимательские общества")
        markup.add(item1,item2)
        bot.send_message(message.chat.id, "Подраздел 2 - Юридическое лицо. Какая глава интересна?", reply_markup=markup)

    if message.text == "Общие положения о юридическом лице":
        if len(GKU_g_7) > 4096:
            for x in range(0, len(GKU_g_7), 4096):
                bot.send_message(message.chat.id, GKU_g_7[x:x + 4096])
        else:
            bot.send_message(message.chat.id, GKU_g_7)

    if message.text == "Предпринимательские общества":
        if len(GKU_g_8) > 4096:
            for x in range(0, len(GKU_g_8), 4096):
                bot.send_message(message.chat.id, GKU_g_8[x:x + 4096])
        else:
            bot.send_message(message.chat.id, GKU_g_8)

    if message.text == "Участие государства, АР Крым, территориальных общин в гражданских отношениях":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        item1 = types.KeyboardButton("Правовые формы Участия государства, АР Крым, территориальных общин в гражданских отношениях")
        item2 = types.KeyboardButton("Органы и представители, через которые действуют государство, АР Крым, территориальные общины в гражданских отношениях")
        item3 = types.KeyboardButton("Ответственность по обязательствам государства, АР Крым, территориальных общин")
        markup.add(item1,item2,item3)
        bot.send_message(message.chat.id, "Подраздел 3 - Участие государства, АР Крым, территориальных общин в гражданских отношениях. Какая глава интересна?", reply_markup=markup)

    if message.text == "Правовые формы Участия государства, АР Крым, территориальных общин в гражданских отношениях":
        if len(GKU_g_9) > 4096:
            for x in range(0, len(GKU_g_9), 4096):
                bot.send_message(message.chat.id, GKU_g_9[x:x + 4096])
        else:
            bot.send_message(message.chat.id, GKU_g_9)

    if message.text == "Органы и представители, через которые действуют государство, АР Крым, территориальные общины в гражданских отношениях":
        if len(GKU_g_10) > 4096:
            for x in range(0, len(GKU_g_10), 4096):
                bot.send_message(message.chat.id, GKU_g_10[x:x + 4096])
        else:
            bot.send_message(message.chat.id, GKU_g_10)

    if message.text == "Ответственность по обязательствам государства, АР Крым, территориальных общин":
        if len(GKU_g_11) > 4096:
            for x in range(0, len(GKU_g_11), 4096):
                bot.send_message(message.chat.id, GKU_g_11[x:x + 4096])
        else:
            bot.send_message(message.chat.id, GKU_g_11)

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

    if message.text == "Личные неимущественные права физического лица":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        item1 = types.KeyboardButton("Общие положения про личные неимущественные права физического лица")
        item2 = types.KeyboardButton("Личные неимущественные права, которые обеспечивают естественное существование физического лица")
        item3 = types.KeyboardButton("Личные неимущественные права, которые обеспечивают социальное бытие физического лица")
        
        markup.add(item1,item2,item3)
        bot.send_message(message.chat.id, "Какая глава интересна?", reply_markup=markup)

    if message.text == "Право собственности и прочие вещные права":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        item1 = types.KeyboardButton("Право собственности")
        item2 = types.KeyboardButton("Вещное право на чужое имущество")
        
        markup.add(item1,item2)
        bot.send_message(message.chat.id, "Какой раздел интересен?", reply_markup=markup)

    if message.text == "Право собственности":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        item1 = types.KeyboardButton("Общие положения о праве собственности")
        item2 = types.KeyboardButton("Возникновение права собственности")
        item3 = types.KeyboardButton("Прекращение права собственности")
        item4 = types.KeyboardButton("Право общей собственности")
        item5 = types.KeyboardButton("Право собственности на землю (земельный участок)")
        item6 = types.KeyboardButton("Право собственности на жилье")
        item7 = types.KeyboardButton("Защита права собственности")
        
        markup.add(item1,item2,item3,item4,item5,item6,item7)
        bot.send_message(message.chat.id, "Какая глава интересна?", reply_markup=markup)

    if message.text == "Вещное право на чужое имущество":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        item1 = types.KeyboardButton("Общие положения о вещевых права на чужое имущество")
        item2 = types.KeyboardButton("Право владения чужим имуществом")
        item3 = types.KeyboardButton("Право пользования чужим имуществом")
        item4 = types.KeyboardButton("Право пользования чужим земельным участком для с/х потребностей")
        item5 = types.KeyboardButton("Право пользования чужим земельным участком для застройки")
        
        markup.add(item1,item2,item3,item4,item5)
        bot.send_message(message.chat.id, "Какая глава интересна?", reply_markup=markup)

    if message.text == "Право интеллектуальной собственности":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        item1 = types.KeyboardButton("Общие положения о праве интеллектуальной собственности")
        item2 = types.KeyboardButton("Право интеллектуальной собственности на литературное, художественное и другое произведение (авторское право)")
        item3 = types.KeyboardButton("Право интеллектуальной собственности на выполнение, фонограмму, видеограмму и программу (передач), организации речи (сопредельные права)")
        item4 = types.KeyboardButton("Право интеллектуальной собственности на научное открытие")
        item5 = types.KeyboardButton("Право интеллектуальной собственности на изобретение, полезную модель, промышленный образец")
        item6 = types.KeyboardButton("Право интеллектуальной собственности на компоновку полупроводниковых изделий")
        item7 = types.KeyboardButton("Право интеллектуальной собственности на рационализаторское предложение")
        item8 = types.KeyboardButton("Право интеллектуальной собственности на сорт растений, породу животных")
        item9 = types.KeyboardButton("Право интеллектуальной собственности на коммерческое наименование")
        item10 = types.KeyboardButton("Право интеллектуальной собственности на торговую марку")
        item11 = types.KeyboardButton("Право интеллектуальной собственности на географическое указание")
        item12 = types.KeyboardButton("Право интеллектуальной собственности на коммерческую тайну")
        
        markup.add(item1,item2,item3,item4,item5,item6,item7,item8,item9,item10,item11,item12)
        bot.send_message(message.chat.id, "Какая глава интересна?", reply_markup=markup)
        
    if message.text == "Обязательственное право":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        item1 = types.KeyboardButton("Общие положения об обязательстве")
        item2 = types.KeyboardButton("Общие положения о договоре")
        item3 = types.KeyboardButton("Отдельные виды обязательств")
        
        markup.add(item1,item2,item3)
        bot.send_message(message.chat.id, "Какой раздел интересен?", reply_markup=markup)

    if message.text == "Общие положения об обязательстве":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        item1 = types.KeyboardButton("Понятие обязательства. Стороны в обязательстве")
        item2 = types.KeyboardButton("Выполнение обязательства")
        item3 = types.KeyboardButton("Обеспечение выполнения обязательств")
        item4 = types.KeyboardButton("Прекращение обязательства")
        item5 = types.KeyboardButton("Правовые последствия нарушения обязательства. Ответственность за нарушение обязательства")
        
        markup.add(item1,item2,item3,item4,item5)
        bot.send_message(message.chat.id, "Какая глава интересна?", reply_markup=markup)

    if message.text == "Общие положения об обязательстве":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        item1 = types.KeyboardButton("Понятие и условия договора")
        item2 = types.KeyboardButton("Заключение, изменение и разрыв договора")
        
        markup.add(item1,item2)
        bot.send_message(message.chat.id, "Какая глава интересна?", reply_markup=markup)

    if message.text == "Отдельные виды обязательств":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        item1 = types.KeyboardButton("Договорные обязательства")
        item2 = types.KeyboardButton("Недоговорные обязательства")
        
        markup.add(item1,item2)
        bot.send_message(message.chat.id, "Какой Подраздел интересен?", reply_markup=markup)

    if message.text == "Договорные обязательства":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        item1 = types.KeyboardButton("Купля - продажа")
        item2 = types.KeyboardButton("Дарение")
        item3 = types.KeyboardButton("Рента")
        item4 = types.KeyboardButton("Пожизненное содержание (уход)")
        item5 = types.KeyboardButton("Найм (аренда)")
        item6 = types.KeyboardButton("Найм (аренда) жилья")
        item7 = types.KeyboardButton("Ссуда")
        item8 = types.KeyboardButton("Подряд")
        item9 = types.KeyboardButton("Выполнение научно- исследовательских или опытно-конструкторских и технологических работ")
        item10 = types.KeyboardButton("Услуги. Общие положения")
        item11 = types.KeyboardButton("Перевозка")
        item12 = types.KeyboardButton("Транспортное экспедирование")
        item13 = types.KeyboardButton("Хранение")
        item14 = types.KeyboardButton("Страхование")
        item15 = types.KeyboardButton("Поручение")
        item16 = types.KeyboardButton("Комиссия")
        item17 = types.KeyboardButton("Управление имуществом")
        item18 = types.KeyboardButton("Займ. Кредит. Банковский вклад")
        item19 = types.KeyboardButton("Банковский счет")
        item20 = types.KeyboardButton("Факторинг")
        item21 = types.KeyboardButton("Расчеты")
        item22 = types.KeyboardButton("Распоряжение имущественными правами интеллектуальной собственности")
        item23 = types.KeyboardButton("Коммерческая концессия")
        item24 = types.KeyboardButton("Совместная деятельность")

        markup.add(item1,item2,item3,item4,item5,item6,item7,item8,item9,item10,item11,item12,item13,item14,item15,item16,item17,item18,item19,item20,item21,item22,item23,item24)
        bot.send_message(message.chat.id, "Какая глава интересна?", reply_markup=markup)

    if message.text == "Недоговорные обязательства":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        item1 = types.KeyboardButton("Публичное обещание вознаграждения")
        item2 = types.KeyboardButton("Совершение действий в имущественных интересах другого лица без его поручения")
        item3 = types.KeyboardButton("Спасение здоровья и жизни физического лица, имущества физического или юридического лица")
        item4 = types.KeyboardButton("Создание угрозы жизни, здоровью, имуществу физического лица или имуществу юридического лица")
        item5 = types.KeyboardButton("Возмещение ущерба")
        item6 = types.KeyboardButton("Обретение, сохранение имущества без достаточного правового основания")
        
        markup.add(item1,item2,item3,item4,item5,item6)
        bot.send_message(message.chat.id, "Какая глава интересна?", reply_markup=markup)

    if message.text == "Наследственное право":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        item1 = types.KeyboardButton("Общие положения о наследовании")
        item2 = types.KeyboardButton("Наследование по завещанию")
        item3 = types.KeyboardButton("Наследование по закону")
        item4 = types.KeyboardButton("Осуществление права на наследование")
        item5 = types.KeyboardButton("Выполнение завещания")
        item6 = types.KeyboardButton("Оформление права на наследство")
        item7 = types.KeyboardButton("Наследственный договор")
        
        markup.add(item1,item2,item3,item4,item5,item6,item7)
        bot.send_message(message.chat.id, "Какая глава интересна?", reply_markup=markup)

    #ГПК(Гражданский процессуальный кодекс)
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

    if message.text == "Общие положения":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        item1 = types.KeyboardButton("Основные положения")
        item2 = types.KeyboardButton("Гражданская юрисдикция")
        item3 = types.KeyboardButton("Состав суда – отводы")
        item4 = types.KeyboardButton("Участники гражданского процесса")
        item5 = types.KeyboardButton("Доказательства")
        item6 = types.KeyboardButton("Процессуальные сроки")
        item7 = types.KeyboardButton("Судебные вызовы и уведомления")
        item8 = types.KeyboardButton("Судебные затраты")
        item9 = types.KeyboardButton("Средства процессуального принуждения")
        
        markup.add(item1,item2,item3,item4,item5,item6,item7,item8,item9)
        bot.send_message(message.chat.id, "Какой раздел интересен?", reply_markup=markup)

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

    #else:
    #    bot.send_message(message.chat.id, "Сделайте свой выбор!")

bot.polling()
