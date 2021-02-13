inputFileName = input("Enter sales file name: ")
outputFileName = input("Enter name for total sales file: ")
inFile = open(inputFileName, "r")
outFile = open(outputFileName, "w")
inFile.close()
outFile.close()

nameSeq = inFile.readlines()
for name in nameSeq:
    splitSales = name.strip().split(" ")
    salesS = splitSales [0]
    salesT = splitSales [1]
    allSales = salesS $[0] + salesT$[:9]
    print(allSales,${:< 6}, file = outFile)
    print("inputFilename + outputFileName")
    
    
    print("Done writing total to $,{:< 6")
