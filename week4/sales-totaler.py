def main():
    
    while True:
        try:
            files = open(input("Enter file name: "), "r")
            break
        except:
            print("that file does not exist, try another ")

    largeArr = []

    useroutfile = input("Save to file ")
    outputfile = open(useroutfile, "w+")
    startline = "Price1        Price2      Total\n"
    outputfile.write(startline)

    for row in files:
    
        rowList = row.split()
        arr = []
        line = "${:>8}   ${:>8}   ${:>8}\n"
    
        for items in rowList:
            values = float(items[1:len(items)])
            arr.append(values)

        add = sum(arr)
        arr.append(sum(arr))
        largeArr.append(arr)
    
        formatline = line.format(arr[0], arr[1], add )
        outputfile.write(formatline)

    print("\nDone writing to", useroutfile )
    outputfile.close()

main()