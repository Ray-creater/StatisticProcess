
import numpy as np
import scipy as sp

def areaMethod(skeleton:dict):
    '''Using principle of equal Area to seek yield point (Consume same amount of energy from zero to peak )''' 
    polyCoeff=np.polyfit(skeleton['Disp'],skeleton['Force'],4)
    polyNominal=np.poly1d(polyCoeff)
    ForcePeak=max(skeleton['Force'])
    DispPeak=skeleton['Disp'][skeleton['Force'].index(ForcePeak)]
    SwapAreaContrast,DispSelectYieldPoint=10000,0
    for DispCrossPonit in np.linspace(0,DispPeak,20):
        ForceCrossPoint=polyNominal(DispCrossPonit)
        DispYieldPoint=DispCrossPonit/ForceCrossPoint*ForcePeak
        AreaContrast=1/2*DispYieldPoint*ForcePeak+ForcePeak*(DispPeak-DispYieldPoint)-sp.integrate.quad(polyNominal,0,DispPeak)[0]
        if AreaContrast<SwapAreaContrast:
            SwapAreaContrast=AreaContrast
            DispSelectYieldPoint=DispYieldPoint
    return {"Disp":DispSelectYieldPoint,'Force':polyNominal(DispSelectYieldPoint),'ErrorGap':SwapAreaContrast}


def geometry(skeleton:dict):
    polyCoeff=np.polyfit(skeleton['Disp'],skeleton['Force'],4)
    polyNominal=np.poly1d(polyCoeff)
    kInit=polyNominal(1)-polyNominal(0)
    ForcePeak=max(skeleton['Force'])
    DispPeak=skeleton['Disp'][skeleton['Force'].index(ForcePeak)]
    DispSwap=ForcePeak/kInit
    ForceSwap=polyNominal(DispSwap)
    DispYieldPoint=DispSwap/ForceSwap*ForcePeak
    return {'Disp':DispYieldPoint,'Force':polyNominal(DispYieldPoint)}

def rpartMethod(skeleton:dict):
    polyCoeff=np.polyfit(skeleton['Disp'],skeleton['Force'],4)
    polyNominal=np.poly1d(polyCoeff)
    ForcePeak=max(skeleton['Force'])
    DispPeak=skeleton['Disp'][skeleton['Force'].index(ForcePeak)]
    ForceSwap=0.75*ForcePeak
    DispSwap,gap=0,1500
    for i in np.linspace(0,DispPeak,0.1):
        if abs(polyNominal(i)-ForceSwap)<gap:
            gap=abs(polyNominal(i)-ForceSwap)
            DispSwap=i
    DispYieldPoint=DispSwap/ForceSwap*ForcePeak
    return {'Disp':DispYieldPoint,'Force':polyNominal(DispYieldPoint)}

# def energyDissipation(skeleton:dict):
#     DispMax,DispMin=max(skeleton['Disp']),min(skeleton['Disp'])
#     IndexMax,IndexMin=skeleton['Disp'].index(DispMax),skeleton['Force'].index(DispMin)
#     if IndexMax<IndexMin:
#         IndexMin,IndexMax=IndexMax,IndexMin
#     oneHalfLoop={"Disp":skeleton['Disp'][IndexMin:IndexMax],'Force':skeleton['Force'][IndexMin,IndexMax]}
#     remainDisp,remainForce=skeleton['Disp'][0:IndexMin],skeleton['Force'][0:IndexMin]
#     remainDisp.extend(skeleton['Disp'][IndexMax:])
#     remainForce.extend(skeleton['Force'][IndexMax:])
    





