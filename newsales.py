
while True:
    try: 
        files = open(input("Enter file name: "), "r")
        break
    except:
        print("that file does not exist, try another ")

savedlist =[]
for rows in files:
    lines = rows.strip("$").split()
    #print(lines)
    savedlist.append(lines)

print(savedlist)
# fout = open(input("File Name to create: "), "w+")
# fout.write("string")
# fout.close()sales.