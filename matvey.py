from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Кнопочки
butt_quest1 = InlineKeyboardButton('Вопрос 1?', callback_data='q1')
butt_quest2 = InlineKeyboardButton('Вопрос 2?', callback_data='q2')
butt_quest3 = InlineKeyboardButton('Вопрос 3?', callback_data='q3')
butt_quest4 = InlineKeyboardButton('Вопрос 4?', callback_data='q4')
butt_quest5 = InlineKeyboardButton('Вопрос 5?', callback_data='q5')

butt_quest6 = InlineKeyboardButton('Вопрос 6?', callback_data='q6')
butt_quest7 = InlineKeyboardButton('Вопрос 7?', callback_data='q7')
butt_quest8 = InlineKeyboardButton('Вопрос 8?', callback_data='q8')
butt_quest9 = InlineKeyboardButton('Вопрос 9?', callback_data='q9')
butt_quest10 = InlineKeyboardButton('Вопрос 10?', callback_data='q10')

butt_quest11 = InlineKeyboardButton('Вопрос 11?', callback_data='q11')
butt_quest12 = InlineKeyboardButton('Вопрос 12?', callback_data='q12')
butt_quest13 = InlineKeyboardButton('Вопрос 13?', callback_data='q13')
butt_quest14 = InlineKeyboardButton('Вопрос 14?', callback_data='q14')
butt_quest15 = InlineKeyboardButton('Вопрос 15?', callback_data='q15')

butt_quest1_NEXT = InlineKeyboardButton('⏩', callback_data='qnext1')
butt_quest1_BACK = InlineKeyboardButton('⏪', callback_data='qback1')
butt_quest2_NEXT = InlineKeyboardButton('⏩', callback_data='qnext2')
butt_quest2_BACK = InlineKeyboardButton('⏪', callback_data='qback2')
butt_questNONE = InlineKeyboardButton('Не нашел вопрос', callback_data='qnone')
butt_esc = InlineKeyboardButton('Вернуться к вопросам', callback_data='esc')
butt_boss = InlineKeyboardButton(text="К боссу", url='t.me/uhtoer')

# Клявищи
kb_1_page = InlineKeyboardMarkup(row_width=1).add(butt_quest1, butt_quest2, butt_quest3, butt_quest4, butt_quest5, butt_quest1_NEXT)

kb_2_page = InlineKeyboardMarkup(row_width=1).add(butt_quest6, butt_quest7, butt_quest8, butt_quest9, butt_quest10)
kb_2_page.row(butt_quest1_BACK, butt_quest2_NEXT)

kb_3_page = InlineKeyboardMarkup(row_width=1).add(butt_quest11, butt_quest12, butt_quest13, butt_quest14, butt_quest15)
kb_3_page.row(butt_quest2_BACK, butt_questNONE)

html = types.ParseMode.HTML

# Хэндлеры
async def matvey_butt(message: types.Message):
	
	await message.answer('🤖')
	await message.answer(f"Привет, <b>{message.from_user.full_name}</b>!\nЯ твой помощник ЧаВо, давай выберем какой вопрос тебя интересует\n<pre>Страница 1 / 3</pre>", reply_markup=kb_1_page, parse_mode=html)


# Команда 1 вопроса
async def quest_1(callback: types.CallbackQuery):

    keyboard = InlineKeyboardMarkup().add(butt_esc)

    await callback.message.edit_text(f'Ответ на 1-ый вопрос =)', reply_markup=keyboard, parse_mode=html)


# Команда 2 вопроса
async def quest_2(callback: types.CallbackQuery):

    keyboard = InlineKeyboardMarkup().add(butt_esc)

    await callback.message.edit_text(f'Ответ на 2-ый вопрос =)', reply_markup=keyboard, parse_mode=html)


# Команда 3 вопроса
async def quest_3(callback: types.CallbackQuery):

    keyboard = InlineKeyboardMarkup().add(butt_esc)

    await callback.message.edit_text(f'Ответ на 3-ый вопрос =)', reply_markup=keyboard, parse_mode=html)


# Команда 4 вопроса
async def quest_4(callback: types.CallbackQuery):

    keyboard = InlineKeyboardMarkup().add(butt_esc)

    await callback.message.edit_text(f'Ответ на 4-ый вопрос =)', reply_markup=keyboard, parse_mode=html)


# Команда 5 вопроса
async def quest_5(callback: types.CallbackQuery):

    keyboard = InlineKeyboardMarkup().add(butt_esc)

    await callback.message.edit_text(f'Ответ на 5-ый вопрос =)', reply_markup=keyboard, parse_mode=html)


# Команда 6 вопроса
async def quest_6(callback: types.CallbackQuery):

    keyboard = InlineKeyboardMarkup().add(butt_esc)

    await callback.message.edit_text(f'Ответ на 6-ый вопрос =)', reply_markup=keyboard, parse_mode=html)


# Команда 7 вопроса
async def quest_7(callback: types.CallbackQuery):

    keyboard = InlineKeyboardMarkup().add(butt_esc)

    await callback.message.edit_text(f'Ответ на 7-ый вопрос =)', reply_markup=keyboard, parse_mode=html)


# Команда 8 вопроса
async def quest_8(callback: types.CallbackQuery):

    keyboard = InlineKeyboardMarkup().add(butt_esc)

    await callback.message.edit_text(f'Ответ на 8-ый вопрос =)', reply_markup=keyboard, parse_mode=html)


# Команда 9 вопроса
async def quest_9(callback: types.CallbackQuery):

    keyboard = InlineKeyboardMarkup().add(butt_esc)

    await callback.message.edit_text(f'Ответ на 9-ый вопрос =)', reply_markup=keyboard, parse_mode=html)


# Команда 10 вопроса
async def quest_10(callback: types.CallbackQuery):

    keyboard = InlineKeyboardMarkup().add(butt_esc)

    await callback.message.edit_text(f'Ответ на 10-ый вопрос =)', reply_markup=keyboard, parse_mode=html)


# Команда 11 вопроса
async def quest_11(callback: types.CallbackQuery):

    keyboard = InlineKeyboardMarkup().add(butt_esc)

    await callback.message.edit_text(f'Ответ на 11-ый вопрос =)', reply_markup=keyboard, parse_mode=html)


# Команда 12 вопроса
async def quest_12(callback: types.CallbackQuery):

    keyboard = InlineKeyboardMarkup().add(butt_esc)

    await callback.message.edit_text(f'Ответ на 12-ый вопрос =)', reply_markup=keyboard, parse_mode=html)


# Команда 13 вопроса
async def quest_13(callback: types.CallbackQuery):

    keyboard = InlineKeyboardMarkup().add(butt_esc)

    await callback.message.edit_text(f'Ответ на 13-ый вопрос =)', reply_markup=keyboard, parse_mode=html)


# Команда 14 вопроса
async def quest_14(callback: types.CallbackQuery):

    keyboard = InlineKeyboardMarkup().add(butt_esc)

    await callback.message.edit_text(f'Ответ на 14-ый вопрос =)', reply_markup=keyboard, parse_mode=html)


# Команда 15 вопроса
async def quest_15(callback: types.CallbackQuery):

    keyboard = InlineKeyboardMarkup().add(butt_esc)

    await callback.message.edit_text(f'Ответ на 15-ый вопрос =)', reply_markup=keyboard, parse_mode=html)


# Команда Не нашел
async def quest_none(callback: types.CallbackQuery):

    keyboard1 = InlineKeyboardMarkup().add(butt_boss, butt_esc)

    await callback.message.edit_text(f"Тогда я хз что тебе сказать, шуруй к боссу", reply_markup=keyboard1, parse_mode=html)


# Кнопка Возвращение
async def quest_esc(callback: types.CallbackQuery):

    await callback.message.edit_text(f"Привет! Я твой помощник ЧаВо, давай выберем какой вопрос тебя интересует\n<pre>Страница 1 / 3</pre>", reply_markup=kb_1_page, parse_mode=html)


# Кнопка Стр 1
async def quest_1_page(callback: types.CallbackQuery):

    await callback.message.edit_text(f"Привет! Я твой помощник ЧаВо, давай выберем какой вопрос тебя интересует\n<pre>Страница 1 / 3</pre>", reply_markup=kb_1_page, parse_mode=html)


# Кнопка Стр 2
async def quest_2_page(callback: types.CallbackQuery):

    await callback.message.edit_text(f"Привет! Я твой помощник ЧаВо, давай выберем какой вопрос тебя интересует\n<pre>Страница 2 / 3</pre>", reply_markup=kb_2_page, parse_mode=html)

# Кнопка Стр 3
async def quest_3_page(callback: types.CallbackQuery):

    await callback.message.edit_text(f"Привет! Я твой помощник ЧаВо, давай выберем какой вопрос тебя интересует\n<pre>Страница 3 / 3</pre>", reply_markup=kb_3_page, parse_mode=html)

# Регистрация хэндлеров
async def register_handlers(dp: Dispatcher):
    """Registration all handlers before processing update."""

    dp.register_message_handler(matvey_butt, commands='matvey')
    dp.register_callback_query_handler(quest_1, lambda c: c.data == 'q1')
    dp.register_callback_query_handler(quest_2, lambda c: c.data == 'q2')
    dp.register_callback_query_handler(quest_3, lambda c: c.data == 'q3')
    dp.register_callback_query_handler(quest_4, lambda c: c.data == 'q4')
    dp.register_callback_query_handler(quest_5, lambda c: c.data == 'q5')

    dp.register_callback_query_handler(quest_6, lambda c: c.data == 'q6')
    dp.register_callback_query_handler(quest_7, lambda c: c.data == 'q7')
    dp.register_callback_query_handler(quest_8, lambda c: c.data == 'q8')
    dp.register_callback_query_handler(quest_9, lambda c: c.data == 'q9')
    dp.register_callback_query_handler(quest_10, lambda c: c.data == 'q10')

    dp.register_callback_query_handler(quest_11, lambda c: c.data == 'q11')
    dp.register_callback_query_handler(quest_12, lambda c: c.data == 'q12')
    dp.register_callback_query_handler(quest_13, lambda c: c.data == 'q13')
    dp.register_callback_query_handler(quest_14, lambda c: c.data == 'q14')
    dp.register_callback_query_handler(quest_15, lambda c: c.data == 'q15')

    dp.register_callback_query_handler(quest_1_page, lambda c: c.data == 'qback1')
    dp.register_callback_query_handler(quest_2_page, lambda c: c.data == 'qnext1')
    dp.register_callback_query_handler(quest_2_page, lambda c: c.data == 'qback2')
    dp.register_callback_query_handler(quest_3_page, lambda c: c.data == 'qnext2')
    dp.register_callback_query_handler(quest_none, lambda c: c.data == 'qnone')
    dp.register_callback_query_handler(quest_esc, lambda c: c.data == 'esc')
