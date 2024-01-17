
string = "3,9,13,44,2"

#Razdvajanje elemenata stringa koristeci zarez kao separator
Podela = string.split(",")

#Pretvaranje elemenata stringa u broj(int), kvadratiranje i kreiranje liste
Lista_kvadrata = [int(num)**2 for num in Podela]
print(Lista_kvadrata)
print(type(Lista_kvadrata))

#Pretvaranje elemenata liste u novi string koristeci zarez kao separator
string_end = ",".join(map(str, Lista_kvadrata))

print(string_end)
print(type(string_end))