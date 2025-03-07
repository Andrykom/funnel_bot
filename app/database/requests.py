import sqlite3
from pathlib import Path
from typing import Optional, Tuple
import logging
import aiosqlite

logger = logging.getLogger(__name__)

# Путь к базе данных
DATABASE_URL = Path(__file__).parent / 'db.sql'

def get_db():
    """Создает соединение с БД и возвращает его"""
    conn = sqlite3.connect(DATABASE_URL)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Инициализация базы данных"""
    conn = sqlite3.connect('app/database/db.sqlite')
    cur = conn.cursor()
    
    # Создаем таблицу users
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tg_id INTEGER UNIQUE,
            username TEXT,
            join_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            Opros TEXT DEFAULT NULL,
            q1 TEXT DEFAULT NULL,
            q2 TEXT DEFAULT NULL,
            q3 TEXT DEFAULT NULL,
            q4 TEXT DEFAULT NULL,
            q5 TEXT DEFAULT NULL,
            q6 TEXT DEFAULT NULL,
            q7 TEXT DEFAULT NULL,
            q8 TEXT DEFAULT NULL,
            q9 TEXT DEFAULT NULL,
            q10 TEXT DEFAULT NULL
        )
    """)
    
    conn.commit()
    conn.close()
    
    logging.info("Database initialized successfully")

async def set_user(user_id: int, username: str):
    """Добавление или обновление пользователя"""
    conn = get_db()
    cur = conn.cursor()
    
    try:
        # Создаем таблицу, если её нет
        cur.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                tg_id INTEGER UNIQUE,
                username TEXT,
                join_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # Проверяем существование пользователя
        cur.execute("SELECT * FROM users WHERE tg_id = ?", (user_id,))
        user = cur.fetchone()
        
        if not user:
            # Если пользователя нет, добавляем
            cur.execute(
                "INSERT INTO users (tg_id, username) VALUES (?, ?)",
                (user_id, username)
            )
            conn.commit()
            
    finally:
        conn.close()

async def db_start():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS users("
                "id INTEGER PRIMARY KEY AUTOINCREMENT, "
                "tg_id BIGINT, "
                "Date TEXT, "
                "Opros TEXT, "
                "username TEXT, "
                "q1 INTEGER, "
                "q2 INTEGER, "
                "q3 INTEGER, "
                "q4 INTEGER, "
                "Member INTEGER, "
                "q5 TEXT, "
                "Opros2 TEXT)")
    conn.commit()
    
    
async def get_users():
    conn = get_db()
    cur = conn.cursor()
    user = cur.execute("SELECT tg_id FROM users").fetchall()
    return user

async def get_ans1():
    conn = get_db()
    cur = conn.cursor()
    user = cur.execute("SELECT q5 FROM users").fetchall()
    return user

async def get_q(number, ans):
    conn = get_db()
    cur = conn.cursor()
    user = cur.execute("SELECT COUNT(q{number}) FROM users WHERE q{number} = {ans}".format(number=number, ans=ans)).fetchall()
    return user

async def set_opros(user_id: int, answer: str) -> Optional[bool]:
    """Сохраняет ответ пользователя на опрос"""
    conn = get_db()
    cur = conn.cursor()
    
    try:
        # Используем параметризованный запрос для безопасности
        query = "UPDATE users SET Opros = ? WHERE tg_id = ?"
        cur.execute(query, (answer, user_id))
        conn.commit()
        return True
    except Exception as e:
        print(f"Error in set_opros: {e}")
        return False
    finally:
        conn.close()

async def set_opros2(user_id, answer):
    conn = get_db()
    cur = conn.cursor()
    user = cur.execute("SELECT * FROM users WHERE tg_id == {key}".format(key=user_id)).fetchone()
    if user:
        cur.execute("UPDATE users SET Opros2 = '{key}' WHERE tg_id == {id}".format(key=answer, id=user_id))
    conn.commit()
    

async def set_q(user_id: int, number: int, answer: str) -> Optional[bool]:
    """Сохраняет ответ пользователя на вопрос"""
    if not isinstance(number, int) or not 1 <= number <= 10:
        return None
        
    conn = get_db()
    cur = conn.cursor()
    
    try:
        # Используем параметризованный запрос для безопасности
        query = f"UPDATE users SET q{number} = ? WHERE tg_id = ?"
        cur.execute(query, (answer, user_id))
        conn.commit()
        return True
    except Exception as e:
        print(f"Error in set_q: {e}")
        return False
    finally:
        conn.close()



async def set_leftmember(user_id):
    conn = get_db()
    cur = conn.cursor()
    user = cur.execute("SELECT * FROM users WHERE tg_id == {key}".format(key=user_id)).fetchone()
    if user:
        cur.execute("UPDATE users SET Member = 0 WHERE tg_id == {id}".format(id=user_id))
    conn.commit()
    
    
    
async def ban(user_id):
    conn = get_db()
    cur = conn.cursor()
    user = cur.execute("SELECT * FROM users WHERE tg_id == {key}".format(key=user_id)).fetchone()
    if user:
        cur.execute("UPDATE users SET Member = -1 WHERE tg_id == {id}".format(id=user_id))
    conn.commit()
    




async def get_opros(user_id):
    conn = get_db()
    cur = conn.cursor()
    user = cur.execute("SELECT Opros FROM users WHERE tg_id == '{key}'".format(key=user_id)).fetchone()
    return user

async def get_info_username(username):
    conn = get_db()
    cur = conn.cursor()
    user = cur.execute("SELECT * FROM users WHERE username == '{key}'".format(key=username)).fetchone()
    return user

async def get_info_all(id):
    conn = get_db()
    cur = conn.cursor()
    user = cur.execute("SELECT * FROM users WHERE id == '{key}'".format(key=id)).fetchone()
    if user:
        return user


async def get_info_id(id):
    conn = get_db()
    cur = conn.cursor()
    user = cur.execute("SELECT * FROM users WHERE tg_id == '{key}'".format(key=id)).fetchone()
    return user
    
    

# Создание таблицы users
async def init_models():
    conn = get_db()
    async with conn.begin() as conn:
        await conn.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                tg_id INTEGER UNIQUE,
                username TEXT,
                join_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                -- добавьте другие нужные поля
            );
        """)
    
    

def migrate_db():
    conn = get_db()
    cur = conn.cursor()
    
    try:
        # Проверяем существующие столбцы
        cur.execute("PRAGMA table_info(users)")
        existing_columns = [column[1] for column in cur.fetchall()]
        
        # Добавляем недостающие столбцы
        columns_to_add = ['Opros'] + [f'q{i}' for i in range(1, 11)]
        for column in columns_to_add:
            if column not in existing_columns:
                try:
                    cur.execute(f"ALTER TABLE users ADD COLUMN {column} TEXT DEFAULT NULL")
                    print(f"Added column {column}")
                except sqlite3.OperationalError as e:
                    if "duplicate column name" not in str(e):
                        print(f"Error adding column {column}: {e}")
    
        conn.commit()
    finally:
        conn.close()

# Вызовите эту функцию при запуске бота, если хотите сохранить данные
    
    

async def get_user_by_username(username: str) -> Optional[Tuple]:
    """
    Асинхронно получает информацию о пользователе по username
    """
    try:
        async with aiosqlite.connect('app/database/db.sqlite') as db:
            async with db.execute(
                "SELECT * FROM users WHERE username = ?", 
                (username,)
            ) as cursor:
                return await cursor.fetchone()
    except Exception as e:
        print(f"Error in get_user_by_username: {e}")
        return None
        
    

async def get_user_by_id(user_id: int) -> Optional[Tuple]:
    """
    Асинхронно получает информацию о пользователе по ID
    Args:
        user_id (int): Telegram ID пользователя
    Returns:
        Optional[Tuple]: данные пользователя или None если не найден
    """
    try:
        async with aiosqlite.connect('app/database/db.sqlite') as db:
            async with db.execute(
                "SELECT * FROM users WHERE tg_id = ?", 
                (user_id,)
            ) as cursor:
                return await cursor.fetchone()
    except Exception as e:
        print(f"Error in get_user_by_id: {e}")
        return None
        
    
