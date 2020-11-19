
import numpy as np

def AreaMethod(skeleton:dict):
    '''    Using principle of equal Area to seek yield point (Consume same amount of energy from zero to peak )''' 
    polyCoeff=np.polyfit(skeleton['Disp'],skeleton['Force'],4)
    polyNominal=np.poly1d(polyCoeff)
    ForcePeak=max(skeleton['Force'])
    DispPeak=skeleton['Disp'][skeleton['Force'].index(ForcePeak)]
    SwapAreaContrast,DispSelectYieldPoint=10000,0
    for DispCrossPonit in np.linspace(0,DispPeak,0.1):
        ForceCrossPoint=polyNominal(DispCrossPonit)
        DispYieldPoint=DispCrossPonit/ForceCrossPoint*ForcePeak
        AreaContrast=1/2*DispYieldPoint*ForcePeak+ForcePeak*(DispPeak-DispYieldPoint)-np.integer(polyNominal,0,DispPeak)
        if AreaContrast<SwapAreaContrast:
            SwapAreaContrast=AreaContrast
            DispSelectYieldPoint=DispYieldPoint
    return {"Disp":DispSelectYieldPoint,'Force':polyNominal(DispSelectYieldPoint),'ErrorGap':SwapAreaContrast}



