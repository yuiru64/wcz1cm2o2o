import xlrd
import os

_path = os.path.realpath(os.getcwd())
os.chdir(os.path.dirname(__file__))

_data = "0.04 0.11 0.24 0.41 0.63 0.90 1.2 1.6 2.0 2.5 3.6 5.5 9.7"
_level = _data.split(" ")
_level = [float(_i) for _i in _level]

def getLevel(year):
    if year < 2010:
        raise Exception("year should >= 2010")
    return _level[(year - 2010) // 10]\
    + _level[(year - 2010) // 10]\
    + (year - 2010) % 10 / 10 * (_level[(year - 2010) // 10 + 1] - _level[(year - 2010) // 10])

if __name__ == "__main__":
    print(getLevel(2012))

os.chdir(_path)