import os
entries = os.listdir('.')
print(entries)

try:
    data = input()
except ValueError:
    data = "you have failed to enter data. Try again"

def writeData(data):
    with open('data.txt', 'w') as f:
        f.write(data)

writeData(data)

def readData(data):
    with open('data.txt', 'r') as f:
        data = f.read()
        print("retrieved data from text file: ", data)

readData()