import csv

#leer un archivo csv
with open ('C:/Users/A200214978/OneDrive - Deutsche Telekom AG/Dokumente/Python/Programa especializado Aprende a programar con Python/2. Estructuras de datos en Python/Modulo 2/csv_example.csv','r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(', '.join(row))

#escribir un arvhivo csv
with open ('C:/Users/A200214978/OneDrive - Deutsche Telekom AG/Dokumente/Python/Programa especializado Aprende a programar con Python/2. Estructuras de datos en Python/Modulo 2/csv_example.csv','a') as csvfile:
    writer=csv.writer(csvfile)
    writer.writerow(['Perrdro','gontr','2321r4214','pgmaincrar@gail.com'])