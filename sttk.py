import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



data=pd.read_excel('student-mat.xlsx')

mean_value=data['absences'].mean() #srednja vrijednost
print("Srednja vrijednosti prije:", mean_value)

standard_deviation=data['absences'].std() #standardna devijacija
print("Standardna devijacija prije:", standard_deviation)

variance=data.var()['absences'] #varijansa
print("Varijansa prije:", variance)

data=data.drop(data[data.absences>mean_value+standard_deviation].index) #izbacivanje vrijednosti izvan standardne devijacije

data = data.fillna(data.mode().iloc[0]) #popunjavanje najcescom vrijednoscu broja izostanaka

mean_value_post=data['absences'].mean() #srednja vrijednost nakon pripreme podataka
print("Srednja vrijednosti poslije:", mean_value_post)

standard_deviation_post=data['absences'].std() #standardna devijacija nakon pripreme podataka
print("Standardna devijacija poslije:", standard_deviation_post)

variance_post=data.var()['absences']  #varijansa nakon pripreme podataka
print("Varijansa poslije:", variance_post)

data["Ocjena_10"] = np.where(data['G3']>= 16,"Dobio/la deset","Nije dobio/la deset")
print(data.head(10))


data["Mnogo_izostanaka"] = np.where(data['absences']>=10,"Mnogo izostanaka","Malo izostanaka")
print(data.head(10))

plt.hist(data['Ocjena_10'])
plt.grid()
plt.title('Histogram')
plt.ylabel('Broj studenata')



data['brojac'] = 1
print(data.head(10))

data = data[['Ocjena_10','Mnogo_izostanaka','brojac']]


tabela = pd.pivot_table(
      data,
      values='brojac',
      index=['Ocjena_10'],
      columns=['Mnogo_izostanaka'],
      aggfunc=np.size,
      )



P_A = (35 + 3) / (276+32+35+3) 
print("Vjerovatnoća da su studenti dobili desetku:",P_A)
P_B = (32 + 3) / (276+32+35+3)
print("Vjerovatnoća da su studenti napravili deset ili više izostanaka:",P_B)
P_AB = 3/(276+32+35+3) #vjerovatnoca da je dobijena desetka i napravljeno vise od 10 izostanaka 
print("Vjerovatnoća da su studenti dobili desetku i napravili više od deset izostanaka:",P_AB)
P_A_B = P_AB / P_B   #uslovna vjerovatnoca
print("Uslovna vjerovatnoća:",P_A_B)
