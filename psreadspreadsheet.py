import pyexcel

sheet = pyexcel.get_sheet(file_name='passwd.xlsx')
for row in sheet:
    print(row)