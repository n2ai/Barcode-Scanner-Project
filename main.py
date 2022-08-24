import csv, copy

def read_scanned(filename):
    scanned_list = []
    textFile = open(filename, 'r')
    for line in textFile:
        scanned_list.append(line.rstrip('\n'))
    return scanned_list

def readFile(filename):
    database_list = []
    with open(filename, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
           database_list.append(line)
    return database_list

def checkDatabase(inputList, database):
    absent_students = copy.deepcopy(database)
    index = 0
    while index < len(inputList):
        for student in absent_students:
            if inputList[index] in student:
                absent_students.remove(student)
           
        index+=1

    return absent_students


def create_absent_list(absent_list):
    with open ('absent_students.csv', 'w') as writeFile:
        csv_writer = csv.writer(writeFile, delimiter=',')
        
        for student in absent_list:
            csv_writer.writerow(student)

if __name__ == '__main__':
    database = readFile('database.csv')
    #show the way to read text file, the beneath is just a demo
    scannedData = read_scanned('test.txt')

    absent_students = checkDatabase(scannedData, database)

    create_absent_list(absent_students)

    print(absent_students)

    
