import hashlib
import csv

def hash_password_hack(input_file_name, output_file_name):
    passdic = dict()
    for i in range(1000,9999):
        nums = str(i)
        converted = hashlib.sha256(nums.encode()).hexdigest()
        passdic[converted] = nums
    with open(input_file_name) as file :
        reader = csv.reader(file)
        namepass = dict()
        for name,passw in reader:
            names = name
            passwords = passw
            namepass[names] = passwords
    with open(output_file_name, 'w' , newline='') as outfile :
        writer = csv.writer(outfile)
        for item in namepass:
            temp = namepass[item]
            foundedpass = passdic[temp]
            writer.writerow([item,foundedpass])