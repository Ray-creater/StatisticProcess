import hysteresis as hy


component=hy.CurrentComponent(r'C:\Users\Ray\Desktop\W-23.dat',r'C:\Users\Ray\Desktop\W-23.log')
component.readData()

import matplotlib.pyplot as plt
import pandas as pd  

data=pd.read_excel(r'C:\Users\Ray\Desktop\20201127.xlsx')
for i in range(1,21):
    fig,axe=plt.subplots(1,2)
    strain=data.iloc[1:,i]
    axe[0].plot(component.OriginalData['Disp'][1:25000],strain[1:25000])
    axe[0].set_title(str(i+2)+'   round')
    axe[1].plot(component.OriginalData["Disp"][17000:19000],component.OriginalData["Force"][17000:19000],color='red')
    axe[1].plot(component.OriginalData['Disp'],component.OriginalData['Force'])
    axe[1].set_title(str(i+2)+'   round')
    plt.show()