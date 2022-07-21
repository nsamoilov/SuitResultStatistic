import sqlite3

dbname = 'CovidStatisticDB.sqlite3'
tablename = 'RawInfectStat'
sqlconn = sqlite3.connect(dbname)

cursor = sqlconn.cursor()
sqlite_select_query = f"SELECT * from {tablename}"
cursor.execute(sqlite_select_query)
records = cursor.fetchall()
print("Всего строк:  ", len(records))
print("Вывод каждой строки:")
for row in records:
    print("Страна:", row[0])
    print("Дата:", row[1])
    print("Количество случаев:", row[2])
cursor.close()
