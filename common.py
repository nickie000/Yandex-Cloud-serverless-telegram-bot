from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


# Кнопки для старта
common_QA_butt = InlineKeyboardButton('Q&A', callback_data='common_QA') # type: ignore
common_Questionnaire_butt = InlineKeyboardButton('Анкетирование', callback_data='common_Questionnare') # type: ignore
# Клавиатура для старта
common_start_butt = InlineKeyboardMarkup(row_width=2).add(common_QA_butt, common_Questionnaire_butt)

# Кнопки для всех функций
common_butts_for_ALL_ESCAPE = InlineKeyboardButton('Вернуться в начало', callback_data='list_of_methods') # type: ignore

# Кнопки для анкетирования
common_butts_for_Questionnaire_FIO = InlineKeyboardButton(text='ФИО:', callback_data='common_Questionnaire_FIO') # type: ignore
common_butts_for_Questionnaire_AGE = InlineKeyboardButton('Возраст:', callback_data='common_Questionnaire_AGE') # type: ignore
common_butts_for_Questionnaire_CITY = InlineKeyboardButton('Город:', callback_data='common_Questionnaire_CITY') # type: ignore

common_butts_for_Questionnaire_TG = InlineKeyboardButton('Телеграм:', callback_data='common_Questionnaire_TG') # type: ignore
common_butts_for_Questionnaire_PHONE = InlineKeyboardButton('Телефон:', callback_data='common_Questionnaire_PHONE') # type: ignore
common_butts_for_Questionnaire_DELETE = InlineKeyboardButton('Очистить:', callback_data='common_Questionnaire_DELETE') # type: ignore

# Клавиатура для анкетирования
common_butts_for_Questionnaire = InlineKeyboardMarkup(row_height=2).add(common_butts_for_Questionnaire_FIO, common_butts_for_Questionnaire_TG, 
                                                                       common_butts_for_Questionnaire_AGE, common_butts_for_Questionnaire_PHONE, 
                                                                       common_butts_for_Questionnaire_CITY, common_butts_for_Questionnaire_DELETE)
common_butts_for_Questionnaire.row(common_butts_for_ALL_ESCAPE)

# Кнопки для Q&A
common_butts_for_QA_Q1 = InlineKeyboardButton('Зачем нужен телеграм-бот?', callback_data='common_QA_Q1') # type: ignore
common_butts_for_QA_Q2 = InlineKeyboardButton('Как боты работают 24/7?', callback_data='common_QA_Q2') # type: ignore

common_butts_for_QA_Q3 = InlineKeyboardButton('Почему здесь так мало примеров?', callback_data='common_QA_Q3') # type: ignore
common_butts_for_QA_Q4 = InlineKeyboardButton('Сколько стоит хостинг?', callback_data='common_QA_Q4') # type: ignore

common_butts_for_QA_ESCAPE = InlineKeyboardButton('Вернуться к вопросам', callback_data='common_QA_ESC') # type: ignore
common_butts_for_QA_NONE = InlineKeyboardButton('Я не нашел вопрос', callback_data='common_QA_NONE') # type: ignore
common_butts_for_QA_BOSS = InlineKeyboardButton('К Боссу', url='t.me/uhtoer') # type: ignore

# Клавиатура для Q&A
common_butts_for_QA_start = InlineKeyboardMarkup(row_width=1).add(
    common_butts_for_QA_Q1, 
    common_butts_for_QA_Q2, 
    common_butts_for_QA_Q3,
    common_butts_for_QA_Q4
)
common_butts_for_QA_start.row(common_butts_for_QA_NONE, common_butts_for_ALL_ESCAPE)
common_butts_for_QA_1 = InlineKeyboardMarkup(row_width=1).add(common_butts_for_QA_ESCAPE)
common_butts_for_QA_BOSS_1 = InlineKeyboardMarkup(row_width=2).add(common_butts_for_QA_BOSS, common_butts_for_QA_ESCAPE)

html = types.ParseMode.HTML
""" 
          анкета
    ФИО     | Телеграм
    Возраст | Телефон
    Город   | Очистить
    
"""
"""-----------------Основные команды------------------"""
async def common_start(message: types.Message):
    await message.answer_sticker(sticker=r'CAACAgIAAxkBAAEJB_xkZySN5Yw4AAHohKX87rJ8YPGyBA0AAm8AA9vbfgABmVtQqHuTgHQvBA')
    await message.answer(f'Привет, <b>{message.from_user.full_name}</b>! Меня зовут Бот Тестировщик\nЯ создан для того, чтобы показать на что способен мой Босс, а также для тестирования твоего бота\n<i>(для этого мой <a href="tg://user?id=582180705">Босс</a> должен был сообщить <tg-spoiler>секретную команду</tg-spoiler></i>)', parse_mode=html, reply_markup=common_start_butt)


async def common_id_handler(message: types.Message):
    await message.answer(f'Ваш ID: <code>{message.from_user.id}</code>', parse_mode=html)


async def common_list_of_methods(callback: types.CallbackQuery):
    await callback.message.edit_text(f'📖 Мы вернулись к списку функций', reply_markup=common_start_butt)


"""---------------Команды Анкетирования---------------"""
# Начало Анкетирования
async def common_Questionnaire(callback: types.CallbackQuery):
    await callback.message.edit_text(f'Начинаем заполнение анкеты 📋\nНажимай на кнопки снизу, чтобы их заполнить инофрмацией =)\n<pre>Кнопки ниже пока не работают</pre>', reply_markup=common_butts_for_Questionnaire, parse_mode=html)


"""--------------------Команды Q&A--------------------"""
# Начало Q&A
async def common_QA(callback: types.CallbackQuery):
    await callback.message.edit_text(f'⁉️ Здесь собраны все вопросы, выбирайте какой Вас больше интересует и я сразу отвечу на него', reply_markup=common_butts_for_QA_start)


# Ответ на Вопрос 1 Q&A
async def common_QA_Q1(callback: types.CallbackQuery):
    await callback.message.edit_text(
        f'👾 Телеграм-боты нужны в основном для простых задач (именно Телеграм-боты):\n' +
        f'1️⃣ Заполнение анкет;\n2️⃣ Вопрос-Ответ;\n3️⃣ Для Web-приложений, сайтов;\n' +
        f'4️⃣ Для модерирования групп (удаление спама и фильтрация сообщений, приглашение в закрытые группы), и т.д.',reply_markup=common_butts_for_QA_1)


# Ответ на Вопрос 2 Q&A
async def common_QA_Q2(callback: types.CallbackQuery):
    await callback.message.edit_text(
        f'Есть 2 варианта:\n' +
        f'1️⃣ Запустить файлы с ботом на своем сервер (ПК);\n' +
        f'2️⃣ Запустить бота на облачном сервере (Яндекс, Гугл, Селектел вроде одни из ходовых).\n' +
        f'Со вторым вариантом нет никаких сложностей, в стоимсть услуг моего <i>Босса</i> входит хостинг на облако, ' +
        f'но если Вы не хотите тратить деньги, на счет стоимости за облако есть отдельная кнопка, то придется столкнуться с возможными ' +
        f'случайными отключениями электричества, что приведет к отключению Вашего бота', reply_markup=common_butts_for_QA_1, parse_mode=html
    )


# Ответ на Вопрос 3 Q&A
async def common_QA_Q3(callback: types.CallbackQuery):
    await callback.message.edit_text(
        f'😬 Функций и в правду мало, но очень сложно брать идеи из ни откуда =)\n' +
        f'Все функции которые здесь представлены, это боты моих заказчиков, только переделанные под тематику Помощника\n' +
        f'Если у Вас есть какие-то предложения, либо Вы нашли баг, пожалуйста, немедленно сообщите об этом <a href="t.me/uhtoer">Боссу</a>', reply_markup=common_butts_for_QA_1, parse_mode=html
    )


# Ответ на Вопрос 4 Q&A
async def common_QA_Q4(callback: types.CallbackQuery):
    await callback.message.edit_text(
        f'☁️ Я могу сказать только про Яндекс.Облако\n' +
        f'Если Ваш бот не будет получать очень много сообщений от пользователей, то практически бесплатно, ' +
        f'достаточно перевести на платежный счет минимальную сумму. Но, если к Вашему боту будут обращаться регулярно ' +
        f'то мой Босс с Вами расчитает месечную стоимость хотсинга', reply_markup=common_butts_for_QA_1
    )


# Возвращение к Вопросам Q&A
async def common_QA_ESC(callback: types.CallbackQuery):
    await callback.message.edit_text(f'⁉️ Здесь собраны все вопросы, выбирайте какой Вас больше интересует и я сразу отвечу на него', reply_markup=common_butts_for_QA_start)


# Кнопка Не нашел вопрос
async def common_QA_NONE(callback: types.CallbackQuery):
    await callback.message.edit_text(f'😉 Мой Босс сможет ответить на любой Ваш вопрос, осталось только нажать заветную кнопочку', reply_markup=common_butts_for_QA_BOSS_1)


async def register_handlers(dp: Dispatcher):
    # Основные хендлеры
    dp.register_message_handler(common_start, commands='start')
    dp.register_message_handler(common_id_handler, commands='id')
    dp.register_callback_query_handler(common_list_of_methods, lambda c: c.data == 'list_of_methods')
    # Хендлеры Анкетирования
    dp.register_callback_query_handler(common_Questionnaire, lambda c: c.data == 'common_Questionnare')
    # Хендлеры Q&A
    dp.register_callback_query_handler(common_QA, lambda c: c.data == 'common_QA')
    dp.register_callback_query_handler(common_QA_Q1, lambda c: c.data == 'common_QA_Q1')
    dp.register_callback_query_handler(common_QA_Q2, lambda c: c.data == 'common_QA_Q2')
    dp.register_callback_query_handler(common_QA_Q3, lambda c: c.data == 'common_QA_Q3')
    dp.register_callback_query_handler(common_QA_Q4, lambda c: c.data == 'common_QA_Q4')

    dp.register_callback_query_handler(common_QA_ESC, lambda c: c.data == 'common_QA_ESC')
    dp.register_callback_query_handler(common_QA_NONE, lambda c: c.data == 'common_QA_NONE')
    