import numpy as np

inputMatrix = np.loadtxt(fname = "E:\Msc\CoMOLA-master\models\economy\map.asc", skiprows=6)
rows, columns = inputMatrix.shape
economy_landuses = np.array([3, 7])
results = 0

for i in range(rows):
    for j in range(columns):
        cellValue = inputMatrix[i][j]
        if cellValue in economy_landuses:
          results += pow(25, 2)
print("results", results)
f = open("E:\Msc\CoMOLA-master\models\economy\economy_output.csv", "w")
f.write(str(results))
f.close