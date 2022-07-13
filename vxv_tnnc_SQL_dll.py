'''
Подключаемся к DLL Константина для отправки данный на MS SQL 2017 server
'''
import clr
import os

def SendText(text):
    '''Поместим библиотеку “TNNC_SQL_transferer.dll” и "tnnc_oapr_stat.ini" в папку с проектом:'''
    '''Укажем путь до нашего .dll файла:'''
    pathDLL = os.getcwd() + "\\TNNC_SQL_transferer.dll"

    '''Чтобы подгрузить нужную нам библиотеку необходимо прописать следующий код:'''
    clr.AddReference(pathDLL)

    '''После чего можно импортировать модуль и всё, что в нем содержится.'''
    import TNNC_SQL_transferer

    try:
        '''Отправляем тескт названия программы'''
        TNNC_SQL_transferer.TNNC_SQL().SendStatMessage(text)
        print(f'Оправка записи на SQL: "{text}"')
    except:
        print('Ошибка оправки записи на SQL')

if __name__ == "__main__":
    text = "Пробный текст . . ."
    SendText(text)
