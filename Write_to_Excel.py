import xlwings as xw
from Get_Differences import * #Run all, get differences list
from Dictionaries import excel_columns

wb = xw.Book(r"C:\Users\CCrowe\Documents\Traffic\Cube\Compare_CSV\Compare_CSVs\Differences.xlsx")
ws_counts = wb.sheets["Counts"]
ws_speeds = wb.sheets["Speeds"]

counts = [x for x in differences if x.type is 'V']
speeds = [x for x in differences if x.type is 'S']

counts.sort(key=lambda x: x.A,reverse = True)
counts.sort(key=lambda x: x.time,reverse = True)

def GetKey(count):
    return count.A + "-" + count.B

def GetA_B_Sets(counts):
    s = set()
    for x in counts:
        key = GetKey(x)
        s.add(key)
    return list(s)

def WriteToExcel(sheet,l):
    rows = GetA_B_Sets(l)
    row_dict = {}
    excel_cnt = 2
    for row in rows:
        spl = row.split("-")
        a = spl[0]
        b = spl[1]
        sheet.range("A" + str(excel_cnt)).value = a
        sheet.range("A" + str(excel_cnt)).value = b
        row_dict[row] = excel_cnt
        excel_cnt += 1
    for count in l:
        key = GetKey(count)
        row = row_dict[key]
        if not count.time in excel_columns:
            raise Exception("Problem finding time within excel_counts: " + counts.time)
        column = int(excel_columns[count.time])
        sheet.range((row,column)).value = count.difference

WriteToExcel(ws_counts,counts)
WriteToExcel(ws_speeds,speeds)

wb.save()
wb.close()
