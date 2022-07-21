from itertools import groupby, accumulate
from deep_translator import MyMemoryTranslator
import plotly.graph_objs as go
import plotly
import matplotlib.pyplot as plt                                                                             
import squarify    
import warnings
warnings.filterwarnings("ignore")

class CountryStatistick():
    def __init__(self, countryName, date, cases):
        self.CountryName = countryName
        self.Date = date
        self.Cases = cases
    
    def __str__(self):
        return f"{self.CountryName};{self.Date};{self.Cases}"

def GetCovidStatisticListFromSQLite(dbname, tablename):
    sqlconn = sqlite3.connect(dbname)
    #cs - Covid Statistic
    cursor = sqlconn.cursor()
    sqlite_select_query = f"SELECT * from {tablename}"
    cursor.execute(sqlite_select_query)
    csdatarows = cursor.fetchall()

    cslist = list()
    for csrow in csdatarows:
        csclass = CountryStatistick(str(csrow[0]), str(csrow[1]), int(csrow[2]))
        cslist.append(csclass)
    return cslist

dbname = 'CovidStatisticDB.sqlite3'        
tablename = 'RawInfectStat'
cslist = GetCovidStatisticListFromSQLite(dbname, tablename)

groups_data = groupby(cslist, lambda x: x.CountryName)

coutries = list()
cases = list()
for key, group in groups_data:
    cases_data = 0
    for csclass in group:
        cases_data += csclass.Cases
    coutries.append(key)
    cases.append(cases_data)
                                                           
countries_data = list()                                                                                     
for counrtyName in coutries:
    translated_word = MyMemoryTranslator(source='english', target='russian').translate(counrtyName)
    countries_data.append(translated_word)

'''
#древовидная карта
colors = [plt.cm.Spectral(i/float(len(countries_data))) for i in range(len(countries_data))]                

plt.figure(figsize=(12,8), dpi= 80)
squarify.plot(sizes=cases, label=countries_data, color=colors, alpha=.8)
plt.title('Количество заболевших по странам')
plt.axis('off')
plt.show()
'''  
#круговая диаграмма
fig = go.Figure()                                                                                         #Отрисовка графика
fig.add_trace(go.Pie(values=cases, labels=countries_data))
#fig.show()
plotly.offline.plot(fig,filename='positives.html',config={'displayModeBar': False})
'''
#Гистограмма
plt.figure(figsize=(16,10), dpi= 80)                                                                                #Формирование графика
plt.bar(countries_data, cases, color=colors, width=.5)
for i, val in enumerate(groups_data):                                                                         #Цикл для элементов графика
    plt.text(i, val, val, horizontalalignment='center', 
             verticalalignment='bottom', fontdict={'fontweight':50, 'size':16})

plt.gca().set_xticklabels(countries_data, rotation=60,fontdict={'fontsize': 16}, horizontalalignment= 'right')      #Декорирование графика
plt.title('Количество заболевших по странам', fontsize=22)
plt.ylabel('Количество случаев')
plt.show() 
'''   
