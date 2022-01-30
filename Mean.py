import csv 
with open("height-weight.csv",newline="") as f:
    reader=csv.reader(f)
    fileData=list(reader)

fileData.pop(0)
newData=[]
for i in range(len(fileData)):
    n_num=fileData[i][1]
    newData.append(float(n_num))

# mean
total=0
n=len(newData)
for x in newData:
    total+=x
mean=total/n
print("mean= "+ str(mean))