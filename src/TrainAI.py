import pickle
import numpy as np
import random


def loadData():
    file = open("TrainingData.txt", "r")
    output = [[]]
    output.remove([])
    i = 0
    for line in file:
        if i != 0:
            dataLine = line.split()
            nums = [int(i) for i in dataLine]
            output.append(nums)
        else:
            header = line
        i += 1
    file.close()
    return output


def write80and20(nums):
    random.shuffle(nums)
    #testing data
    file = open("20_test.txt", "w")
    file.write("#Play tennis|Outlook|Temperature|Humidity|Wind")
    nums20 = nums[0:int(len(nums)*0.2)]
    for i in nums20:
        file.write("\n")
        length = len(i)
        for j in range(length):
            token = str(i[j]) + " "
            file.write(token)
    file.close()
    #training data
    file = open("80_train.txt", "w")
    file.write("#Play tennis|Outlook|Temperature|Humidity|Wind")
    nums80 = nums[int(len(nums)*0.2):]
    for i in nums80:
        file.write("\n")
        length = len(i)
        for j in range(length):
            token = str(i[j]) + " "
            file.write(token)
    file.close()


def readInputFile(fileName):
    file = open(fileName, "r")
    features = []
    output = []
    i = 0
    for line in file:
        if i != 0:
            dataLine = line.split()
            nums = [int(i) for i in dataLine]
            output.append(nums[0])
            features.append(nums[1:4])
        i += 1
    output = np.array(output)
    data = np.array(features)
    return data, output


nums = loadData()
write80and20(nums)
trainingData = readInputFile("80_train.txt")
testingData = readInputFile("20_test.txt")