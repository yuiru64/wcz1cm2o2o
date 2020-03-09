import xlrd
import os

os.chdir(os.path.dirname(__file__))

def fromCountries(_list: list) -> dict:
    table = xlrd.open_workbook("Countries of the world.xls")
    sheet: xlrd.sheet.Sheet = table.sheet_by_index(0)
    ret = {}
    count = {}
    for i in range(5, sheet.nrows):
        key = sheet.cell_value(i, 0).strip()
        if key is None:
            break
        flag = False
        for it in _list:
            if it in key:
                flag = True
                key = it
                break
        if flag:
            if key not in ret:
                ret[key] = {
                    "population": sheet.cell_value(i, 2),   # population
                    "area": sheet.cell_value(i, 3)    # area
                }
                count[key] = 1
            else:
                ret[key] = {
                    "population": ret[key]["population"] + sheet.cell_value(i, 2),   # population
                    "area": ret[key]["area"] + sheet.cell_value(i, 3)    # area
                }
                count[key] += 1
    for key in ret:
        ret[key]["population"] /= count[key]
        ret[key]["area"] /= count[key]
    return ret

if __name__ == "__main__":
    ret = fromCountries([
        "Tuvalu", "Nauru", "Palau"
    ])
    print(ret)
