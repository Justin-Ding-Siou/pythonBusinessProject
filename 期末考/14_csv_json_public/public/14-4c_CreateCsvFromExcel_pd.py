import pandas as pd
import os

xlfname = 'example.xlsx'
fname, ext = os.path.splitext(xlfname) 
xl = pd.ExcelFile(xlfname)
 
for sheet in xl.sheet_names:
    print(sheet)
    df = xl.parse(sheet)
    #df = pd.read_excel(xlfname, sheet)
    csvfname = fname + '_'  + sheet + '.csv'
    df.to_csv(csvfname, encoding='utf-8', index=False)