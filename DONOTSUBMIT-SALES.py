with open('sales.txt') as f:
    matrix = [line.split() for line in f]

print(matrix)

# strip $ from lines and convert to float from string
def parseFile(file):
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            cellvalue = matrix[row][col]
            reducedstring = float(cellvalue[1:len(cellvalue)])
            matrix[row][col] = reducedstring
  
    for row in range(len(matrix)): 
        line = matrix[row]
        line.append(sum(line))
        
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            cellvalue = matrix[row][col]
            stringvalue = str(cellvalue)
            matrix[row][col] = "$" + stringvalue


def main():
    parseFile(matrix)
    print(matrix)
    


if __name__ == "__main__":
    main()