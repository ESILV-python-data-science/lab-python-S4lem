# Open the csv file, read all the lines
f = open('jfkrelease-2017.csv', 'r')

for line in f:
     print(line, end='')

# Check that the number of fields is identical for all lines

numberFields = len(f.readline().split(';'))
print(numberFields)
for line in f:
    if numberFields == len(line.split(';')) : 
        numberFields = len(line.split(';'))
    else:
        print("Not a good CSV")
print("good csv")

# Compute the mean number of pages per document, the minimum and maximum of pages per document
numberPages = []

# How many documents have a missing number of pages ?
# There is a document with zero page. Why ?

f.close()