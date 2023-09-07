import csv

with open('C:\\Users\\Abhishek.sharma\\PycharmProjects\\pythonProject4august\\excelcsv\\loanapp.csv') as csvFile:
    csvReader = csv.reader(csvFile,delimiter=',')
    # print(csvReader)
    # print(list(csvReader))
    names =[]
    stats = []

    for row in csvReader:
        names.append(row[0])
        stats.append(row[1])

print(names)
print(stats )

Index = names.index('Sam')
loanStatus = stats[Index]
print('loan status is' + loanStatus)

with open('C:\\Users\\Abhishek.sharma\\PycharmProjects\\pythonProject4august\\excelcsv\\loanapp.csv', 'a') as wFile:
    write = csv.writer(wFile)
    write.writerow(["Bob","rejected"])