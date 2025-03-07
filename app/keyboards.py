from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

from aiogram.utils.keyboard import InlineKeyboardBuilder


vid2 = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='УЗНАТЬ СЕКРЕТ👈', url="https://t.me/c/1962837464/829")]])
vid1 = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='СМОТРЕТЬ ВИДЕО👈', url="https://www.youtube.com/@Crypto.Volium")]])
vid3 = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='ВЕРНУТЬСЯ👈', url="https://t.me/+85-AYipvVrw0MzYy")]])
admin = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='РАССЫЛКА', callback_data='panda')], [InlineKeyboardButton(text='Посмотреть статистку опроса', callback_data='menu_opsros')], [InlineKeyboardButton(text='Посмотреть информацию о подписчике', callback_data='zapros')]])
menu = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Опрос после отписки на канал', callback_data="opros_1")]])
proity = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Пройти опрос', callback_data="rrr")]])

def first_poll():
    inline_kb_list = [
        [InlineKeyboardButton(text='Приветственный опрос ТЕКСТ', callback_data='frst_poll', resize_keyboard=True)],
        [InlineKeyboardButton(text='Вернуться в админ-панель🔙', callback_data="back")],
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list, row_width=2)


def ease_link_kb():
    inline_kb_list = [
        [InlineKeyboardButton(text='🔊🟩 Рассылка', callback_data='panda', resize_keyboard=True)],
        [InlineKeyboardButton(text='📊🟪 Статистика канала', callback_data='menu_opsros', resize_keyboard=True)],
        [InlineKeyboardButton(text='🧩🟨 Информация о подписчике', callback_data='zapros', resize_keyboard=True)],
        [InlineKeyboardButton(text='🔇⬛️ Забанить/разбанить челика', callback_data='ban', resize_keyboard=True)],
        [InlineKeyboardButton(text='🔳🔲 Назначить/снять администратора', callback_data='sds', resize_keyboard=True)]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list, row_width=2)
comeback = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Вернуться в админ-панель🔙', callback_data="back")]])
def poisk():
    inline_kb_list = [
        [InlineKeyboardButton(text='Поиск по username 🩸', callback_data='search_username', resize_keyboard=True)],
        [InlineKeyboardButton(text='Поиск по ID 🎚', callback_data='search_id', resize_keyboard=True)],
        [InlineKeyboardButton(text='Вернуться в админ-панель🔙', callback_data="back")],
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list, row_width=2)


def statistik():
    inline_kb_list = [
        [InlineKeyboardButton(text='Результаты опроса после отписки 🩸', callback_data='get_res', resize_keyboard=True)],
        [InlineKeyboardButton(text='Результаты опроса перед подпиской 🩸', callback_data='get_ser', resize_keyboard=True)],
        [InlineKeyboardButton(text='Таблица опросника', callback_data='get_channel', resize_keyboard=True)],
        [InlineKeyboardButton(text='Вернуться в админ-панель🔙', callback_data="back")],
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list, row_width=2)


def question():
    inline_kb_list = [
        [InlineKeyboardButton(text='Слишком много уведомлений', callback_data=f'ans_{0}', resize_keyboard=True)],
        [InlineKeyboardButton(text='Не заходит контент', callback_data=f'ans_{1}', resize_keyboard=True)],
        [InlineKeyboardButton(text='Не хватает ценного общение в группе', callback_data=f'ans_{2}')],
        [InlineKeyboardButton(text='Я присоединился по ошибке', callback_data=f'ans_{3}')],
        [InlineKeyboardButton(text='Другое(пожалуйста уточни!)', callback_data=f'ans_{4}')],
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list, row_width=2)


def question2():
    inline_kb_list = [
        [InlineKeyboardButton(text='Да', callback_data=f'var_{0}', resize_keyboard=True)],
        [InlineKeyboardButton(text='50/50, не уверен', callback_data=f'var_{1}', resize_keyboard=True)],
        [InlineKeyboardButton(text='Не очень', callback_data=f'var_{2}')],
        [InlineKeyboardButton(text='Нет', callback_data=f'var_{3}')],
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list, row_width=2)


def asdd():
    inline_kb_list = [
        [InlineKeyboardButton(text='Каждый день', callback_data=f'coh_{0}', resize_keyboard=True)],
        [InlineKeyboardButton(text='1-3 раза в неделю', callback_data=f'coh_{1}', resize_keyboard=True)],
        [InlineKeyboardButton(text='Раз в несколько недель', callback_data=f'coh_{2}')],
        [InlineKeyboardButton(text='Не взаимодействовал', callback_data=f'coh_{3}')],
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list, row_width=2)

def rb_1():
    inline_kb_list = [
        [InlineKeyboardButton(text='Интерес к теме', callback_data=f'new_{0}', resize_keyboard=True)],
        [InlineKeyboardButton(text='Интерес к новостям и аналитике', callback_data=f'new_{1}', resize_keyboard=True)],
        [InlineKeyboardButton(text='Узнал от друга/коллеги', callback_data=f'new_{2}')],
        [InlineKeyboardButton(text='Просто решил присоединиться', callback_data=f'new_{3}')],
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list, row_width=2)

def rb_2():
    inline_kb_list = [
        [InlineKeyboardButton(text='Интересные темы для обсуждения', callback_data=f'new_{0}', resize_keyboard=True)],
        [InlineKeyboardButton(text='Интерактивные опросы и конкурсы', callback_data=f'new_{1}', resize_keyboard=True)],
        [InlineKeyboardButton(text='Возможность задать вопросы экспертам', callback_data=f'new_{2}')],
        [InlineKeyboardButton(text='Специальные материалы или полезные ресурсы', callback_data=f'new_{3}')],
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list, row_width=2)

def rb_3():
    inline_kb_list = [
        [InlineKeyboardButton(text='Видео и прямые эфиры', callback_data=f'new_{0}', resize_keyboard=True)],
        [InlineKeyboardButton(text='Краткие аналитические посты', callback_data=f'new_{1}', resize_keyboard=True)],
        [InlineKeyboardButton(text='Полезные ссылки и руководства', callback_data=f'new_{2}')],
        [InlineKeyboardButton(text='Общение и ответы на вопрос', callback_data=f'new_{3}')],
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list, row_width=2)

def rb_4():
    inline_kb_list = [
        [InlineKeyboardButton(text='Новости и тренды в индустрии', callback_data=f'new_{0}', resize_keyboard=True)],
        [InlineKeyboardButton(text='Обучающие материалы и рекомендации', callback_data=f'new_{1}', resize_keyboard=True)],
        [InlineKeyboardButton(text='Возможности для инвестиций', callback_data=f'new_{2}')],
        [InlineKeyboardButton(text='Взаимодействие с участниками', callback_data=f'new_{3}')],
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list, row_width=2)

def rb_5():
    inline_kb_list = [
        [InlineKeyboardButton(text='Посты с фактами и статистикой', callback_data=f'new_{0}', resize_keyboard=True)],
        [InlineKeyboardButton(text='Примеры из практики и истории успеха', callback_data=f'new_{1}', resize_keyboard=True)],
        [InlineKeyboardButton(text='Видеоконтент и трансляции', callback_data=f'new_{2}')],
        [InlineKeyboardButton(text='Аналитика, графики, прогнозы', callback_data=f'new_{3}')],
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list, row_width=2)

def rb_6():
    inline_kb_list = [
        [InlineKeyboardButton(text='Да, интересуют статьи и материалы', callback_data=f'new_{0}', resize_keyboard=True)],
        [InlineKeyboardButton(text='Да, хотелось бы участвовать в обсуждениях', callback_data=f'new_{1}', resize_keyboard=True)],
        [InlineKeyboardButton(text='Возможно, если это легко усваиваемая информация', callback_data=f'new_{2}')],
        [InlineKeyboardButton(text='Нет, меня больше интересует наблюдение за новостями', callback_data=f'new_{3}')],
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list, row_width=2)


def rb_7():
    inline_kb_list = [
        [InlineKeyboardButton(text='Получать знания и повышать уровень экспертизы', callback_data=f'new_{0}', resize_keyboard=True)],
        [InlineKeyboardButton(text='Следить за трендами и новостями', callback_data=f'new_{1}', resize_keyboard=True)],
        [InlineKeyboardButton(text='Искать возможности для личного или профессионального роста', callback_data=f'new_{2}')],
        [InlineKeyboardButton(text='Общаться с другими участниками и делиться опытом', callback_data=f'new_{3}')],
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list, row_width=2)


def rb_8():
    inline_kb_list = [
        [InlineKeyboardButton(text='0-500$', callback_data=f'new_{0}', resize_keyboard=True)],
        [InlineKeyboardButton(text='500-1000$', callback_data=f'new_{1}', resize_keyboard=True)],
        [InlineKeyboardButton(text='1000-1500$', callback_data=f'new_{2}')],
        [InlineKeyboardButton(text='больше 2000$', callback_data=f'new_{3}')],
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list, row_width=2)

def rb_9():
    inline_kb_list = [
        [InlineKeyboardButton(text='В плюсе', callback_data=f'new_{0}', resize_keyboard=True)],
        [InlineKeyboardButton(text='В минусе', callback_data=f'new_{1}', resize_keyboard=True)],
        [InlineKeyboardButton(text='Торгую в безубыток ', callback_data=f'new_{2}')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list, row_width=2)

def rb_10():
    inline_kb_list = [
        [InlineKeyboardButton(text='Да, проходил(а) курсы или личное наставничество', callback_data=f'new_{0}', resize_keyboard=True)],
        [InlineKeyboardButton(text='Самостоятельно искал(а) и изучал материалы', callback_data=f'new_{1}', resize_keyboard=True)]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list, row_width=2)