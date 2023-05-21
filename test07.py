from xlrd import open_workbook

book = open_workbook('Dio_Result.xlsx',on_demand=True)
for name in book.sheet_names():
    if name.endswith('2'):
        sheet = book.sheet_by_name(name)

        # Attempt to find a matching row (search the first column for 'john')
        rowIndex = -1
        for cell in sheet.col(0): # 
            if 'john' in cell.value:
                break

        # If we found the row, print it
        if row != -1:
            cells = sheet.row(row)
            for cell in cells:
                print (cell.value)

        book.unload_sheet(name) 