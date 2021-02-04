
while True:
    try:
        files = open(input("Enter file name: "), "r")
        break
    except:
        print("that file does not exist, try another ")

listitem = []
outputfile = open(input("Save to file "), "w+")


for row in files:
    print(row.split(), type(row.split()))
    rowList = row.split()
    for items in rowList:
        values = float(items[1:len(items)])
        listitem.append(values)

print(len(listitem), listitem)
outputstring = "${}  ${} ${}\n${}  ${} ${} "
formatstring = outputstring.format(str(listitem[0]), str(listitem[1]), str(
    listitem[0] + listitem[1]), str(listitem[2]), str(listitem[3]), str(listitem[2] + listitem[3]))

outputfile.write(formatstring)
outputfile.close()
