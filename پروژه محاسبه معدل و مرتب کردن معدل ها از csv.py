import csv
# For the average
from statistics import mean
from collections import OrderedDict

def calculate_averages(input_file_name, output_file_name):
    with open(input_file_name) as file :
        reader = csv.reader(file)
        Names_Averages = dict()
        for row in reader :
            names = row[0]
            grades = list()
            for grade in row[1:]:
                grades.append(float(grade))
            average = mean(grades)
            Names_Averages[names] = average
    with open(output_file_name, 'w', newline='') as output:
        writer = csv.writer(output)
        for item in Names_Averages:
            writer.writerow([item, Names_Averages[item]])

def calculate_sorted_averages(input_file_name, output_file_name):
    with open(input_file_name) as file :
        reader = csv.reader(file)
        Names_Averages = OrderedDict()
        for row in reader :
            names = row[0]
            grades = list()
            for grade in row[1:]:
                grades.append(float(grade))
            average = mean(grades)
            Names_Averages[names] = average
    with open(output_file_name, 'w', newline='') as output:
        writer = csv.writer(output)
        sorted_items = sorted(Names_Averages.items(), key=lambda x: (x[1], x[0]))
        for name,point in sorted_items:
            writer.writerow([str(name),str(point)])
   
def calculate_three_best(input_file_name, output_file_name):
    with open(input_file_name) as file :
        reader = csv.reader(file)
        Names_Averages = OrderedDict()
        for row in reader :
            names = row[0]
            grades = list()
            for grade in row[1:]:
                grades.append(float(grade))
            average = mean(grades)
            Names_Averages[names] = average
    with open(output_file_name, 'w', newline='') as output:
        writer = csv.writer(output)
        sorted_items = sorted(Names_Averages.items(), key=lambda x: (x[1],-ord(x[0][0])), reverse=True)[:3]
        for name,point in sorted_items:
            writer.writerow([str(name),str(point)])

def calculate_three_worst(input_file_name, output_file_name):
    with open(input_file_name) as file :
        reader = csv.reader(file)
        Names_Averages = OrderedDict()
        for row in reader :
            names = row[0]
            grades = list()
            for grade in row[1:]:
                grades.append(float(grade))
            average = mean(grades)
            Names_Averages[names] = average
    with open(output_file_name, 'w', newline='') as output:
        writer = csv.writer(output)
        sorted_items = sorted(Names_Averages.items(), key=lambda x: (x[1],-ord(x[0][0])))[:3]
        for name,point in sorted_items:
            writer.writerow([str(point)])

def calculate_average_of_averages(input_file_name, output_file_name):
    with open(input_file_name) as file :
        reader = csv.reader(file)
        Names_Averages = OrderedDict()
        for row in reader :
            names = row[0]
            grades = list()
            for grade in row[1:]:
                grades.append(float(grade))
            average = mean(grades)
            Names_Averages[names] = average
    ave_ave = list(Names_Averages.values())
    ave_ave = mean(ave_ave)
    with open(output_file_name, 'w', newline='') as output:
        writer = csv.writer(output)
        writer.writerow([ave_ave])