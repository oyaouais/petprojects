from hashlib import sha256
import requests
import os

def get(namestring, classnumber):
    hash = sha256(namestring.encode()).hexdigest()

    url = f"https://diploma.rsr-olymp.ru/files/rsosh-diplomas-static/compiled-storage-2023/by-person-released/{hash}/codes.js"
    r = requests.get(url).text
    r2 = r.split("{")[1:]
    r = r.split()
    codes = []
    names = []
    for i in range(0, len(r)):
        if (r[i] == 'code:'):
            codes.append(r[i + 1][:-1])
    for i in r2:
        s = i.split(":")
        name = s[2][8:-8]
        while "," in name:
            name = name.replace(",", " ")
        while "." in name:
            name = name.replace(".", " ")
        while "\"" in name:
            name = name.replace("\"", " ")
        names.append(name)

    print(len(names), len(codes))
    for i in range(len(codes)):
        c = codes[i]
        name = names[i]
        download_url = f"https://diploma.rsr-olymp.ru/files/rsosh-diplomas-static/compiled-storage-2023/by-code/{c}/color.pdf"
        try:
            os.mkdir(f"C:\\дипломы\\{classnumber}")
        except: pass
        try:
            os.mkdir(f"C:\\дипломы\\{classnumber}\\{namestring}")
        except: pass
        pdf = open(f"C:\\дипломы\\{classnumber}\\{namestring}\\{name}.pdf", 'wb')
        pdf.write(requests.get(download_url).content)
        pdf.close()

import csv


with open("students.csv", "r", encoding="utf-8") as file:
    csvreader = csv.reader(file)

    for row in csvreader:
        name = row[1].strip()
        date = row[2].split(".")
        date.reverse()
        date = "-".join(date)
        namestring = name + " " + date

        get(namestring, row[0])
        print(namestring, row[0])
