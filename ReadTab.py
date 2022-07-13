'''Модуль чтения таблицы из NanoCada'''

def Read():
    import win32com.client
    '''Подключаемся к AutoCad'''
    # acad = win32com.client.Dispatch("AutoCAD.Application")
    acad = win32com.client.Dispatch("NanoCAD.Application")
    '''Выполняем вход в пространство модели активной вкладке (документу) AutoCad'''
    doc = acad.ActiveDocument
    # mSp = doc.ModelSpace
    '''Регенерация пространства модели'''
    doc.Regen(1)

    '''Удаляем набор выбора, если он есть'''
    try:
        doc.SelectionSets.Item("SS1").Delete()
    except:
        print('Не удалось удалить набор выбора SS1') 
    '''Создайте набор выбора с именем SS1'''
    slt = doc.SelectionSets.Add("SS1")

    '''Выбор объектов в ручную'''
    slt.SelectOnScreen()

    '''Ищем выноски в наборе'''
    for object in slt:
        name = object.objectName
        table = object
        if name == 'AcDbTable':
            '''Узнаем текущее количество строк в таблице'''
            Rows = table.Rows
            '''Узнаем текущее количество колонн в таблице'''
            Columns = table.Columns
            '''Сбор данных со всей таблицы'''
            def TablDataList():
                TabData = []
                for i in range(0, Rows):
                    RowData = []
                    for x in range(0, Columns):
                        RowData.append(table.GetCellValue(i, x))
                        # RowData.append(table.GetCellStyle(i, x))
                    TabData.append(RowData)
                return TabData
            TabData = TablDataList()
        else:
            print('Таблица не выбрана, попробуйте еще раз!!!')
    return TabData

if __name__ == "__main__":
    TabData = Read()
    print('TabData = ', TabData)

