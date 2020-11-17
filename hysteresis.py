import os
import matplotlib.pyplot as plt
import numpy as np 

class CurrentComponent():

    def __init__(self,pathofdat,pathoflog):
        self.pathofdat=pathofdat
        self.pathoflog=pathoflog


    def fitcurveForOneLoop(self,indexGroup:int,degree:int):
        groupData=self.dispart(indexGroup)
        polyCoeff=np.polyfit(groupData['Disp'],groupData['Force'],degree)
        polyNominal=np.poly1d(polyCoeff)
        fitY=[]
        for i in groupData['Disp']:
            fitY.append(polyNominal(i))
        return {'Disp':groupData['Disp'],'Force':fitY}


    def readData(self):
        ###input path of dat file and log file,get TimeStop, TimeIndex corresponds to (Disp,Force) and Disp Force
        with open(self.pathofdat,'r',encoding='gbk') as f:
            Data=f.readlines()
        with open(self.pathoflog,'r',encoding='gbk') as f:
            TimeLimit=f.readlines()
        UsefulData=Data[12:-1]
        TimeIndex,Disp,Force,TimeStop=[],[],[],[]
        for i in UsefulData:
            LineList=i.split()
            TimeIndex.append(float(LineList[1]))
            Disp.append(float(LineList[3]))
            Force.append(float(LineList[2]))
        for j in TimeLimit[1:-1]:
            j=j.split('=')[1].split()[0].replace('ms','')
            TimeStop.append(float(j))
        self.timeStop,self.timeIndex,self.originalData=TimeStop,TimeIndex,{'Disp':Disp,'Force':Force}

    def readTimeChangeIndex(self):
        ###through TimeStop(ChangePoints) find change Valve to dispart the curve, ouput Time change index
        self.timeChangeIndex=[]
        for i in self.timeStop:
            index,gap=0,100000000
            for j,k in enumerate(self.timeIndex):
                if abs(i-k)<gap:
                    gap=abs(i-k)
                    index=j
            self.timeChangeIndex.append(index)
        self.timeChangeIndex.pop()
        self.timeChangeIndex.pop(0)
        self.timeChangeIndex.pop(0)
        return self.timeChangeIndex

    def dispart(self,i:int):
        #data[1]:TimeIndex, data[2]:Disp,data[3]:Force             self.timeChangeIndex
        ###for example self.timeChangeIndex=[1,5,9]  there is two group of data, first group contain data[1:5] second group contain data[5:9]
        self.readData()
        self.readTimeChangeIndex()
        dispartTimeIndex=self.timeIndex[self.timeChangeIndex[i-1]:self.timeChangeIndex[i]]
        dispartDisp=self.originalData['Disp'][self.timeChangeIndex[i-1]:self.timeChangeIndex[i]]
        dispartForce=self.originalData['Force'][self.timeChangeIndex[i-1]:self.timeChangeIndex[i]] 
        return {'Time':dispartTimeIndex,'Disp':dispartDisp,'Force':dispartForce}

        
    def modifiedCurve(self):
        ### output fitedCurve using dictionary and keys are 'Disp'  and "Force
        #read data
        self.readData()
        self.readTimeChangeIndex()
        #dispartfit and zuhe 
        fitWholeX=[]
        fitWholeY=[]
        for i in range(len(self.timeChangeIndex)-1):
                fitX,fitY=self.fitcurveForOneLoop(i+1,4)['Disp'],self.fitcurveForOneLoop(i+1,4)['Force']
                for temp in fitY:
                    fitWholeY.append(temp)
                for temp in fitX:
                    fitWholeX.append(temp)
        # plt.plot(fitWholeX,fitWholeY)
        # plt.plot(data[2],data[3],color='r')
        return  {'Disp':fitWholeX, 'Force': fitWholeY}

    def skeleton(self):
        self.readData()
        self.readTimeChangeIndex()
        modifiedData=self.modifiedCurve()
        changeDisp,changeForce=[],[]
        temp,Data={},{}
        for i in self.timeChangeIndex:
            # changeDisp.append(self.originalData['Disp'][i])
            # changeForce.append(self.originalData['Force'][i])
            temp[modifiedData['Disp'][i]]=modifiedData['Force'][i]
        for i in sorted(temp):
            Data[i]=temp[i]
        self.Skeleton={'Disp':list(Data.keys()),'Force':list(Data.values())}



