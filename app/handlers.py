from aiogram import F, Router, Bot
from aiogram.filters import CommandStart, Command , ChatMemberUpdatedFilter, IS_MEMBER, IS_NOT_MEMBER
from aiogram.types import Message, ChatJoinRequest, ChatMemberLeft, ContentType, ChatMemberUpdated, PollAnswer, FSInputFile, CallbackQuery, Poll
import app.database.requests as rq
import app.ex as tabl
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime, timedelta
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from app.keyboards import vid1, vid2, vid3, admin, menu, ease_link_kb, comeback, poisk, statistik, question, question2, asdd, rb_1, rb_2, rb_3, rb_4, rb_5, rb_6, rb_7, proity, first_poll, rb_10, rb_8, rb_9
from aiogram.methods import SendPoll
import openpyxl
import asyncio
import time
import threading
from threading import Thread
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from config import BOT_TOKEN, CHANNEL_ID  # Добавьте импорт токена
import os
from app.config import MEDIA_PATH, VIDEOS
import logging

# Настраиваем логирование
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = Router()
ANS1 = {'0' : 'Слишком много уведомлений', '1': 'Не заходит контент', '2': 'Не хватает ценного общение в группе', '3': 'Я присоединился по ошибке', '4': 'Другое(пожалуйста уточни!)'}
ANS2 = {'0' : 'Да', '1': '50/50, не уверен', '2': 'Не очень', '3': 'Нет'}
ANS3 = {'0' : 'Каждый день', '1': '1-3 раза в неделю', '2': 'Раз в несколько недель', '3': 'Не взаимодействовал'}

ANS4 = {'0' : 'Интерес к теме', '1': 'Интерес к новостям и аналитике', '2': 'Узнал от друга/коллеги', '3': 'Просто решил присоединиться'}
ANS5 = {'0' : 'Интересные темы для обсуждения', '1': 'Интерактивные опросы и конкурсы', '2': 'Возможность задать вопросы экспертам', '3': 'Специальные материалы или полезные ресурсы'}
ANS6 = {'0' : 'Видео и прямые эфиры', '1': 'Краткие аналитические посты', '2': 'Полезные ссылки и руководства', '3': 'Общение и ответы на вопрос'}
ANS7 = {'0' : 'Новости и тренды в индустрии', '1': 'Обучающие материалы и рекомендации', '2': 'Возможности для инвестиций', '3': 'Взаимодействие с участниками'}
ANS8 = {'0' : 'Посты с фактами и статистикой', '1': 'Примеры из практики и истории успеха', '2': 'Видеоконтент и трансляции', '3': 'Аналитика, графики, прогнозы'}
ANS9 = {'0' : 'Да, интересуют статьи и материалы', '1': 'Да, хотелось бы участвовать в обсуждениях', '2': 'Возможно, если это легко усваиваемая информация', '3': 'Нет, меня больше интересует наблюдение за новостями'}
ANS10 = {'0' : 'Получать знания и повышать уровень экспертизы', '1': 'Следить за трендами и новостями', '2': 'Искать возможности для личного или профессионального роста', '3': 'Общаться с другими участниками и делиться опытом'}
ANS11 = {'0' : ' 0-500$', '1': '500-1000$', '2': '1000-1500$', '3': 'больше 2000$'}
ANS12 = {'0' : 'В плюсе', '1': ' В минусе', '2': 'Торгую в безубыток'}
ANS13 = {'0' : 'Да, проходил(а) курсы или личное наставничество', '1': 'Самостоятельно искал(а) и изучал материалы'}

ADMIN = [987762906,7367627953]
USER_ADMIN = []
class MyForm(StatesGroup):
    message = State()
    opros1 = State()
    opros2 = State()
    opros3 = State()
    opros4 = State()
    opros5 = State()
    opros6 = State()
    opros7 = State()
    opros8 = State()
    opros9 = State()
    opros10 = State()
    opros11 = State()
    opros12 = State()
    opros13 = State()
    opros14 = State()
    gd = State()
    ans = State()
    user_username = State()
    idd = State()


# Функция для создания нового экземпляра бота
async def get_bot():
    return Bot(token=BOT_TOKEN)

def run_async(coro):
    """Вспомогательная функция для запуска асинхронного кода в синхронном контексте"""
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        return loop.run_until_complete(coro)
    finally:
        loop.close()

# Путь к папке с медиафайлами (измените на ваш путь)
MEDIA_PATH = os.path.join(os.path.dirname(__file__), '..', 'media')

def msg6(id: int):
    async def _msg6():
        bot = await get_bot()
        try:
            logger.info(f"Trying to send video from: {VIDEOS['welcome']}")
            
            if not os.path.exists(VIDEOS["welcome"]):
                logger.error(f"Video file not found at: {VIDEOS['welcome']}")
                raise FileNotFoundError("Video file not found")
                
            video = FSInputFile(VIDEOS["welcome"])
            await bot.send_video_note(
                chat_id=id,
                video_note=video,
                reply_markup=proity
            )
            
        except Exception as e:
            logger.error(f"Error in msg6: {e}")
            await bot.send_message(
                chat_id=id,
                text="Приветствую! К сожалению, видео-сообщение сейчас недоступно.",
                reply_markup=proity
            )
        finally:
            await bot.session.close()
    
    run_async(_msg6())

# Также можно добавить проверку при запуске бота
def check_video_file():
    if not os.path.exists(VIDEOS["welcome"]):
        logger.warning(f"Video file not found at startup: {VIDEOS['welcome']}")
    else:
        logger.info(f"Video file found at: {VIDEOS['welcome']}")

def msg1(id: int):
    async def _msg1():
        bot = await get_bot()
        try:
            await bot.send_photo(
                chat_id=id, 
                photo="https://ibb.co/Q9mbkLf", 
                caption='<b>Торговая стратегия с использованием ОДНОГО инструмента</b>\r\n\r\n' +
                       '🔥Записал для вас обучающий ролик \r\n\r\n'+
                       'С полным разбором механики имбалансов и их правильного использования\r\n\r\n',
                parse_mode='HTML',
                reply_markup=vid2
            )
        except Exception as e:
            print(f"Error in msg1: {e}")
        finally:
            await bot.session.close()
    
    run_async(_msg1())

async def msg2(id: int):
    bot = await get_bot()
    try:
        await bot.send_message(
            chat_id=id, 
            text='<b>Совет по торговле на текущем рынке</b>\r\n\r\n' +
'Это аспект который знают ВСЕ смарт-мани трейдеры, но все равно часто его упускают. \r\n\r\n'+
'Это поможет вам эффективно понимать направление работы с ценой.\r\n\r\n'+
'И открывать высокоточные сделки во время консолидации.\r\n\r\n'
, parse_mode='HTML', reply_markup=vid1)
    except Exception as e:
        print(f"Error in msg2: {e}")
    finally:
        await bot.session.close()
    
async def msg3(id: int):
    bot = await get_bot()
    try:
        await bot.send_photo(chat_id=id, photo="https://ibb.co/RDFLdVT", caption='<b>ЕДИНСТВЕННАЯ СТРАТЕГИЯ, которая нужна, чтобы зарабатывать от $5 000 в месяц</b>\r\n\r\n' +
'Это видео решит ваши проблемы в трейдинге\r\n\r\n'+
'Знаешь, в чем проблема большинства трейдеров? Они слишком все усложняют\r\n\r\n'+
'Поэтому я записал для вас видео с пошаговым алгоритмом для стабильной торговли в долгосроке\r\n\r\n' 
, parse_mode='HTML', reply_markup=vid2)
    except Exception as e:
        print(f"Error in msg3: {e}")
    finally:
        await bot.session.close()
    
async def msg4(id: int):
    bot = await get_bot()
    try:
        await bot.send_photo(chat_id=id, photo="https://ibb.co/xHNThgQ", caption='<b>Я бы хотел знать ЭТО, когда был НОВИЧКОМ</b>\r\n\r\n' +
'Большинство трейдеров на начальном этапе допускают одни и те же ошибки\r\n\r\n'+
'И если бы я узнал раньше о советах из этого видео, то добился бы успеха гораздо быстрее!\r\n\r\n'
, parse_mode='HTML', reply_markup=vid2)
    except Exception as e:
        print(f"Error in msg4: {e}")
    finally:
        await bot.session.close()
    
async def msg5(id: int):
    bot = await get_bot()
    try:
        await bot.send_photo(chat_id=id, photo="https://ibb.co/q51ftN9", caption='<b>Как я сделал 10.000$ ЗА МЕСЯЦ на трейдинге</b>\r\n\r\n'
, parse_mode='HTML', reply_markup=vid2)
    except Exception as e:
        print(f"Error in msg5: {e}")
    finally:
        await bot.session.close()
        

@router.chat_join_request()
async def start1(chat_join_request: ChatJoinRequest, bot: Bot, state: FSMContext):
    # тут мы принимаем юзера в канал
    await state.clear()
    await rq.set_user(chat_join_request.from_user.id, chat_join_request.from_user.username)
    try:
        await chat_join_request.approve()
        await bot.send_photo(chat_id=chat_join_request.from_user.id, photo="https://ibb.co/zNNgCvw", caption='<b>Рад приветствовать тебя в лучшем сообществе трейдеров в Восточной Европе – Crypto Volium 🤝</b>\r\n\r\n' +
		    '<b>Канал полностью открытый и бесплатный,</b> создан с целью объединения и обучения трейдеров.\r\n\r\n' +
                    'Рекомендую начать с изучения бесплатного обучения, которое я подготовил для тебя в <a href="https://t.me/c/1962837464/800">этом посте</a> 👈.\r\n\r\n' +
                    '💬 Так же у нас есть <a href="whttps://t.me/CRYPTO_VOLIUM_CHAT">публичный чат</a>, где ты можешь задавать вопросы и обсуждать торговые возможности.\r\n\r\n' +
		    'Методичка по торговой стратегии "Черепаший Суп" с винрейтом 74%: <a href="https://t.me/c/1962837464/860">ссылка</a> 📚\r\n\r\n' +
		    '📌 Сразу поставь канал в закреп и включи уведомления, чтобы не пропускать торговые идеи и обучение.', parse_mode='HTML')
        await rq.set_user(chat_join_request.from_user.id, chat_join_request.from_user.username)
        await bot.send_message(CHANNEL_ID, f'Новый подписчик @{chat_join_request.from_user.username} еще не прошел вступительный опрос')

      #  await bot.send_video_note(id, video_note="DQACAgIAAxkBAAIv8GdEqupmtUzkcqI1ETO68eXNqXgKAALaWgAChbSpSSwnR-Zse7Q9NgQ", reply_markup=proity)
     #   await bot.send_photo(chat_join_request.from_user.id, photo="https://ibb.org.ru/1/fEZDZ3", caption='Привет, трейдер! 🚀\nПомоги нам стать лучше! Пройди короткий опрос, для улучшения качества нашего проекта чтобы ты получил еще больше ценности.\n\n🎁За твою помощь, ты получишь материалы по SMT-дивергенции, которые помогут тебе ещё глубже понимать рынок и действовать увереннее. 📈(обычно $49)\n\nПройди короткий опрос и внеси свой вклад в развитие нашего сообщества.\n\nВместе мы можем достичь большего!', reply_markup=proity)
    except:
        pass
    id =  chat_join_request.from_user.id
   # time.sleep(120)
   # await bot.send_video_note(id, video_note="DQACAgIAAxkBAAIv8GdEqupmtUzkcqI1ETO68eXNqXgKAALaWgAChbSpSSwnR-Zse7Q9NgQ", reply_markup=proity)
    
    scheduler = AsyncIOScheduler(
        jobstores={
            'default': SQLAlchemyJobStore(url='sqlite:///jobs.sqlite')
        }
    )
    
    # Теперь используем синхронные функции
    scheduler.add_job(
        msg6, 
        trigger='date',
        run_date=datetime.now() + timedelta(seconds=1),#было 120
        kwargs={'id': id}
    )
    
    scheduler.add_job(
        msg1,
        trigger='date',
        run_date=datetime.now() + timedelta(seconds=86400),
        kwargs={'id': id}
    )
    
    scheduler.add_job(
        msg2,
        trigger='date',
        run_date=datetime.now() + timedelta(seconds=86400*2),
        kwargs={'id': id}
    )
    
    scheduler.add_job(
        msg3,
        trigger='date',
        run_date=datetime.now() + timedelta(seconds=86400*3),
        kwargs={'id': id}
    )
    
    scheduler.add_job(
        msg4,
        trigger='date',
        run_date=datetime.now() + timedelta(seconds=86400*4),
        kwargs={'id': id}
    )
    
    scheduler.add_job(
        msg5,
        trigger='date',
        run_date=datetime.now() + timedelta(seconds=86400*5),
        kwargs={'id': id}
    )
    
    scheduler.start()



@router.callback_query(F.data == 'rrr')
async def proit(callback: CallbackQuery, bot: Bot, state: FSMContext):
    await bot.answer_callback_query(callback.id, '')
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    await bot.send_message(callback.from_user.id, "1.Что побудило вас присоединиться к нашей группе?", reply_markup=rb_1())


@router.callback_query(F.data[:4] == 'new_', MyForm.opros6)
async def pols_2(callback: CallbackQuery, bot: Bot, state: FSMContext):
    await state.update_data(ans2=callback.data[4:])
    await bot.answer_callback_query(callback.id, 'Спасибо за ответ')
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    await bot.send_message(callback.from_user.id, "3.Есть ли что-то, что вы хотели бы видеть в группе?", reply_markup=rb_3())
    await state.set_state(MyForm.opros7)
    data = await state.get_data()
    q5 = ''
    for i in data:
        q5 += str(data[i])
    q5 += '77777777'
    try:
        await rq.set_q(callback.from_user.id, 5, q5)
    except Exception as e:
        print(f"Error in pols_2: {e}")
        # Обработка ошибки...
    
@router.callback_query(F.data[:4] == 'new_', MyForm.opros7)
async def pols_3(callback: CallbackQuery, bot: Bot, state: FSMContext):
    await state.update_data(ans3=callback.data[4:])
    await bot.answer_callback_query(callback.id, 'Спасибо за ответ')
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    await bot.send_message(callback.from_user.id, "4.Какие темы вам интересны больше всего?", reply_markup=rb_4())
    await state.set_state(MyForm.opros8)
    data = await state.get_data()
    q5 = ''
    for i in data:
        q5 += str(data[i])
    q5 += '7777777'
    try:
        await rq.set_q(callback.from_user.id, 5, q5)
    except Exception as e:
        print(f"Error in pols_3: {e}")
        # Обработка ошибки...
    
@router.callback_query(F.data[:4] == 'new_', MyForm.opros8)
async def pols_4(callback: CallbackQuery, bot: Bot, state: FSMContext):
    await state.update_data(ans4=callback.data[4:])
    await bot.answer_callback_query(callback.id, 'Спасибо за ответ')
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    await bot.send_message(callback.from_user.id, "5.Какие типы контента вызывают у вас наибольший интерес?", reply_markup=rb_5())
    await state.set_state(MyForm.opros9)
    data = await state.get_data()
    q5 = ''
    for i in data:
        q5 += str(data[i])
    q5 += '777777'
    try:
        await rq.set_q(callback.from_user.id, 5, q5)
    except Exception as e:
        print(f"Error in pols_4: {e}")
        # Обработка ошибки...
    
    
@router.callback_query(F.data[:4] == 'new_', MyForm.opros9)
async def pols_5(callback: CallbackQuery, bot: Bot, state: FSMContext):
    await state.update_data(ans5=callback.data[4:])
    await bot.answer_callback_query(callback.id, 'Спасибо за ответ')
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    await bot.send_message(callback.from_user.id, "6.Интересны ли вам возможности для обучения?", reply_markup=rb_6())
    await state.set_state(MyForm.opros10)
    data = await state.get_data()
    q5 = ''
    for i in data:
        q5 += str(data[i])
    q5 += '77777'
    try:
        await rq.set_q(callback.from_user.id, 5, q5)
    except Exception as e:
        print(f"Error in pols_5: {e}")
        # Обработка ошибки...
    


@router.callback_query(F.data[:4] == 'new_', MyForm.opros10)
async def pols_6(callback: CallbackQuery, bot: Bot, state: FSMContext):
    await state.update_data(ans6=callback.data[4:])
    await bot.answer_callback_query(callback.id, 'Спасибо за ответ')
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    data = await state.get_data()
    q5 = ''
    for i in data:
        q5 += str(data[i])
    q5 += '7777'
    try:
        await rq.set_q(callback.from_user.id, 5, q5)
    except Exception as e:
        print(f"Error in pols_6: {e}")
        # Обработка ошибки...
    await bot.send_message(callback.from_user.id, "7.Какие цели вы преследуете, присоединившись к группе?", reply_markup=rb_7())
    await state.set_state(MyForm.opros11)
    
@router.callback_query(F.data[:4] == 'new_', MyForm.opros11)
async def pols_7(callback: CallbackQuery, bot: Bot, state: FSMContext):
    await state.update_data(ans7=callback.data[4:])
    await bot.answer_callback_query(callback.id, 'Спасибо за ответ')
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    data = await state.get_data()
    q5 = ''
    for i in data:
        q5 += str(data[i])
    q5 += '777'
    try:
        await rq.set_q(callback.from_user.id, 5, q5)
    except Exception as e:
        print(f"Error in pols_7: {e}")
        # Обработка ошибки...
    await bot.send_message(callback.from_user.id, "8.Какой у тебя доход?  (*это только между нами)", reply_markup=rb_8())
    await state.set_state(MyForm.opros12)
    
@router.callback_query(F.data[:4] == 'new_', MyForm.opros12)
async def pols_8(callback: CallbackQuery, bot: Bot, state: FSMContext):
    await state.update_data(ans8=callback.data[4:])
    await bot.answer_callback_query(callback.id, 'Спасибо за ответ')
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    data = await state.get_data()
    q5 = ''
    for i in data:
        q5 += str(data[i])
    q5 += '77'
    try:
        await rq.set_q(callback.from_user.id, 5, q5)
    except Exception as e:
        print(f"Error in pols_8: {e}")
        # Обработка ошибки...
    await bot.send_message(callback.from_user.id, "9.Результаты торговли?", reply_markup=rb_9())
    await state.set_state(MyForm.opros13)
    
@router.callback_query(F.data[:4] == 'new_', MyForm.opros13)
async def pols_9(callback: CallbackQuery, bot: Bot, state: FSMContext):
    await state.update_data(ans9=callback.data[4:])
    await bot.answer_callback_query(callback.id, 'Спасибо за ответ')
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    data = await state.get_data()
    q5 = ''
    for i in data:
        q5 += str(data[i])
    q5 += '7'
    try:
        await rq.set_q(callback.from_user.id, 5, q5)
    except Exception as e:
        print(f"Error in pols_9: {e}")
        # Обработка ошибки...
    await bot.send_message(callback.from_user.id, "10.Проходили обучение по трейдингу?", reply_markup=rb_10())
    await state.set_state(MyForm.opros14)
    
    
@router.callback_query(F.data[:4] == 'new_', MyForm.opros14)
async def pols_10(callback: CallbackQuery, bot: Bot, state: FSMContext):
    await bot.answer_callback_query(callback.id, 'Спасибо за ответ')
    try:
        await bot.delete_message(callback.from_user.id, callback.message.message_id)
    except:
        pass
    await state.update_data(ans10=callback.data[4:])
    try:
        data = await state.get_data()
        q5 = ''
        for i in data:
            q5 += str(data[i])
        await rq.set_q(callback.from_user.id, 5, q5)
        ans = str(f'<i>Пользователь:</i> @{callback.from_user.username} <i>Что побудило вас присоединиться к нашей группе?:</i> {ANS4[q5[0]]}\n<i>Что могло бы побудить вас активнее участвовать?:</i> {ANS5[q5[1]]}\n<i>Есть ли что-то, что вы хотели бы видеть в группе?:</i> {ANS6[q5[2]]}\n<i>Какие темы вам интересны больше всего?:</i> {ANS7[q5[3]]}\n<i>Какие типы контента вызывают у вас наибольший интерес?:</i> {ANS8[q5[4]]}\n<i>Интересны ли вам возможности для обучения?:</i> {ANS9[q5[5]]}\n<i>Какие цели вы преследуете, присоединившись к группе?:</i> {ANS10[q5[6]]}\
\nКакой у тебя доход?  (*это только между нами) : {ANS11[q5[7]]}\nРезультаты торговли : {ANS12[q5[8]]}\nПроходили обучение по трейдингу? : {ANS13[q5[9]]}')
        await rq.set_opros2(callback.from_user.id, ans)
        print(ans)
        await bot.send_document(callback.from_user.id, document=FSInputFile('Методичка SMT от Crypto Volium 2.pdf'), caption='Спасибо, что помогаешь нам стать лучше!')
        await rq.set_opros(callback.from_user.id, ans)
        await bot.send_message(CHANNEL_ID, text=ans, parse_mode='HTML')
    except:
        pass
    await state.clear()
 


@router.callback_query(F.data[:4] == 'new_')
async def pols_1(callback: CallbackQuery, bot: Bot, state: FSMContext):
    await state.update_data(ans1=callback.data[4:])
    await bot.answer_callback_query(callback.id, 'Спасибо за ответ')
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    await bot.send_message(callback.from_user.id, "2.Что могло бы побудить вас активнее участвовать?", reply_markup=rb_2())
    await state.set_state(MyForm.opros6)
    data = await state.get_data()
    q5 = ''
    for i in data:
        q5 += str(data[i])
    q5 += '777777777'
    await rq.set_q(callback.from_user.id, 5, q5)    


@router.callback_query(F.data == 'get_channel')
async def exc(callback: CallbackQuery, bot: Bot, state: FSMContext):
    try:
        # Сообщаем о начале обработки
        await callback.answer('Формирую статистику...')
        
        # Просто используем await вместо создания нового loop
        await tabl.st()
        
        # Отправляем подтверждение
        await callback.answer('Четенько')
        
        # Отправляем файл
        await bot.send_document(
            callback.from_user.id, 
            document=FSInputFile('data.xlsx'), 
            caption='Статистика'
        )
        
    except Exception as e:
        logger.error(f"Error in exc: {e}")
        await callback.answer('Произошла ошибка', show_alert=True)




@router.callback_query(F.data == 'frst_poll')
async def frst_poll(callback: CallbackQuery, bot: Bot, state: FSMContext):
    await bot.answer_callback_query(callback.id, 'БЫстро блеат')
    for i in (await rq.get_users()):
        try: 
  
            await bot.send_photo(i[0], photo="https://ibb.org.ru/1/fEZDZ3" ,caption='Привет, трейдер! 🚀\nПомоги нам стать лучше! Пройди короткий опрос, для улучшения качества нашего проекта чтобы ты получил еще больше ценности.\n\n🎁За твою помощь, ты получишь материалы по SMT-дивергенции, которые помогут тебе ещё глубже понимать рынок и действовать увереннее. 📈 (обычно $49)\n\nПройди короткий опрос и внеси свой вклад в развитие нашего сообщества.\n\nВместе мы можем достичь большего!', reply_markup=proity)
        except:
            print(i)   
    await state.clear() 


@router.message(F.text == 'admin')
async def admin2(message: Message, bot: Bot, state: FSMContext):
    if message.from_user.id in ADMIN or message.from_user.username in USER_ADMIN:
        await bot.send_message(message.from_user.id, '🔻Добро пожаловать повэлитель🔺', reply_markup=ease_link_kb())
    else:
        await bot.send_message(message.from_user.id, 'Куда лезешь щенок')


@router.callback_query(F.data == 'panda')
async def qr1(callback: CallbackQuery, bot: Bot, state: FSMContext):
    await bot.answer_callback_query(callback.id, 'ЕБООООШЬ ПО ВСЕМ....')
    await callback.message.answer(f'Введите текст рассылки', reply_markup=first_poll())
    await state.set_state(MyForm.message)


@router.callback_query(F.data == 'zapros')
async def qr2(callback: CallbackQuery, bot: Bot, state: FSMContext):
    await bot.answer_callback_query(callback.id, 'Что же он там прячет?....')
    await callback.message.answer(f'Выберите как вы хотите реализовать поиск повэлитель🌑', reply_markup=poisk())

@router.callback_query(F.data == 'search_username')
async def qr3(callback: CallbackQuery, bot: Bot, state: FSMContext):
    await bot.answer_callback_query(callback.id, ':)')
    await callback.message.answer(f'Введите username пользователя без @', reply_markup=comeback)
    await state.set_state(MyForm.user_username)
    
@router.callback_query(F.data == 'search_id')
async def qr4(callback: CallbackQuery, bot: Bot, state: FSMContext):
    await bot.answer_callback_query(callback.id, ':)')
    await callback.message.answer(f'Введите id пользователя', reply_markup=comeback)
    await state.set_state(MyForm.idd)
    
@router.callback_query(F.data == 'menu_opsros')
async def qr5(callback: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(callback.id, 'ты че эксель')
    await callback.message.answer(f'опа опа опапа', reply_markup=statistik())

@router.callback_query(F.data == 'get_res')
async def qr6(callback: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(callback.id, 'ну смотрице')
    ans = [[-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1]]
    ans[0][4] = (await rq.get_q(1, 4))[0][0]
    for i in range(1, 4):
        for j in range(0, 4):
            ans[i - 1][j] = (await rq.get_q(i, j))[0][0]
    await bot.send_document(callback.from_user.id, document=FSInputFile('test.txt'), caption='Ответы: ДРУГОЕ')
    await bot.send_document(callback.from_user.id, document=FSInputFile('ans.txt'), caption='Чтобы пользователи хотели видеть в Crypto Volium')
    await bot.send_message(callback.from_user.id, f'Покинули Crypto Volium потому, что\n---Слишком много уведомлений:{ans[0][0]}\n---Не заходит контент: {ans[0][1]}\n---Не хватает ценного общение в группе: {ans[0][2]}\n\
---Я присоединился по ошибке: {ans[0][3]}\n---Другое: {ans[0][4]}\nБыл ли контент полезен:\n---Да: {ans[1][0]}\n---50/50: {ans[1][1]}\n---Не очень: {ans[1][2]}\n---Нет: {ans[1][3]}\n\
Часто ли взаимодействовали с сообществом:\n---Каждый день: {ans[2][0]}\n---1-3 раза в неделю: {ans[2][1]}\n---Раз в несколько недель: {ans[2][2]}\n---Не взаимодействовал: {ans[2][3]}\n', reply_markup=comeback)
    
@router.callback_query(F.data == 'get_ser')
async def qr7(callback: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(callback.id, 'ну смотрице')
    ans = [[0] * 4 for i in range(10)]
    q5 = await rq.get_ans1()
    el = ''
    arr = []
    for i in q5:
        if i[0] != 'Не проходил':
            el += str(i[0])
    print(el)
    for j in range(10):
        ex = ''
        for i in range(j, len(el), 10):
            ex += el[i]
        arr.append(ex)  
    print(arr)
            
    await bot.send_message(callback.from_user.id, f'Что побудило вас присоединиться к нашей группе?\n---Интерес к теме: {arr[0].count("0")}\n---Интерес к новостям и аналитике: {arr[0].count("1")}\n---Узнал от друга/коллеги: {arr[0].count("2")}\n\
---Просто решил присоединиться: {arr[0].count("3")}\nЧто могло бы побудить вас активнее участвовать?:\n---Интересные темы для обсуждения: {arr[1].count("0")}\n---Интерактивные опросы и конкурсы: {arr[1].count("1")}\n---Возможность задать вопросы экспертам: {arr[1].count("2")}\n---Специальные материалы или полезные ресурсы: {arr[1].count("3")}\n\
Есть ли что-то, что вы хотели бы видеть в группе?:\n--Видео и прямые эфиры: {arr[2].count("0")}\n---Краткие аналитические посты: {arr[2].count("1")}\n---Полезные ссылки и руководств: {arr[2].count("2")}\n---Общение и ответы на вопрос: {arr[2].count("3")}\n\
Какие темы вам интересны больше всего?:\n--Новости и тренды в индустрии: {arr[3].count("0")}\n---Обучающие материалы и рекомендации: {arr[3].count("1")}\n--Возможности для инвестиций: {arr[3].count("2")}\n---Взаимодействие с участниками: {arr[3].count("3")}\n\
Какие типы контента вызывают у вас наибольший интерес?:\n--Посты с фактами и статистикой: {arr[4].count("0")}\n---Примеры из практики и истории успеха: {arr[4].count("1")}\n--Видеоконтент и трансляции: {arr[4].count("2")}\n---Аналитика, графики, прогнозы: {arr[4].count("3")}\n\
Интересны ли вам возможности для обучения?:\n--Да, интересуют статьи и материалы: {arr[5].count("0")}\n---Да, хотелось бы участвовать в обсуждениях: {arr[5].count("1")}\n--Возможно, если это легко усваиваемая информация: {arr[5].count("2")}\n---Нет, меня больше интересует наблюдение за новостями: {arr[5].count("3")}\n\
Какие цели вы преследуете, присоединившись к группе?:\n--Получать знания и повышать уровень экспертизы: {arr[6].count("0")}\n---Следить за трендами и новостями: {arr[6].count("1")}\n--Искать возможности для личного или профессионального роста: {arr[6].count("2")}\n---Общаться с другими участниками и делиться опытом: {arr[6].count("3")}\n\
Какой у тебя доход?  (*это только между нами):\n-- 0-500$: {arr[7].count("0")}\n---500-1000$: {arr[7].count("1")}\n--1000-1500$: {arr[7].count("2")}\n---больше 2000$ {arr[7].count("3")}\n\
Какие у тебя результаты торговли?:\n-- В плюсе: {arr[8].count("0")}\n---В минусе: {arr[8].count("1")}\n--Торгую в безубыток: {arr[8].count("2")}\n\
Проходили обучение по трейдингу?:\n--да, проходил(а) курсы или личное наставничество: {arr[9].count("0")}\n---Самостоятельно искал(а) и изучал материалы: {arr[9].count("1")}\n\
   ', reply_markup=comeback)
        
    
    
    

@router.message(MyForm.user_username)
async def mes(message: Message, bot: Bot, state: FSMContext):
    try:
        # Получаем username без @
        username = message.text.lstrip('@')
        
        # Получаем данные пользователя (с await)
        data = await rq.get_user_by_username(username)
        
        if not data:
            await bot.send_message(
                message.from_user.id, 
                f"Пользователь @{username} не найден в базе данных"
            )
            return
        
        # Определяем статус
        s = "Статус: Активный"
        
        # Отправляем информацию
        await bot.send_message(
            message.from_user.id, 
            f'🔲<b>Информация о пользователе:</b>🔳\n'
            f'<b>Id:</b> <i>{data[1]}</i>\n'
            f'<b>Присоединился первый раз к сообществу:</b> <i>{data[2]}</i>\n'
            f'<b>Результат опроса после отписки:</b>\n{data[3]}\n'
            f'<b>Результат опроса перед подпиской:</b>\n{data[11]}\n\n'
            f'<b>Username:</b> <i>@{data[4]}</i>\n\n'
            f'<b>{s}</b>', 
            parse_mode='HTML'
        )
        
    except Exception as e:
        logger.error(f"Error in mes handler: {e}")
        await bot.send_message(
            message.from_user.id, 
            "Произошла ошибка при получении информации"
        )
    finally:
        await state.clear()
    
    
@router.message(MyForm.idd)
async def get_info_by_id(message: Message, bot: Bot, state: FSMContext):
    try:
        # Проверяем, что введён корректный ID
        try:
            user_id = int(message.text)
        except ValueError:
            await bot.send_message(
                message.from_user.id,
                "Пожалуйста, введите корректный числовой ID"
            )
            return

        # Получаем данные пользователя
        data = await rq.get_user_by_id(user_id)
        
        if not data:
            await bot.send_message(
                message.from_user.id,
                f"Пользователь с ID {user_id} не найден"
            )
            return
        
        # Определяем статус
        s = "Статус: Активный"
        
        # Отправляем информацию
        await bot.send_message(
            message.from_user.id,
            f'🔲<b>Информация о пользователе:</b>🔳\n'
            f'<b>Id:</b> <i>{data[1]}</i>\n'
            f'<b>Присоединился первый раз к сообществу:</b> <i>{data[2]}</i>\n'
            f'<b>Результат опроса после отписки:</b>\n{data[3]}\n'
            f'<b>Результат опроса перед подпиской:</b>\n{data[11]}\n\n'
            f'<b>Username:</b> <i>@{data[4]}</i>\n\n'
            f'<b>{s}</b>',
            parse_mode='HTML'
        )
        
    except Exception as e:
        logger.error(f"Error in get_info_by_id: {e}")
        await bot.send_message(
            message.from_user.id,
            "Произошла ошибка при получении информации"
        )
    finally:
        await state.clear()

@router.callback_query(F.data == 'back')
async def admin1(callback: CallbackQuery, bot: Bot, state: FSMContext):
    await state.clear()
    if callback.from_user.id in ADMIN or callback.from_user.username in USER_ADMIN:
        print('AAAAAAAAAAAAAAAa')
        await bot.answer_callback_query(callback.id, 'I will be comeback....')
        await bot.send_message(callback.from_user.id, '🔺Добро пожаловать повэлитель🔻', reply_markup=ease_link_kb())
    else:
        await bot.send_message(callback.from_user.id, 'Куда лезешь щенок')
    
       
@router.message(MyForm.message)
async def handle_message_for_broadcast(message: Message, state: FSMContext, bot: Bot):
    if message.text == '1%1':
        pass
    else:
        if message.photo is not None:

            for i in (await rq.get_users()):
                if message.caption is None:
                    d = ''
                else:
                    d = message.caption
                try:
                    await bot.send_photo(i[0], photo=message.photo[0].file_id, caption=f"{d}")
                except:
                    print(i)
        else:
            if message.video_note is not None:
                print(message.video_note.file_id)
                for i in (await rq.get_users()):


                    try:
                        await bot.send_video_note(i[0], video_note=message.video_note.file_id)
                    except:
                        print(i)
            else:
                
                
                for i in (await rq.get_users()):
                    try:
                        await bot.send_message(i[0], f'{message.text}')
                    except:
                        print(i)
        await bot.send_message(message.from_user.id, 'Успешно')
    await state.clear()





@router.chat_member(ChatMemberUpdatedFilter(IS_MEMBER >> IS_NOT_MEMBER))
async def left_member(event: ChatMemberUpdated, bot: Bot, state: FSMContext):
    try:
        await state.clear()
        await rq.set_leftmember(event.old_chat_member.user.id)
        try:
            await bot.send_message(CHANNEL_ID, text=f'Пользователь @{event.old_chat_member.user.username} решил покинуть нас')
        except:
            pass
        await bot.send_message(event.old_chat_member.user.id, text='Ты ушел, так и не попрощавшись? Напиши, что помогло бы тебе стать эффективнее, или же, что бы ты хотел видеть у нас на канале. Мы стремимся давать наибольший уровень ценности в нашем канале и ты нам можешь помочь в этом. Пройди короткий опрос и получи секретную методичку которую я использую ежедневно!')
        await bot.send_message(event.old_chat_member.user.id, '1.Почему ты решил покинуть Crypto Volium?',
                              reply_markup=question())
        
    except:
        pass

@router.callback_query(F.data[:4] == 'ans_')
async def polfl_answer_1(callback: CallbackQuery, bot: Bot, state: FSMContext):
    await rq.set_q(callback.from_user.id, 1, callback.data[4:])
    await bot.answer_callback_query(callback.id, 'Спасибо за ответ')
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    if callback.data[4:] == '4':
        await state.set_state(MyForm.ans)
        await bot.send_message(callback.from_user.id, "Пожалуйста уточните, что именно повлияло на ваш уход из сообщества?")
    else:
        await state.update_data(name=ANS1[callback.data[4:]])
        await bot.send_message(callback.from_user.id, "2.Был ли полезен наш контент?", reply_markup=question2())
        await state.set_state(MyForm.opros2)

@router.callback_query(F.data[:4] == 'var_', MyForm.opros2)
async def poll_answer_2(callback: CallbackQuery, bot: Bot, state: FSMContext):
    await rq.set_q(callback.from_user.id, 2, callback.data[4:])
    await bot.answer_callback_query(callback.id, 'Спасибо за ответ')
    await state.update_data(e=ANS2[callback.data[4:]])
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    await bot.send_message(callback.from_user.id, "3.Как часто ты взаимодействовал с Crypto Volium?", reply_markup=asdd())
    await state.set_state(MyForm.opros3)



    
@router.callback_query(F.data[:4] == 'coh_', MyForm.opros3)
async def poll_answer_3(callback: CallbackQuery, bot: Bot, state: FSMContext):
    await rq.set_q(callback.from_user.id, 3, callback.data[4:])
    await bot.answer_callback_query(callback.id, 'Спасибо за ответ')
    await state.update_data(f=ANS3[callback.data[4:]])
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    await bot.send_message(callback.from_user.id, text='4.Что бы ты хотел видеть чтобы остаться в Crypto Volium?')
    await state.set_state(MyForm.opros4)

@router.message(MyForm.opros4)
async def pool_answer_4(message: Message, state: FSMContext, bot: Bot):
    try:
        ans = message.text
        await rq.set_opros(message.from_user.id, ans)
    except Exception as e:
        print(f"Error in pool_answer_4: {e}")
        # Обработка ошибки...
    await bot.send_message(message.from_user.id, 'Успешно')
    await state.clear()

@router.message(MyForm.ans)
async def poa(message: Message, state: FSMContext, bot: Bot):
    await state.update_data(name=message.text)
    with open("test.txt", 'a') as myfile:
        myfile.write("\n" + message.text)
        
    await bot.send_poll(message.from_user.id, question='3.Был ли полезен наш контент?',
                                    options=['Да', '50/50, не уверен', 'Не очень', 'Нет'],   is_anonymous=False)
        
    await state.set_state(MyForm.opros2)

CHANNEL_ID = CHANNEL_ID  # Ваш ID канала

async def check_subscription(user_id: int, bot: Bot) -> bool:
    try:
        member = await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=user_id)
        return member.status in ['member', 'administrator', 'creator']
    except:
        return False

@router.message(Command("start"))
async def cmd_start(message: Message, bot: Bot):
    is_subscribed = await check_subscription(message.from_user.id, bot)
    if not is_subscribed:
        await message.answer("Пожалуйста, подпишитесь на канал, чтобы использовать бота")
        return
    # Дальнейшая логика для подписчиков
    await message.answer("Добро пожаловать!")

@router.message(F.video_note)
async def get_video_note_id(message: Message):
    """Хендлер для получения file_id видео-кружка"""
    print(f"Video note file_id: {message.video_note.file_id}")