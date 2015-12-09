import openpyxl
countrys = {}
wb = openpyxl.load_workbook('total.xlsx')
column = ['E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P']
sheet = wb.get_sheet_by_name('Sheet1')
for i in range(32,93):
    country = sheet['A'+str(i)].value.strip()
    year = 2002
    countrys[country] = {}
    for j in range(12):
        countrys[country][year] = sheet[column[j]+str(i)].value
        year += 1
print(countrys)
