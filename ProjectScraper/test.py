txt = ("Auckland Print Shop, 98-102 Albert Street Auckalnd +64 (09) 281 5101")


i, phone = txt.split('+', 1)
name, address = i.split(',',1)
print(name)
print(address)
print(phone)
