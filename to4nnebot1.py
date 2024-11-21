import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

TOKEN = 'ybt'
bot = telebot.TeleBot(TOKEN)


def create_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton('Байков Александр Александрович'), KeyboardButton('Карпинский Александр Петрович'))
    keyboard.add(KeyboardButton('Вавилов Николай Иванович'), KeyboardButton('Вавилов Сергей Иванович'), KeyboardButton('Константинов Борис Павлович'))
    keyboard.add(KeyboardButton('Обручев Владимир Афанасьевич'), KeyboardButton("Обручев Сергей Владимирович"), KeyboardButton('Глушко Валентин Петрович'))
    keyboard.add(KeyboardButton('Веденеев Борис Евгеньевич'), KeyboardButton('Бутлеров Александр Михайлович'), KeyboardButton('Ковалевская Софья Васильевна'))
    return keyboard


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(
        message.chat.id,
        "Выберите учёного:",
        reply_markup=create_keyboard()
    )


def send_response_with_photo(chat_id, text, photo_path):
    with open(photo_path, 'rb') as photo:
        bot.send_photo(chat_id, photo, caption=text, parse_mode="HTML")


@bot.message_handler(func=lambda message: message.text == "Байков Александр Александрович")
def handle_button_1(message):
    latitude = 60.026496
    longitude = 30.379532
    send_response_with_photo(message.chat.id,
                              "Улица Академика Байкова названа в честь Байкова Александра Александровича (25 июля 1870 - 6 апреля 1946) - советский химик, материаловед, металлург."
                              "\n\n«Я — старый металлург, и я привык годами думать, что нет ничего на свете крепче стали. И вот сегодня я убедился в своей ошибке… Да, я ошибся. Есть, оказывается, материал, который ещё крепче стали. Этот благородный материал — советские люди»."
                              "\n\nДля более подробной информации посетите <a href='https://ru.wikipedia.org/wiki/%D0%91%D0%B0%D0%B9%D0%BA%D0%BE%D0%B2,_%D0%90%D0%BB%D0%B5%D0%BA%D1%81%D0%B0%D0%BD%D0%B4%D1%80_%D0%90%D0%BB%D0%B5%D0%BA%D1%81%D0%B0%D0%BD%D0%B4%D1%80%D0%BE%D0%B2%D0%B8%D1%87'>Википедию</a>.",
                              "u4eniefotki/photo1.jpg")
    bot.send_location(message.chat.id, latitude, longitude)


@bot.message_handler(func=lambda message: message.text == "Карпинский Александр Петрович")
def handle_button_2(message):
    latitude = 60.007654
    longitude = 30.424070
    send_response_with_photo(message.chat.id,
                              "Карпинский Александр Петрович (25 ноября 1799 - 7 мая 1855) - российский учёный, инженер, педагог, один из основателей отечественной гидротехники."
                              "\n\n«Вода — это не просто жидкость, это основа всей жизни на Земле». "
                              "\n\nДля более подробной информации посетите <a href='https://ru.wikipedia.org/wiki/%D0%9A%D0%B0%D1%80%D0%BF%D0%B8%D0%BD%D1%81%D0%BA%D0%B8%D0%B9,_%D0%90%D0%BB%D0%B5%D0%BA%D1%81%D0%B0%D0%BD%D0%B4%D1%80_%D0%9F%D0%B5%D1%82%D1%80%D0%BE%D0%B2%D0%B8%D1%87'>Википедию</a>.",
                              "u4eniefotki/photo2.jpg")
    bot.send_location(message.chat.id, latitude, longitude)


@bot.message_handler(func=lambda message: message.text == "Вавилов Николай Иванович")
def handle_button_3(message):
    latitude = 60.020494
    longitude = 30.390303
    send_response_with_photo(message.chat.id,
                              "Улица Вавиловых названа в честь братьев Вавиловых. Вавилова Николая Ивановича (13 ноября 1887 - 26 января 1943) - русский и советский учёный - генетик, ботаник, селекционер, химик, географ, общественный и государственный деятель."
                              "\n\n«Мне очень по душе нарушение основного закона Ньютона - закона инерции покоя, превращения его в инерцию движения»."
                              "\n\nДля более подробной информации посетите <a href='https://ru.wikipedia.org/wiki/%D0%92%D0%B0%D0%B2%D0%B8%D0%BB%D0%BE%D0%B2,_%D0%9D%D0%B8%D0%BA%D0%BE%D0%BB%D0%B0%D0%B9_%D0%98%D0%B2%D0%B0%D0%BD%D0%BE%D0%B2%D0%B8%D1%87'>Википедию</a>.",
                              "u4eniefotki/photo3.jpg")
    bot.send_location(message.chat.id, latitude, longitude)


@bot.message_handler(func=lambda message: message.text == "Вавилов Сергей Иванович")
def handle_button_4(message):
    latitude = 60.020494
    longitude = 30.390303
    send_response_with_photo(message.chat.id,
                              "Улица Вавиловых названа в честь братьев Вавиловых. Вавилова Сергея Ивановича (12 марта 1891 - 25 января 1951) - советский физик, основатель научной школы физической оптики в СССР."
                              "\n\n«С точки зрения службы науки народу никогда не следует забывать, что её цель — возможно большая помощь государству и обществу»."
                              "\n\nДля более подробной информации посетите <a href='https://ru.wikipedia.org/wiki/%D0%92%D0%B0%D0%B2%D0%B8%D0%BB%D0%BE%D0%B2,_%D0%A1%D0%B5%D1%80%D0%B3%D0%B5%D0%B9_%D0%98%D0%B2%D0%B0%D0%BD%D0%BE%D0%B2%D0%B8%D1%87'>Википедию</a>.",
                              "u4eniefotki/photo4.jpg")
    bot.send_location(message.chat.id, latitude, longitude)


@bot.message_handler(func=lambda message: message.text == "Константинов Борис Павлович")
def handle_button_5(message):
    latitude = 60.021011
    longitude = 30.381589
    send_response_with_photo(message.chat.id,
                              "Улица Академика Константинова названа в честь Константинова Бориса Павловича (23 июня 1910 - 9 июля 1969) - советский учёный-физик, академик, вице-президент Академии наук СССР."
                              "\n\n«Только физики и математики могут сдвинуть нашу застывшую экономику с мёртвой точки и сделать её научно обоснованной»."
                              "\n\nДля более подробной информации посетите <a href='https://ru.wikipedia.org/wiki/%D0%9A%D0%BE%D0%BD%D1%81%D1%82%D0%B0%D0%BD%D1%82%D0%B8%D0%BD%D0%BE%D0%B2,_%D0%91%D0%BE%D1%80%D0%B8%D1%81_%D0%9F%D0%B0%D0%B2%D0%BB%D0%BE%D0%B2%D0%B8%D1%87'>Википедию</a>.",
                              "u4eniefotki/photo5.jpg")
    bot.send_location(message.chat.id, latitude, longitude)


@bot.message_handler(func=lambda message: message.text == "Обручев Владимир Афанасьевич")
def handle_button_6(message):
    latitude = 60.012665
    longitude = 30.378759
    send_response_with_photo(message.chat.id,
                              "Улица Обручевых названа в честь отца и сына Обручевых.  Отец Владимир Афанасьевич Обручев (28 сентября 1863 - 19 июня 1956) - русский и советский учёный, организатор науки, и популяризатор науки, широко известен как геолог, историк геологии и горного дела, географ и путешественник."
                              "\n\n«Любите трудиться. Самое большое наслаждение и удовлетворение приносит человеку труд»."
                              "\n\nДля более подробной информации посетите <a href='https://ru.wikipedia.org/wiki/%D0%9E%D0%B1%D1%80%D1%83%D1%87%D0%B5%D0%B2,_%D0%92%D0%BB%D0%B0%D0%B4%D0%B8%D0%BC%D0%B8%D1%80_%D0%90%D1%84%D0%B0%D0%BD%D0%B0%D1%81%D1%8C%D0%B5%D0%B2%D0%B8%D1%87'>Википедию</a>.",
                              "u4eniefotki/photo6.jpg")
    bot.send_location(message.chat.id, latitude, longitude)


@bot.message_handler(func=lambda message: message.text == "Обручев Сергей Владимирович")
def handle_button_7(message):
    latitude = 60.012665
    longitude = 30.378759
    send_response_with_photo(message.chat.id,
                              "Улица Обручевых названа в честь отца и сына Обручевых. Сын Обручев Сергей Владимирович Обручев (22 января 1891 - 29 августа 1965) - советский геолог, член-корреспондент АН СССР."
                              "\n\n«А у нас пурга метет за окном и брезент гремит на крыше. Но мы чувствуем, что мы не оторваны, что мы живём со всей Советской страной»."
                              "\n\nДля более подробной информации посетите <a href='https://ru.wikipedia.org/wiki/%D0%9E%D0%B1%D1%80%D1%83%D1%87%D0%B5%D0%B2,_%D0%A1%D0%B5%D1%80%D0%B3%D0%B5%D0%B9_%D0%92%D0%BB%D0%B0%D0%B4%D0%B8%D0%BC%D0%B8%D1%80%D0%BE%D0%B2%D0%B8%D1%87'>Википедию</a>.",
                              "u4eniefotki/photo7.jpg")
    bot.send_location(message.chat.id, latitude, longitude)


@bot.message_handler(func=lambda message: message.text == "Глушко Валентин Петрович")
def handle_button_8(message):
    latitude = 60.023412
    longitude = 30.373576
    send_response_with_photo(message.chat.id,
                              "Аллея Академика Глушко названа в честь Глушко Валентина Петровича (20 августа 1908 - 10 января 1989) - советский инженер и учёный в области ракетно-космической техники."
                              "\n\n«С хорошим двигателем и ворота полетят»."
                              "\n\nДля более подробной информации посетите <a href='https://ru.wikipedia.org/wiki/%D0%93%D0%BB%D1%83%D1%88%D0%BA%D0%BE,_%D0%92%D0%B0%D0%BB%D0%B5%D0%BD%D1%82%D0%B8%D0%BD_%D0%9F%D0%B5%D1%82%D1%80%D0%BE%D0%B2%D0%B8%D1%87'>Википедию</a>.",
                              "u4eniefotki/photo8.jpg")
    bot.send_location(message.chat.id, latitude, longitude)


@bot.message_handler(func=lambda message: message.text == "Веденеев Борис Евгеньевич")
def handle_button_9(message):
    latitude = 60.022103
    longitude = 30.371510
    send_response_with_photo(message.chat.id,
                              "Улица Веденеева названа в честь Бориса Евгеньевича Веденеева (21 декабря 1884 - 25 сентября 1946) - русский и советский учёный, энергетик и гидротехник."
                              "\n\nНа улице Гидротехников расположен институт его имени."
                              "\n\nДля более подробной информации посетите <a href='https://ru.wikipedia.org/wiki/%D0%92%D0%B5%D0%B4%D0%B5%D0%BD%D0%B5%D0%B5%D0%B2,_%D0%91%D0%BE%D1%80%D0%B8%D1%81_%D0%95%D0%B2%D0%B3%D0%B5%D0%BD%D1%8C%D0%B5%D0%B2%D0%B8%D1%87'>Википедию</a>.",
                              "u4eniefotki/photo9.jpg")
    bot.send_location(message.chat.id, latitude, longitude)


@bot.message_handler(func=lambda message: message.text == "Бутлеров Александр Михайлович")
def handle_button_10(message):
    latitude = 60.002436
    longitude = 30.397246
    send_response_with_photo(message.chat.id,
                                "Улица Бутлерова названа в честь Бутлерова Александра Михайловича (3 сентября 1828 - 17 сентября 1886) - русский химик, основоположник теории химической структуры."
                              "\n\n«Для химика нет ничего более важного, чем понимание структуры вещества»."
                              "\n\nДля более подробной информации посетите <a href='https://ru.wikipedia.org/wiki/%D0%91%D1%83%D1%82%D0%BB%D0%B5%D1%80%D0%BE%D0%B2,_%D0%90%D0%BB%D0%B5%D0%BA%D1%81%D0%B0%D0%BD%D0%B4%D1%80_%D0%9C%D0%B8%D1%85%D0%B0%D0%B9%D0%BB%D0%BE%D0%B2%D0%B8%D1%87'>Википедию</a>.",
                              "u4eniefotki/photo10.jpg")
    bot.send_location(message.chat.id, latitude, longitude)


@bot.message_handler(func=lambda message: message.text == "Ковалевская Софья Васильевна")
def handle_button_11(message):
    latitude = 60.014783
    longitude = 30.412922
    send_response_with_photo(message.chat.id,
                              "Улица Ковалевской названа в честь Софьи Васильевны Ковалевской (15 января 1850 - 10 февраля 1891) - российская математик, первая женщина, получившая степень доктора наук в Европе."
                              "\n\n«Математика — это не просто наука, это искусство»."
                              "\n\nДля более подробной информации посетите <a href='https://ru.wikipedia.org/wiki/%D0%9A%D0%BE%D0%B2%D0%B0%D0%BB%D0%B5%D0%B2%D1%81%D0%BA%D0%B0%D1%8F,_%D0%A1%D0%BE%D1%84%D1%8C%D1%8F_%D0%92%D0%B0%D1%81%D0%B8%D0%BB%D1%8C%D0%B5%D0%B2%D0%BD%D0%B0'>Википедию</a>.",
                              "u4eniefotki/photo11.jpg")
    bot.send_location(message.chat.id, latitude, longitude)


bot.polling(none_stop=True)
