import sys
from sklearn import tree


def read_problem(data_path):
    '''
    Read Libsvm format data and return labels y and data instance x.
    '''
    f = open(data_path, "r")
    Y,X = [],[]
    for line in f:
        line = line.split(' ', 1)
        label, feature = line
        Y.append(label)
        tmpx = []
        idx = 1
        for e in feature.split():
            e = e.split(':')
            for i in range(idx, int(e[0])):
                tmpx.append(0.0)
            idx = int(e[0])+1
            tmpx.append(float(e[1]))
        X.append(tmpx)
    f.close()
    return Y,X

def evaluate(teY, prY):
    corr = 0
    total = 0
    for (y1, y2) in zip(teY, prY):
        if y1 == y2:
            corr += 1
        total += 1
    print("Accuracy: {0} ({1}/{2})".format(float(corr)/total, corr, total))

def main():

    if len(sys.argv) != 3:
        print("Usage: python destree.py [train-data] [test-data]")
        exit(0)
    print(sys.argv[1])
    trY, trX = read_problem(sys.argv[1])
    teY, teX = read_problem(sys.argv[2])
  
    '''  
    for (x1, y1) in zip(trX, trY):
        print(y1, x1)
    '''
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(trX,trY)
    
    prY = clf.predict(teX)
    evaluate(teY, prY)
    

if __name__ == "__main__":
    main();
