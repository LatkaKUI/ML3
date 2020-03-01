import numpy as np
import operator
from CreateDataSet import CreateDataSet


def classify0(inX,dataSet,labels,k):
    dataSetSize = dataSet.shape[0]
    print("dataSet的行数",dataSetSize)

    diffMat = np.tile(inX,(dataSetSize,1)) - dataSet
    print("tile函数",np.tile(inX,(dataSetSize,1)))
    print("diffMat",diffMat)
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances**0.5
    print("distances距离",distances)
    sortedDistIndices = distances.argsort()
    print("sortedDistIndices0索引值",sortedDistIndices)

#定义一个记录类别次数的字典  KNN 算法
    classCount = {}
    print("classCount0",classCount)
    print("labels",labels)
    print("labels2",labels[2])
    for i in range(k):
        voteIlabel = labels[sortedDistIndices[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
        print("classCount[voteIlabel",classCount[voteIlabel])
    sortedClassCount = sorted(classCount.items(),key= operator.itemgetter(1),reverse=True)
    print("classCount2",sortedClassCount)
    return sortedClassCount[0][0]

if __name__ == '__main__':
    group,labels = CreateDataSet()

    test=[37.4,40]
    test_class = classify0(test,group,labels,3)
    print("test_class:",test_class)

#如何实现像百度页面那样的算法应用？
#