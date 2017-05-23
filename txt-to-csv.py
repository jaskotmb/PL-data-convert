import csv
import os

# function to remove weird character out of list of names and return list of clean names
def cleanNames(dataNames):
    cleanedDataNames = []
    for j in range(len(dataNames)):
        cleanedDataNameTemp = ''
        for i in range(len(dataNames[j])):
            if ord(dataNames[j][i]) == 65403:
                cleanedDataNameTemp += cleanedDataNameTemp.join('-')
            else:
                cleanedDataNameTemp += cleanedDataNameTemp.join(dataNames[j][i])
        cleanedDataNames.append(cleanedDataNameTemp)
    return cleanedDataNames


# Function to take in an array of data
# Returns list of floats from whichever column of data is specified with "index"
def dataColumn(dataPoints,dataLine,index):
    X1 = []
    for i in range(dataPoints):
        if not(dataLine[i][index] == ''):
            X1.append(dataLine[i][index])
    return(X1)

# Given a max data length, pads data with '' to make same length
def padSmallColumns(inputColumn,maxLength):
    if len(inputColumn) < maxLength:
        for i in range(maxLength-len(inputColumn)):
            inputColumn.append('')
    return inputColumn

#####################################################################################
# Body of Script
#####################################################################################

# Prompt for directory, get ".txt" file list
os.chdir("/home/jaskotmb/Documents/Mines/Research/OLED/170517_Irppy3_CBP_PL_Tseries")
direcOpen = input("Input directory (or Enter for {})".format(os.getcwd()))
files = [file for file in os.listdir(os.getcwd()) if '.txt' in file]

for k in range(len(files)):
    print("File {:2} = {}".format(k+1,files[k]))
    # Reading in raw data lines
    rawFile = open("/home/jaskotmb/Documents/Mines/Research/OLED/170517_Irppy3_CBP_PL_Tseries/{}".format(files[k]),'r',encoding='shiftjis')
    temp = []
    for line in rawFile:
        temp.append(line.split('\n')[0])
    rawFile.close()

    # Line 2 contains header labels
    # Line 4 is where data starts

    # Length of longest data index
    dataMaxLength = len(temp) - 5
    # 5 non-data lines:
    # line0 throwaway, line1 #headers, line2 data labels, line3 X,Y labels, last line throwaway
    # Data on lines 4 thru (len(temp)-2)

    # for i in range(4,(len(temp)-1)):
    #     print(temp[i])

    # Slicing data to what I need to use
    dataArray = []
    for i in range(4,(len(temp)-1)):
        dataArray.append(temp[i].split('\t'))

    # List of names of datasets
    dataLabels = temp[2].split('\t')[::2]

    # Cleaning up data list of data labels
    cleanLabelsTemp = cleanNames(dataLabels)
    print("cleanLabelsTemp = {}".format(cleanLabelsTemp))
    cleanLabels = []
    for i in range(len(cleanLabelsTemp)):
        print(cleanLabels)
        cleanLabels.append("X{}".format(i+1))
        cleanLabels.append(cleanLabelsTemp[i])
    print("cleanLabels = {}".format(cleanLabels))
    # Getting first column
    C1 = dataColumn(dataMaxLength,dataArray,0)

    # Assembling array of str formatted data in rows
    Total = [padSmallColumns(C1,dataMaxLength)]
    for i in range(1,len(cleanLabels)):
        print(i)
        Total.append(padSmallColumns(dataColumn(dataMaxLength,dataArray,i),dataMaxLength))
    s = [list(i) for i in zip(*Total)]

    # Writing data to output file
    with open("/home/jaskotmb/Documents/Mines/Research/OLED/170517_Irppy3_CBP_PL_Tseries/{}.csv".format(files[k][:-4]),'w',encoding='utf-8') as csvfile:
        spamwriter = csv.writer(csvfile,delimiter=',')
        spamwriter.writerow(cleanLabels)
        for row in s:
            spamwriter.writerow(row)



