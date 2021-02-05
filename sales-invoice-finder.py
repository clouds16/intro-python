import csv

csvfile = open('sales_data.csv')
readCSV = csv.reader(csvfile, delimiter=',')


def findInvoiceByID(findid):
    idcol = []
    for rows in readCSV:
        if rows[0] == str(findid):
            idcol.append(rows)
            print(rows)
    print(len(idcol), " records found \n")
    #print(idcol, type(idcol))


def findInvoiceByLastName(findname):
    namecol = []
    for rows in readCSV:

        if rows[2] == findname:
            count = count + 1
            namecol.append(rows)
            print(rows)
    # print(namecol)
    print(len(namecol), " records found \n ")


def main():

    getprompt = str(
        input("Search by invoice id (id) or customer last name (lname) "))

    if getprompt == 'id':

        idprompt = int(
            input("What is the invoice ID you would like to find? "))
        findInvoiceByID(idprompt)

    elif getprompt == 'lname':
        nameprompt = str(
            input("What is the last name of the persons records you are trying to find? "))
        findInvoiceByLastName(nameprompt)
    else:
        print("ERROR: You must enter either 'id' for Invoice ID search or 'Lname' for customer last name search \n\n")


if __name__ == '__main__':
    main()
