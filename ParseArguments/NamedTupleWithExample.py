from cmath import cos
from collections import namedtuple


Parts = namedtuple('Parts', 'id_num desc cost amount')
auto_parts = Parts(id_num='1234', desc='Ford Engine', cost=1200, amount=10)
print(auto_parts.id_num)