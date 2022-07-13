'''Модуль прорисовки таблицы и вставки в NanoCad'''

import win32com.client
from pythoncom import VT_ARRAY, VT_R8
from PyQt5 import QtCore
from okno_general import ui

def write():
    def CC(*args):
        '''    Функция преобразования координат в формат AutoCAD
        :param args: координаты для преобразования, допустима передача списка или кортежа
        :return: Координаты в формате AutoCAD    '''
        if isinstance(args[0], (list, tuple)):
            coords = [item for item in args[0]]
        else:
            coords = args
        return win32com.client.VARIANT(VT_ARRAY | VT_R8, coords)
    '''Подключаемся к AutoCad'''
    # acad = win32com.client.Dispatch("AutoCAD.Application")
    acad = win32com.client.Dispatch("NanoCAD.Application")
    '''Выполняем вход в пространство модели активной вкладке (документу) AutoCad'''
    doc = acad.ActiveDocument
    msp = doc.ModelSpace
    '''Регенерация пространства модели'''
    doc.Regen(1)

    '''Число строк и столбцов в таблице'''
    row_count = 3
    WidthCol = [1500, 8000, 3000, 3000]
    column_count = len(WidthCol)

    try: point = doc.Utility.GetPoint(CC(0, 0, 0), "Укажите точку вставки геол. разреза:")
    except: return

    '''# масштаб листа'''
    scale = 100
    tab_point_X = point[0] - 0 * scale
    tab_point_Y = point[1] - 0 * scale
    insertion_point = (tab_point_X, tab_point_Y, 0)
    # insertion_point = (0, 0, 0)

    '''Вставляем таблицу в верхний правый угол Формата листа'''
    table = msp.AddTable(CC(insertion_point), row_count, column_count, 8 * scale, 1 * scale)
    for i in range(0, len(WidthCol)):
        table.SetColumnWidth(i, WidthCol[i])

    '''Задание высоты строк: Название, Заголовок'''
    table.SetRowHeight(0, 1200)
    table.SetTextHeight(0, 500)

    table.SetRowHeight(1, 800)
    table.SetTextHeight(1, 250)
    table.SetRowHeight(2, 800)
    table.SetTextHeight(2, 250)
    
    '''Объединяем ячейки (разъединение ячеек = UnmergeCells) '''
    table.MergeCells(minRow=1, maxRow=2, minCol=0, maxCol=0)
    table.MergeCells(minRow=1, maxRow=2, minCol=1, maxCol=1)
    table.MergeCells(minRow=1, maxRow=1, minCol=2, maxCol=3)
    # print(dir(table))

    '''Отступ по горизонтали в ячейке'''
    table.HorzCellMargin = 150

    def tab_nazv(row, list):
        for i in range(0, len(list)):
            table.SetText(row, i, list[i])

    NazvTab = ['ДАННЫЕ СТАТИЧЕСКОГО ЗОНДИРОВАНИЯ}', '', '', '']
    ZagolovokTab_1 = ['ИГЭ', 'Наименование', 'Среднее значение по слою', '']
    ZagolovokTab_2 = ['', '', '\\A1;q{\\H0.7x;\\S^с ср.;\\H1.4286x;, МПа}', '\\A1;f{\\H0.7x;\\S^з ср.;}, кПа']

    tab_nazv(0, NazvTab)
    tab_nazv(1, ZagolovokTab_1)
    tab_nazv(2, ZagolovokTab_2)

    '''Проверка стиля ячейки: table.GetCellStyle(0, 0)'''
    '''Устанавливаем стиль ячейки и строки (Название и Заголовок) _TITLE, _HEADER, _DATA'''
    table.SetCellStyle(0, 0, '_TITLE')
    for i in range(4):
        table.SetCellStyle(2, i, '_HEADER')

    '''Заполняем строчку в таблицы'''
    def tab_text(list):
        '''Узнаем текущее количество строк в таблице'''
        rowX = table.Rows
        '''Добавляем строчку в таблицу'''
        table.InsertRows(rowX, Height = 8 * scale, Rows = 1)
        '''Для каждой колонки от 0 до 4:'''
        for i in range(4):
            '''Вносим тескт из списка в ячеки строки'''
            table.SetText(rowX, i, list[i])
            '''Устанавливаем стиль ячейки и строки (Данные) _TITLE, _HEADER, _DATA'''
            table.SetCellStyle(rowX, i, '_DATA')
            # '''Выравнивание значения колонки "Наименование" по левому краю (Строчка, столбец, индекс выравнивания)'''
            # table.SetCellAlignment (rowX, 2, 4)

    '''Сбор данных из таблица "Характеристики грунтов" из Statzond'''
    dataList = []
    for x in range(0, 20):
        dataListRow = []
        for y in range(3):
            xxx = ui.tableWidget.item(x, y).text()
            if ui.tableWidget.item(x, 0).text() != '':
                dataListRow.append(xxx)
                if y == 0:
                    dataListRow.append('')
        if len(dataListRow) != 0: 
            dataList.append(dataListRow)
    print('dataList = ', dataList)

    '''Дорисовываем таблицу в NanoCad'''
    for x in range(len(dataList)):
        tab_text(dataList[x])

if __name__ == "__main__":
    write()





