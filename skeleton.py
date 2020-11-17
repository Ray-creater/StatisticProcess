import hysteresis as hy 
import os
import matplotlib.pyplot as plt


def main():
    OriginalPath=os.getcwd()
    OriginalPathData=os.path.join(OriginalPath,'1212.dat')
    OriginalPathTimeLimit=os.path.join(OriginalPath,'1212.log')
    component=hy.CurrentComponent(OriginalPathData,OriginalPathTimeLimit)
    component.skeleton()
    print(component.Skeleton)
    plt.plot(component.Skeleton['Disp'],component.Skeleton['Force'])
    plt.show()




if __name__ == "__main__":
    main()