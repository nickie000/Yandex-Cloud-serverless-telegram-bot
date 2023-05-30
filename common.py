from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Кнопки для старта
common_QA_butt = InlineKeyboardButton('Q&A', callback_data='common_QA')
common_Questionnaire_butt = InlineKeyboardButton('Анкетирование', callback_data='common_Questionnare')
# Клавиатура для старта
common_start_butt = InlineKeyboardMarkup(row_width=2).add(common_QA_butt, common_Questionnaire_butt)

# Кнопки для всех функций
common_butts_for_ALL_ESCAPE = InlineKeyboardButton('Вернуться в начало', callback_data='list_of_methods')

# Кнопки для анкетирования
common_butts_for_Questionnaire_FIO = InlineKeyboardButton(text='ФИО:', callback_data='common_Questionnaire_FIO')
common_butts_for_Questionnaire_AGE = InlineKeyboardButton('Возраст:', callback_data='common_Questionnaire_AGE')
common_butts_for_Questionnaire_CITY = InlineKeyboardButton('Город:', callback_data='common_Questionnaire_CITY')

common_butts_for_Questionnaire_TG = InlineKeyboardButton('Телеграм:', callback_data='common_Questionnaire_TG')
common_butts_for_Questionnaire_PHONE = InlineKeyboardButton('Телефон:', callback_data='common_Questionnaire_PHONE')
common_butts_for_Questionnaire_DELETE = InlineKeyboardButton('Очистить:', callback_data='common_Questionnaire_DELETE')
# Клавиатура для анкетирования
common_butts_for_Questionnaire = InlineKeyboardMarkup(row_width=2).add(common_butts_for_Questionnaire_FIO, common_butts_for_Questionnaire_TG, 
                                                                       common_butts_for_Questionnaire_AGE, common_butts_for_Questionnaire_PHONE, 
                                                                       common_butts_for_Questionnaire_CITY, common_butts_for_Questionnaire_DELETE)
common_butts_for_Questionnaire.row(common_butts_for_ALL_ESCAPE)

html = types.ParseMode.HTML

""" 
          анкета
    ФИО     | Телеграм
    Возраст | Телефон
    Город   | Очистить
    
"""

async def start(message: types.Message):
    await message.answer_sticker(sticker=r'CAACAgIAAxkBAAEJB_xkZySN5Yw4AAHohKX87rJ8YPGyBA0AAm8AA9vbfgABmVtQqHuTgHQvBA')
    await message.answer(f'Привет, <b>{message.from_user.full_name}</b>! Меня зовут Бот Тестировщик\nЯ создан для того, чтобы показать на что способен мой Босс, а также для тестирования твоего бота\n<i>(для этого мой <a href="tg://user?id=582180705">Босс</a> должен был сообщить <tg-spoiler>секретную команду</tg-spoiler></i>)', parse_mode=html, reply_markup=common_start_butt)


async def id_handler(message: types.Message):
    await message.answer(f'Ваш ID: <code>{message.from_user.id}</code>', parse_mode=html)


async def common_Questionnaire(callback: types.CallbackQuery):
    await callback.message.edit_text('Начинаем заполнение анкеты 📋\nНажимай на кнопки снизу, чтобы их заполнить инофрмацией =)\n<pre>Кнопки ниже пока не работают</pre>', reply_markup=common_butts_for_Questionnaire, parse_mode=html)


async def list_of_methods(callback: types.CallbackQuery):
    await callback.message.edit_text('Мы вернулись к списку функций', reply_markup=common_start_butt)

async def register_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(list_of_methods, lambda c: c.data == 'list_of_methods')
    dp.register_message_handler(start, commands='start')
    dp.register_message_handler(id_handler, commands='id')
    dp.register_callback_query_handler(common_Questionnaire, lambda c: c.data == 'common_Questionnare')
