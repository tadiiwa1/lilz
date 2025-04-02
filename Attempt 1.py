import csv
def read_data(filename):
    file=open(filename.csv,"r")
    this_data=csv.reader(file)

    print(this_data)