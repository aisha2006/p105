#importing modules
import csv
import math

#reading the data in the file
with open("data.csv", newline="") as f:
    reader = csv.reader(f)
    file_data = list(reader)

#parameter
data = file_data[0]

#function to find mean of the data
def mean(data):
    n=len(data)
    sum=0
    for x in data:
        sum+=int(x)
    mean = sum/n
    return mean

#empty list to append 
squaredList=[]

#subtracting the mean by the actual value and squaring it
for i in data:
    a=int(i)-mean(data)
    a=a**2
    squaredList.append(a)

#adding all the squared values
total=0
for t in squaredList:
    total=total+t

#dividing the (number of values - 1) by 'total'
result=total/(len(data)-1)

#obtaining the final standard deviation by taking the root of 'result'
standardDeviation = math.sqrt(result)

#displaying the standard deviation
print(standardDeviation)
