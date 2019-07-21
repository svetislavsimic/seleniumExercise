import pandas as pd
from openpyxl import load_workbook
import os
currentFolderPath = os.getcwd()
filePath = os.path.join(currentFolderPath, "data", "testPandas.xlsx")
book = load_workbook(filePath)
writer = pd.ExcelWriter(filePath, engine='openpyxl', mode='a')
writer.book = book
writer.sheets = dict((ws.title, ws) for ws in book.worksheets)
df = pd.DataFrame({'PITANJE5': [1, 3, 5, 7, 4, 5, 6, 4, 7, 8, 9],
                   'PITANJE6': [3, 5, 6, 2, 4, 6, 7, 8, 7, 8, 9]})
df.to_excel(writer, "log_in", columns=['PITANJE5', 'PITANJE6'])
writer.save()