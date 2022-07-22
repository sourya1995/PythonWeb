my_List = [(20, 30), (40, 50), (60,70), (80, 90)]
reg_dict= {}
for key, value in my_List:
    if key in reg_dict:
        reg_dict[key].append(value)
    else:
        reg_dict[key] = value

print(reg_dict)