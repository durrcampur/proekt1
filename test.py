alfavit_EU =  'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
alfavit_RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
choose = int(input("1 = дешифровка 0 = шифровка:"))
smeshenie = int(input('Шаг шифровки: '))
message = input("Сообщение для шифровки: ").upper()
itog = ''
if choose == 1:
    for i in message:
        mesto = alfavit_RU.find(i)
        new_mesto = mesto - smeshenie
    if i in alfavit_RU:
        itog += alfavit_RU[new_mesto]
    else:
        itog += i
else:
    for i in message:
        mesto = alfavit_RU.find(i)
        new_mesto = mesto + smeshenie
    if i in alfavit_RU:
        itog += alfavit_RU[new_mesto]
    else:
        itog += i
print (itog)



