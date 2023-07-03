from aiogram import types, Dispatcher
from aiogram.types import (ReplyKeyboardRemove, 
                           InlineKeyboardMarkup,
                           InlineKeyboardButton)


html = types.ParseMode.HTML
main_chat_id = -1001886825499

'''
# Создаем Машину состояний
class Feedback(StatesGroup):
    waiting_for_start_feedback = State()
    waiting_for_message_feedback = State()
'''

# Клавиатура Начала
feedback_start = InlineKeyboardButton('Погнали!', callback_data='FB_go') # type: ignore
feedback_fb_start = InlineKeyboardMarkup(row_width=1).add(feedback_start) # type: ignore


async def matvey_feedback(message: types.Message):

    await message.answer(f'Мой Босс сказал мне, что Ваш робот уже готов\n'+
                        f'Не желаете ли отсавить отзыв о выполненной работе?',
                        reply_markup=feedback_fb_start)


async def matvey_feedback_writing(callback: types.CallbackQuery):

    await callback.message.edit_text(f'😉 Напишите отзыв в ответном сообщении\n'+
                         f'Отправляя отзыв боту, Вы <b>соглашаетесь</b> с публикацией Вашего отзыва '+
                         'в <a href="https://t.me/botsindachat">нашем сообществе</a>',
                         parse_mode=html) # type: ignore
    

async def matvey_feedback_end(message: types.Message):

    await message.forward(chat_id=main_chat_id) # type: ignore
    await message.answer_sticker(sticker=r'CAACAgIAAxkBAAEJOoJkfy21wy8strsgYcGlMKRdi7QgtAACaQAD29t-AAEjFTIg5Xxuuy8E')
    await message.answer(f'Спасибо Вам большое за отзыв, я уже опубликовал '+
                         'его в <a href="https://t.me/botsindachat">нашем сообществе</a>',
                          parse_mode=html, reply_markup=ReplyKeyboardRemove()) # type: ignore

async def register_handlers(dp: Dispatcher):
    # Основные хендлеры
    dp.register_message_handler(matvey_feedback, state='*', commands='matvey')
    dp.register_callback_query_handler(matvey_feedback_writing, lambda c: c.data == 'FB_go')
    dp.register_message_handler(matvey_feedback_end)