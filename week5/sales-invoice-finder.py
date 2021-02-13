import csv

def findInvoiceByID(findid):
    csvfile = open('sales_data.csv')
    readCSV = csv.reader(csvfile, delimiter=',')
    idcol = []
    
    for rows in readCSV:
        if rows[0] == str(findid):
            idcol.append(rows)
            print(rows)
    print(len(idcol), " records found \n")
    csvfile.close()

def findInvoiceByLastName(findname):
    csvfile = open('sales_data.csv')
    readCSV = csv.reader(csvfile, delimiter=',')
    namecol = []
    
    for rows in readCSV:
        if rows[2] == findname:
            namecol.append(rows)
            print(rows)
    print(len(namecol), " records found \n ")
    csvfile.close()


def main():
    while True:
        
        getprompt = str(input("Search by invoice id (id) or customer last name (lname) or (q) to quit"))

        if getprompt == 'id':
            idprompt = int(input("What is the invoice ID you would like to find? "))
            findInvoiceByID(idprompt)

        elif getprompt == 'lname':
            nameprompt = str(input("What is the last name of the persons records you are trying to find? "))
            findInvoiceByLastName(nameprompt)

        elif getprompt == "q":
            break

        else:
            print("ERROR: You must enter either 'id' for Invoice ID search or 'Lname' for customer last name search \n press ctrol + c to quit\n")
        

if __name__ == '__main__':
    main()