import hysteresis as hy 
import os
import matplotlib.pyplot as plt


def main():
    OriginalPath=os.getcwd()
    OriginalPathData=os.path.join(OriginalPath,'1212.dat')
    OriginalPathTimeLimit=os.path.join(OriginalPath,'1212.log')
    component=hy.CurrentComponent(OriginalPathData,OriginalPathTimeLimit)
    component.yieldPoint()
    component.visualData()




if __name__ == "__main__":
    main()