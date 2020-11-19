import os
import matplotlib.pyplot as plt
import numpy as np 

class CurrentComponent():
    '''Construct a Component Class with init input path of .dat and .log'''

    def __init__(self,pathofdat,pathoflog):
        self.pathofdat=pathofdat
        self.pathoflog=pathoflog


    def fitcurveForOneLoop(self,indexGroup:int,degree:int):
        '''indexGroup: number of group
        degree: degree of polynominal to fit statistic'''
        groupData=self.dispart(indexGroup)
        polyCoeff=np.polyfit(groupData['Disp'],groupData['Force'],degree)
        polyNominal=np.poly1d(polyCoeff)
        fitY=[]
        for i in groupData['Disp']:
            fitY.append(polyNominal(i))
        return {'Disp':groupData['Disp'],'Force':fitY}


    def readData(self):
        '''Get TimeStop, TimeIndex, OriginalData(dic) as self.property'''
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
        self.TimeStop,self.TimeIndex,self.OriginalData=TimeStop,TimeIndex,{'Disp':Disp,'Force':Force}

    
    def readTimeChangeIndex(self):
        '''Through TimeStop(ChangePoints) find change Valve to dispart the curve, ouput Time change index
            \n !!!!Get index of time when you change aimed deformation or velocity of loading '''
        self.TimeChangeIndex=[]
        for i in self.TimeStop:
            index,gap=0,100000000
            for j,k in enumerate(self.TimeIndex):
                if abs(i-k)<gap:
                    gap=abs(i-k)
                    index=j
            self.TimeChangeIndex.append(index)
        self.TimeChangeIndex.pop()
        self.TimeChangeIndex.pop(0)
        self.TimeChangeIndex.pop(0)
        return self.TimeChangeIndex

    
    def dispart(self,i:int):
        ''' Dispart from original data. According to Timechangeindex\n 
        i represent group sequence \n
        for example self.TimeChangeIndex=[1,5,9]  there is two group of data, first group contain data[1:5] second group contain data[5:9]
        '''
        self.readData()
        self.readTimeChangeIndex()
        dispartTimeIndex=self.TimeIndex[self.TimeChangeIndex[i-1]:self.TimeChangeIndex[i]]
        dispartDisp=self.OriginalData['Disp'][self.TimeChangeIndex[i-1]:self.TimeChangeIndex[i]]
        dispartForce=self.OriginalData['Force'][self.TimeChangeIndex[i-1]:self.TimeChangeIndex[i]] 
        return {'Time':dispartTimeIndex,'Disp':dispartDisp,'Force':dispartForce}

        
    def modifiedCurve(self):
        ''' output fitedCurve using dictionary with keys labeled 'Disp'and 'Force' '''
        #read data
        self.readData()
        self.readTimeChangeIndex()
        #dispartfit and zuhe 
        fitWholeX=[]
        fitWholeY=[]
        for i in range(len(self.TimeChangeIndex)-1):
                fitX,fitY=self.fitcurveForOneLoop(i+1,4)['Disp'],self.fitcurveForOneLoop(i+1,4)['Force']
                for temp in fitY:
                    fitWholeY.append(temp)
                for temp in fitX:
                    fitWholeX.append(temp)
        # plt.plot(fitWholeX,fitWholeY)
        # plt.plot(data[2],data[3],color='r')
        return  {'Disp':fitWholeX, 'Force': fitWholeY} 

    
    def modifiedCurveDecreased(self,interval:int):
        '''Every interval numbers data produce a valid data to decrease total data number''' 
        modifiedData=self.modifiedCurve()
        DispDecreased,ForceDecreased=[],[]
        for i in range(0,len(modifiedData['Disp']),interval):
            DispDecreased.append(modifiedData['Disp'][i])
            ForceDecreased.append(modifiedData['Force'][i])
        return {'Disp':DispDecreased,'Force':ForceDecreased}


    def skeleton(self,modifiedSkeleton=0):
        self.readData()
        self.readTimeChangeIndex()
        modifiedDataDecreased=self.modifiedCurveDecreased(10)
        DispMin,DispMax=min(modifiedDataDecreased['Disp']),max(modifiedDataDecreased['Disp'])
        Data={}
        for i in range(int(DispMin),int(DispMax),1):
            for j,k in enumerate(modifiedDataDecreased['Disp']):
                if i<=k<=i+1:
                    Data[i]=modifiedDataDecreased['Force'][j]
                    break
                else:
                    pass
        # for i in self.TimeChangeIndex:
        #     # changeDisp.append(self.OriginalData['Disp'][i])
        #     # changeForce.append(self.OriginalData['Force'][i])
        #     # temp[modifiedData['Disp'][i]]=modifiedData['Force'][i]
        #     temp[self.OriginalData['Disp'][i]]=self.OriginalData['Force'][i]
        # for i in sorted(temp):
        #     Data[i]=temp[i]
        skeleton={'Disp':list(Data.keys()),'Force':list(Data.values())}
        if modifiedSkeleton:
            polyCoeff=np.polyfit(skeleton['Disp'],skeleton['Force'],4)
            polyNominal=np.poly1d(polyCoeff)
            fitedCurve=[]
            for i in skeleton['Disp']:
                fitedCurve.append(polyNominal(i))
            skeleton['Force']=fitedCurve
        return skeleton


    def visualData(self,skeleton=0,modifiedCurve=0,save=0):
        '''Change values of para to plot coorespond data: 0 for not ploting and non-0 for ploting'''
        if skeleton:
            skeleton=self.skeleton()
            plt.plot(skeleton['Disp'],skeleton['Force'])
        if modifiedCurve:
            modifiedCurve=self.modifiedCurveDecreased(100)
            plt.plot(modifiedCurve['Disp'],modifiedCurve['Force'])
        if save:
            plt.savefig("1.png")

    def yieldPoint(self):
        skeleton=self.skeleton(1)
       
        
        plt.plot(skeleton['Disp'],skeleton['Force'])
        
        
    

    



