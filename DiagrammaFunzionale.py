#Il codice serve per generare il diagramma funzionale
#divide le variabili da quelle con il Rec State
#mette in ordine alfabetico le variabili che devono essere inserite nella CFTS
import pandas as pd


df_sheet_index = pd.read_excel('C:\\Users\\Kineton\\Fabio\\Controls\\VF_382_TCS\\APPLBEV_EVCU2_InterfacceCFTS_LP3_13_03_2023_2.xlsx', sheet_name=4)


print(df_sheet_index.get(["Module Variable Name"]))
file = open("DiagrammaFunzionale.txt", "r", encoding="utf-8")

lista_var = []
lista_rec = []
lista_nomi_CFTS = []

key_word = "_RecSt"
key_char = "_"
a = 0
b = 0
c = 0
d = 0 
e = 0

for line in file:
    c = c+1
    if key_word in line:
        if line not in lista_rec:
            lista_rec.append(line)
            lista_rec.sort()
            a = a+1
    elif line not in lista_var:
            lista_var.append(line)
            lista_var.sort()
            b = b+1
    e = e+1
    if "RecSt" in line:
        line = line.replace("RecSt", "Diagnosis State")
        if key_char in line:
            line = line.replace(key_char, " ")
            lista_nomi_CFTS.append(line)
            lista_nomi_CFTS.sort()
            d = d+1
    elif key_char in line:
        line = line.replace(key_char, " ")
        lista_nomi_CFTS.append(line)
        lista_nomi_CFTS.sort()
        d = d+1
    else:
        lista_nomi_CFTS.append(line)
        lista_nomi_CFTS.sort()
        d = d+1

file.close()
file = open("DiagrammaFunzionale.txt", "r", encoding="utf-8")

# insieme delle variabili di EXCEL (nomi Doors grezzi che vanno mainpolati) --> INPUT 
dict_nomi_file = {}
lista_nomi_file_temp = [] #chiavi messe in ordine alfabetico

for line in file:
    dict_nomi_file[line] = {"name":line}# dizionario[chiave]={"campo1":campo1,"campo2":campo2,"campo3":campo3...}
lista_nomi_file_temp = dict_nomi_file.keys()
lista_temp = []
for l in lista_nomi_file_temp:
    lista_temp.append(l.upper())
lista_nomi_file_final = []
for key_up in sorted(lista_temp):
    for key in lista_nomi_file_temp:
        if key.upper() == key_up:
            lista_nomi_file_final.append(dict_nomi_file.get(key)["name"])

#variabili che vanno in CFTS (nomi Doors manipolati che vanno messi nello stesso ordine alfabetico di quelli Doors) --> OUTPUT
dict_nomi_CFTS = {}
lista_nomi_CFTS_temp = []

for linea in lista_nomi_CFTS:
    dict_nomi_CFTS[linea] = {"name":linea}
lista_nomi_CFTS_temp = dict_nomi_CFTS.keys()
lista_temp = []
for l in lista_nomi_CFTS_temp:
    lista_temp.append(l.upper())
lista_nomi_CFTS_final = []
for key_up in sorted(lista_temp):
    for key in lista_nomi_CFTS_temp:
        if key.upper() == key_up:
            lista_nomi_CFTS_final.append(dict_nomi_CFTS.get(key)["name"])

            
file.close()
for var in lista_nomi_CFTS_final:
    if var.endswith("\n"):
        print(var.replace("\n", ""))