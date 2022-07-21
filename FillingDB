import sqlite3
import csv
tablename = 'RawInfectStat'
dbname = 'CovidStatisticDB.sqlite3'

sqlconn = sqlite3.connect(dbname)
cursor = sqlconn.cursor()
with open('/Users/nsamoilove/Desktop/coronavirus_dataset4.csv', newline='') as File:  
    reader = csv.reader(File)
    firststr = True
    for row in reader:
        if firststr == True:
            firststr = False
            continue
        insertcmd = f"""INSERT INTO {tablename} (CountryName, Date, Cases)
                        VALUES ('{str(row[1])}', '{str(row[4])}', {int(row[5])});"""
        #print(insertcmd)
        cursor.execute(insertcmd)
        #print('Insert completed!')
sqlconn.commit()
cursor.close()
