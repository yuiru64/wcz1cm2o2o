import xlrd
import os
import re

os.chdir(os.path.dirname(__file__))

# since 2000
data = """
Monaco  100
Maldives    100
Tuvalu  100
Marshall    99.02
Kiribati    96.67
Bahamas 71.99
Netherlands 58.47
""".strip()

_items = re.split(r"\r?\n", data)
_dict = {}
for _i in _items:
    _tokens = re.split(r"\s+", _i)
    _dict[_tokens[0]] = float(_tokens[1])

def getData():
    return _dict

if __name__ == "__main__":
    print(getData())