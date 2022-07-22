from collections import defaultdict


my_List = [(20, 30), (40, 50), (60,70), (80, 90)]
reg_dict= {}

reg_dict= defaultdict(list)
for key, value in my_List:
    reg_dict[key].append(value)

print(reg_dict)