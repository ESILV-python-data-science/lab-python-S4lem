import pprint
def question1_1():
    # Open the csv file, read all the lines

    f = open('jfkrelease-2017.csv', 'r')
    
    for line in f:
         print(line, end='')
    f.close()

def question1_2():
# Check that the number of fields is identical for all lines
    f = open('jfkrelease-2017.csv', 'r')

    numberFields = len(f.readline().split(';'))
    i= 0
    for line in f:
        i= i+1
        if numberFields == len(line.split(';')) : 
            numberFields = len(line.split(';'))
        else:
            print("Not a good line: line n° %d, it contains %d fields" %(i,len(line.split(';'))))
    
    f.close()


def question2_1():
    # Compute the mean number of pages per document, the minimum and maximum of pages per document
    
    f = open('jfkrelease-2017.csv', 'r')
    
    minimum = 0; maximum=0; average=0; summ=0; count=0
    
    for line in f:
        lineSplitted = line.split(';')
        try:
            numberPage = int(lineSplitted[11])
            if numberPage < minimum:
                minimum = numberPage
            if numberPage > maximum:
                maximum = numberPage
            count = count + 1
            summ = summ + numberPage
        except ValueError:
            print("String catched")

    average = summ / count    
    print("minimum : %d" %minimum)
    print("maximum : %d" %maximum)
    print("average : %d" %average)
    
    f.close()

    
    # How many documents have a missing number of pages ?
    
def question2_2():
        
    f = open('jfkrelease-2017.csv', 'r')
    countAll = 0; countmiss = 0

    for line in f:
        lineSplitted = line.split(';')
        try:
            countAll = countAll + 1
            int(lineSplitted[11])
        except ValueError:
            countmiss = countmiss + 1                
    print("There is %d out of %d missing lines in this file" %(countmiss, countAll))
    f.close()


# There is a document with zero page. Why ?
# The file is missing.


def question3_1():
    #How many types of document is there in the collection ?
    
    f = open('jfkrelease-2017.csv', 'r')
    documentTypes = []
    for line in f:
        lineSplitted = line.split(';')
        
        if not lineSplitted[6] in documentTypes:
            documentTypes.append(lineSplitted[6])
    
    print(len(documentTypes))
    f.close()


def question3_2():
    #Compute the number of documents per document type (use a dictionaly to store the count per document type)
    f = open('jfkrelease-2017.csv', 'r')
    documentTypes = {}
    for line in f:
        lineSplitted = line.split(';')
        
        if not lineSplitted[6] in documentTypes:
            documentTypes[lineSplitted[6]] = 1
            #documentTypes.append(lineSplitted[6])
        else:
            documentTypes[lineSplitted[6]] = documentTypes[lineSplitted[6]] + 1
    pprint.pprint(documentTypes)
        
    f.close()

def question3_3():
    #How many different agencies are involved ?
    f = open('jfkrelease-2017.csv', 'r')
    
    agencies = []
    for line in f:
        lineSplitted = line.split(';')

        if not lineSplitted[4] in agencies:
            
            agencies.append(lineSplitted[4])
    
    print("There are %d agencies" %len(agencies))
    f.close()


def question3_4():
    #Computer the number of document per agency (use a dictionary)
    documentNumbers = {}
    f = open('jfkrelease-2017.csv', 'r')
    
    for line in f:
        lineSplitted = line.split(';')
        
        if not lineSplitted[4] in documentNumbers:
            documentNumbers[lineSplitted[4]] = 1
        else:
            documentNumbers[lineSplitted[4]] += 1
    
    pprint.pprint(documentNumbers)
    f.close()
    
question3_4()