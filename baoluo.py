# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 14:26:57 2020

@author: Ray
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
rpath = r'C:\Users\Ray\Desktop\实验\数据\830mm弱轴-轴压比0.2(no)\final.xlsx'
wpath = r'C:\Users\Ray\Desktop\实验\数据\830mm弱轴-轴压比0.2(no)\baoluo.xlsx'
sta = pd.read_excel(rpath,sheet_name=0,header=None)
stan = sta.values 
maxd = 40
final = np.empty((maxd*2+1,2))
for i in range(-maxd-1,maxd+1,1):
#    print(i)
    for a in stan:
        if (a[0]>=i) and (a[0]<=i+1):            
#            print(a[1])
            final[i+maxd,0]=a[0]
            final[i+maxd,1]=a[1]
            break
final_final = []
for i in range(0,maxd*2-1,maxd):
    poly = np.polyfit(final[i:i+maxd,0],final[i:i+maxd,1],5)
    p = np.poly1d(poly)
    b = p(final[i:i+maxd,0])
    for c in b:
        final_final.append(c)
plt.title('baoluo')
plt.plot(final[0:maxd*2,0],final_final,color = 'r')
plt.plot(final[0:maxd*2,0],final[0:maxd*2,1],color  = 'b')
plt.show()
baoluo=np.vstack((final[0:maxd*2,0],final_final))
baoluo=baoluo.T
bl = pd.DataFrame(baoluo)
bl.columns=['D','F']
os.mknod(wpath)
bl.to_excel(wpath)
