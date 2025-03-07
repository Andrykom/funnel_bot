import asyncio
import logging
from config import BOT_TOKEN, CHANNEL_ID
from aiogram import Bot, Dispatcher
from app.handlers import router
from app.database.models import async_main
from aiogram.filters import ChatMemberUpdatedFilter, IS_NOT_MEMBER, IS_MEMBER
from app.handlers import MyForm, handle_message_for_broadcast, polfl_answer_1, poll_answer_2, poll_answer_3, pool_answer_4, start1, left_member, poa, mes, get_info_by_id, pols_1, pols_2, pols_3, pols_4, pols_5, pols_6, pols_7, pols_9, pols_8, pols_10, check_video_file
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
import app.database.requests as rq
from sqlalchemy.ext.asyncio import create_async_engine
import sqlite3
from app.database.requests import init_db, migrate_db
import os
from sqlalchemy import text

DATABASE_URL = "sqlite+aiosqlite:///app/database/db.sqlite"
engine = create_async_engine(DATABASE_URL)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(storage=MemoryStorage())
logging.basicConfig(level=logging.INFO)

# Настройка логгера
logger = logging.getLogger(__name__)

async def main():
    # Сначала создаем/проверяем базу данных
    logger.info("Initializing database...")
    init_db()  # Создаем таблицу users
    
    # Затем проверяем структуру
    logger.info("Verifying database structure...")
    db_ok = await verify_db_structure()
    if not db_ok:
        logger.error("Database verification failed!")
        return
    
    # Проверяем права доступа
    if not check_db_access():
        logger.error("Database access check failed!")
        return
    
    # Проверяем наличие видео
    check_video_file()
    
    # Запускаем основную логику бота
    await async_main()
    dp.include_router(router)
    
    # Регистрируем хендлеры
    dp.chat_member.register(start1, ChatMemberUpdatedFilter(IS_NOT_MEMBER >> IS_MEMBER))  
    dp.chat_member.register(left_member, ChatMemberUpdatedFilter(IS_MEMBER >> IS_NOT_MEMBER))
    dp.message.register(handle_message_for_broadcast, MyForm.message)
    dp.message.register(poa, MyForm.ans)
    dp.message.register(mes, MyForm.user_username)
    dp.message.register(get_info_by_id, MyForm.idd)
    dp.poll_answer.register(poll_answer_2, MyForm.opros2)
    dp.poll_answer.register(poll_answer_3, MyForm.opros3)
    dp.message.register(pool_answer_4, MyForm.opros4)
    dp.message.register(pols_1, MyForm.opros5)
    dp.message.register(pols_2, MyForm.opros6)
    dp.message.register(pols_3, MyForm.opros7)
    dp.message.register(pols_4, MyForm.opros8)
    dp.message.register(pols_5, MyForm.opros9)
    dp.message.register(pols_6, MyForm.opros10)
    dp.message.register(pols_7, MyForm.opros11)
    dp.message.register(pols_8, MyForm.opros12)
    dp.message.register(pols_9, MyForm.opros13)
    dp.message.register(pols_10, MyForm.opros14)
    
    # Запуск бота
    await dp.start_polling(bot)

async def diagnose_db():
    logger.info("Starting database diagnosis")
    
    # Проверяем существование файла
    if not os.path.exists(DATABASE_URL):
        logger.error(f"Database file not found at {DATABASE_URL}")
        return
    
    
    # Проверяем соединение
    try:
        async with engine.connect() as conn:
            await conn.execute("SELECT 1")
            logger.info("Database connection successful")
    except Exception as e:
        logger.error(f"Connection failed: {e}")
        
def check_db_access():
    """Проверяет права доступа к файлу базы данных"""
    db_path = "app/database/db.sqlite"
    db_dir = os.path.dirname(db_path)
    
    try:
        # Проверяем права на запись в директорию
        if not os.access(db_dir, os.W_OK):
            logger.error(f"Нет прав на запись в директорию {db_dir}")
            return False
            
        # Если файл существует, проверяем права на чтение/запись
        if os.path.exists(db_path):
            if not os.access(db_path, os.R_OK | os.W_OK):
                logger.error(f"Нет прав на чтение/запись файла {db_path}")
                return False
                
        return True
        
    except Exception as e:
        logger.error(f"Ошибка при проверке прав доступа: {e}")
        return False

async def verify_db_structure():
    """Проверяет структуру базы данных"""
    try:
        async with engine.connect() as conn:
            # Проверяем существование таблиц
            result = await conn.execute(text("SELECT name FROM sqlite_master WHERE type='table'"))
            rows = result.fetchall()  # Без await
            tables = [row[0] for row in rows]
            
            logger.info(f"Found tables: {tables}")
            
            # Проверяем наличие необходимых таблиц
            required_tables = ['users']
            for table in required_tables:
                if table not in tables:
                    logger.error(f"Missing required table: {table}")
                    return False
            
            # Проверяем структуру таблицы users
            result = await conn.execute(text("PRAGMA table_info(users)"))
            columns = result.fetchall()  # Без await
            column_names = [col[1] for col in columns]
            
            logger.info(f"Found columns: {column_names}")
            
            # Проверяем наличие необходимых столбцов
            required_columns = ['id', 'tg_id', 'username', 'join_date', 'Opros']
            required_columns.extend([f'q{i}' for i in range(1, 11)])
            
            missing_columns = [col for col in required_columns if col not in column_names]
            if missing_columns:
                logger.error(f"Missing columns: {missing_columns}")
                return False
            
            logger.info("Database structure verification completed successfully")
            return True
            
    except Exception as e:
        logger.error(f"Error verifying database structure: {e}")
        return False

if __name__ == "__main__":
    asyncio.run(main())


