import numpy as np
import operator
def CreateDataSet():
    group = np.array([[35.6,2],[36.9,20],[37.8,50],[36.8,4],[37.5,39],[36.6,1]])
    labels = ['正常','确诊','确诊','正常','确诊','正常']
    return group,labels
if __name__=='__main__':
    group,labels = CreateDataSet()
    print("数据样本group:",group)
    print("特征标签labels:",labels)


