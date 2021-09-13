import elektronik
from pprint import pprint

zapytanie = input("Podaj zapytanie: ")

# Wybierz konkretny dzień, godzina też może zostać wybrana
dni = ['hours', 'd1', 'd2']
pprint(elektronik.query(zapytanie, dni))

# Wybierz wszystko 
pprint(elektronik.query(zapytanie, "all"))

# Zwróc listę CTR + Listę Linków
pprint(elektronik.href_list())
pprint(elektronik.text_list())

pprint(elektronik.text2href(zapytanie))
