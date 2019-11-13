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
    file = open("20_test.txt", "w")
    file.write("#Play tennis|Outlook|Temperature|Humidity|Wind")
    for i in nums:
        file.write("\n")
        length = len(i)
        for j in range(length):
            token = str(i[j]) + " "
            file.write(token)
    file.close()


    # file = open("80_test.txt", "w")
    # file.write("#Play tennis|Outlook|Temperature|Humidity|Wind")
    #
    # file.close()
    pass


def readInputFile(fileName):
    file = open(fileName, "r")
    features = [[]]
    output = [[]]
    features.remove([])
    output.remove([])
    i = 0
    for line in file:
        if i != 0:
            dataLine = line.split()
            nums = [int(i) for i in dataLine]
            output.append(nums[0])
            features.append(nums[1:4])
        i += 1
    output = np.array(output)
    random.shuffle(output)
    data = np.array(features)
    random.shuffle(features)
    print(data)
    print(output)
    return data, output


nums = loadData()
print(nums)
write80and20(nums)
# readInputFile("80_train.txt")
# readInputFile("20_train.txt")