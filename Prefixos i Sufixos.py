from fileinput import filename
import os
from re import sub

arxiu = 0

filepath = input("Ruta: ")
if os.path.isdir(filepath) == False:
    print("El directori no existeix!")
tipus = input("Tipus(Prefix o Sufix): ")
while tipus != "Prefix" and tipus != "Sufix":
    print("No t'entenc, comprova si ho has escrit bé.")
    tipus = input("Tipus(Prefix o Sufix): ")
if tipus == "Prefix":
    text = input("Prefix: ")
else:
    text = input("Sufix: ")
filenames = os.listdir(filepath)

for fn in filenames:
    if tipus == "Sufix":
        if "." in fn and fn[0] != ".":
            arxiu = 1
            exten = fn[(fn.index(".")):]
            suf_fn = fn.replace(exten, "")
        else:
            arxiu = 0
    for i in range(len(text)):
        if tipus == "Prefix":
            if fn[i] == text[i]:
                if i == (len(text)-1):
                    ruta_antiga = os.path.join(filepath, fn)
                    nounom = fn.replace(text, "")
                    ruta_nova = os.path.join(filepath, nounom)
                    os.rename(ruta_antiga, ruta_nova)
        elif arxiu == 1:
            if suf_fn[-i] == text[-i]:
                if i == (len(text)-1):
                    ruta_antiga = os.path.join(filepath, fn)
                    nounom = fn.replace(text, "")
                    ruta_nova = os.path.join(filepath, nounom)
                    os.rename(ruta_antiga, ruta_nova)

print("Noms canviats correctament!")
