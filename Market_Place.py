import telebot
from telebot import types

bot = telebot.TeleBot('2135352061:AAEdBOhbUu7DRmcUxQAzn-Ns0VvLRxTK7M4')

# меню для выбора
markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("Покупатель")
item2 = types.KeyboardButton("Поставщик")
item3 = types.KeyboardButton("Перевозчик")
item4 = types.KeyboardButton("Менеджер склада")
markup.add(item1, item2, item3, item4)

markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("Назад к выбору")
markup1.add(item1)

markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("Изменить цены")
item2 = types.KeyboardButton("Продукция на складе")
item3 = types.KeyboardButton("Текущие заказы")
markup2.add(item1, item2, item3)

markup3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("Работник компании")
item2 = types.KeyboardButton("Частное лицо")
markup3.add(item1, item2)

markup5 = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("Активные заказы")
item2 = types.KeyboardButton("Доступные заказы")
markup5.add(item1, item2)
# запомнинание ролей
is_customer = is_seller = is_operator = is_driver = is_auth = is_first_time = is_private = is_company = 0

@bot.message_handler(commands=['start'])
def welcome(message):
    # keyboard

    bot.send_message(message.chat.id,
                     "Добро пожаловать, {0.first_name}!\nКто вы?".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        global is_customer, is_seller, is_operator, is_driver, is_auth, is_first_time, is_private, is_company

        if message.text == 'Покупатель':
            is_customer = 1
            is_seller = is_operator = is_driver = 0
            bot.send_message(message.chat.id, "Что желаете?", reply_markup=markup1)
        elif message.text == 'Перевозчик':
            is_driver = 1
            is_seller = is_operator = is_customer = 0
            bot.send_message(message.chat.id, "Введите номер для авторизации", reply_markup=markup1)
        elif message.text == 'Поставщик':
            is_seller = 1
            is_customer = is_operator = is_driver = 0
            bot.send_message(message.chat.id, "Введите номер для авторизации", reply_markup=markup1)
        elif message.text == 'Менеджер склада':
            is_operator = 1
            is_seller = is_customer = is_driver = 0
            bot.send_message(message.chat.id, "Введите номер для авторизации", reply_markup=markup1)

        if message.text == '88005553535':
            bot.send_message(message.chat.id, "Введите код, отправленный на ваш номер")
        if message.text == '123':
            is_auth = 1
            is_first_time = 1

        if is_customer:
            if message.text == 'молоко':
                bot.send_message(message.chat.id, "В каком объеме?")
        if is_auth:
            if is_operator:
                if is_first_time:
                    bot.send_message(message.chat.id, "Выберите действие", reply_markup=markup2)
                    is_first_time = 0
                else:
                    if message.text == 'молоко - 100':
                        bot.send_message(message.chat.id, "Цена изменена")
                    if message.text == 'Продукция на складе':
                        bot.send_message(message.chat.id, "Картофель - 2 тонны\nКапуста - 0.5 тонны")
                    elif message.text == "Изменить цены":
                        bot.send_message(message.chat.id, "Что хотите изменить?")
                    elif message.text == 'Текущие заказы':
                        bot.send_message(message.chat.id, "ул. Ленина, д.1 - 10кг картофель\nул. Ленина, д.15 - 2 кг капуста")
            elif is_driver:
                if is_first_time:
                    bot.send_message(message.chat.id, "Вы частное лицо или работник компании?", reply_markup=markup3)
                    is_first_time = 0
                if message.text == 'Частное лицо':
                    bot.send_message(message.chat.id, "Выберите действие",
                                     reply_markup=markup5)
                    is_private = 1
                    is_company = 0
                if is_private:
                    if message.text == 'Активные заказы':
                        bot.send_message(message.chat.id, '''Адрес приема: г. Волжск, ул. Ленина, стр. 1 к А
Адрес доставки: г. Йошкар-Ола, ул. Гоголя, стр 3б к 5
Товар: Картофель красный
Вес: 1000 кг
Ожидаемое время доставки: 13 ноября, 14:00
Ответственный за погрузку: Васильев П.П. 898887865433
Получатель: Иванов А.А., 89888888888
\nОплата: 5000 рублей''',
                                         reply_markup=markup5)
                    if message.text == 'Доступные заказы':

                        markup4 = types.InlineKeyboardMarkup(row_width=2)
                        item1 = types.InlineKeyboardButton("Принять", callback_data='good')
                        item2 = types.InlineKeyboardButton("Отказаться", callback_data='bad')

                        markup4.add(item1, item2)
                        bot.send_message(message.chat.id, '''Адрес приема: г. Звенигово, мкр. Парковый, д.5
Адрес доставки: г. Йошкар-Ола, ул. Пушкина, стр 3б к 5
Товар: Капуста
Вес: 1500 кг
Ожидаемое время доставки: 14 ноября, 17:00
Ответственный за погрузку: Антонов В.М. 89264356790
Получатель: Иванов А.А., 89888888888
\nОплата: 2000 рублей''',
                                         reply_markup=markup4)

                if message.text == "Работник компании":
                    bot.send_message(message.chat.id, "Выберите действие",
                                     reply_markup=markup5)
                    is_company = 1
                    is_private = 0
                if is_company:
                    if message.text == 'Активные заказы':
                        bot.send_message(message.chat.id, "Сейчас заказов нет...\n\nВам поступит уведомление при новых заказах",
                                         reply_markup=markup5)
                    if message.text == 'Доступные заказы':

                        bot.send_message(message.chat.id, "Сейчас заказов нет...\n\nВам поступит уведомление при новых заказах",
                                         reply_markup=markup5)

            elif is_seller:
                bot.send_message(message.chat.id, '''Активные заказы:
❗Товар: Картофель красный
Вес: 10 тонн
Время погрузки: 11 ноября, 12:00
\nСтоимость товара: 500000 рублей❗''',
                                 reply_markup=types.ReplyKeyboardRemove())
        if message.text == 'Назад к выбору':
            bot.send_message(message.chat.id, "Кто вы?",
                             reply_markup=markup)
            is_auth = 0


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'good':
                bot.send_message(call.message.chat.id, 'Заказ за вами закреплен')
            elif call.data == 'bad':
                bot.send_message(call.message.chat.id, 'Вам поступит уведомление при новых заказах')
    except Exception as e:
        print(repr(e))
bot.polling(none_stop=True)