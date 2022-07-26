from collections import namedtuple


Parts={'id_num':'1234', 'desc':'Ford Engine', 'cost':1200, 'amount':10}
parts = namedtuple('Parts', Parts.keys())(**Parts)
print(parts) 