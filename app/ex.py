import openpyxl
import app.database.requests as rq
import asyncio
from functools import partial
import logging

logger = logging.getLogger(__name__)

async def st():
    try:
        # Получаем список пользователей
        users = await rq.get_users()
        users_count = len(users)
        
        # Получаем данные всех пользователей
        all_data = []
        for i in range(users_count):
            data = await rq.get_info_all(i + 1)
            all_data.append(data)
        
        # Обрабатываем Excel в отдельном потоке
        loop = asyncio.get_running_loop()
        await loop.run_in_executor(
            None, 
            partial(process_excel_data, users_count, all_data)
        )
        
    except Exception as e:
        logger.error(f"Error in st function: {e}")
        raise

def process_excel_data(users_count, all_data):
    """Синхронная функция для работы с Excel"""
    try:
        book = openpyxl.open("data.xlsx")
        sheet = book.active

        # Удаляем старые строки
        for i in range(users_count):
            sheet.delete_rows(i + 2, 1)

        # Обрабатываем данные
        for i, data in enumerate(all_data):
            p = i + 2
            q5 = data[10]
            prg1 = 0
            s = ''
            if q5 is not None:
                
                for j in q5:
                    if j == '7' or q5 == 'Не проходил':
                        break 
                    prg1 += 1

                for b in q5:
                    if q5 == 'Не проходил':
                        s = '----------'
                        break
                    if b == '7':
                        s += '-'
                    else:
                        s += str(int(b) + 1)
            else:
                s = '----------'
            prg2 = 0
            q1 = data[5]
            q2 = data[6]
            q3 = data[7]
            if q1 is None:
                q1 = -1
            if q2 is None:
                q2 = -1
            if q3 is None:
                q3 = -1
            if q1 == -1:
                prg2 = 0
            elif q2 == -1:
                prg2 = 1
            elif q3 == -1:
                prg2 = 2
            else:
                prg2 = 3
                
            sheet[p][0].value = data[1]
            sheet[p][1].value = data[4]
            if prg1 == 7:
                sheet[p][3].value = 'Прошел'
            else:
                sheet[p][3].value = 'На ' + str(prg1) + 'ом вопросе'
            if prg2 == 3:
                sheet[p][2].value = 'Прошел'
            else:
                sheet[p][2].value = 'На ' + str(prg2) + 'ом вопросе'
            sheet[p][4].value = s[0] 
            sheet[p][5].value = s[1] 
            sheet[p][6].value = s[2] 
            sheet[p][7].value = s[3]
            sheet[p][8].value = s[4]
            sheet[p][9].value = s[5]
            sheet[p][10].value = s[6]
            sheet[p][11].value = s[7]
            sheet[p][12].value = s[8]
            sheet[p][13].value = s[9]
            sheet[p][14].value = q1 + 1
            sheet[p][15].value = q2 + 1
            sheet[p][16].value = q3 + 1

        book.save("data.xlsx")
        book.close()
        
    except Exception as e:
        logger.error(f"Error processing Excel: {e}")
        raise