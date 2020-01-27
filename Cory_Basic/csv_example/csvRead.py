# https://www.youtube.com/watch?v=q5uM4VKywbA&index=28&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU
'''
Python Tutorial: CSV Module - How to Read, Parse, and Write CSV Files
'''
import csv

# reading csv file
# with open('csvFile.csv', 'r') as csv_file:
#     csv_reader = csv.reader(csv_file)
#      csv_reader = csv.reader(csv_file, delimiter='\t')  #it will read the file with \t delimiter by splitting each
#     next(csv_reader)  # when you put next before loop.. loop fill start from second value
#     for line in csv_reader:
#         print(line)

# writing csv file
# with open('csvFile.csv', 'r') as csv_file:
#     csv_reader = csv.reader(csv_file)
#
#     with open('csvwrite.csv','w')as new_file:
#         csv_writer = csv.writer(new_file, delimiter='\t')
#
#         for line in csv_reader:
#             csv_writer.writerow(line)

# writing csv file using dictionary
with open('csvwrite.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open('new_csvwrite.csv','w')as new_file:
        fieldnames= ['first_name','last_name','email']

        csv_writer = csv.DictWriter(new_file, fieldnames='fieldnames', delimiter='\t', extrasaction='ignore')
        csv_writer.writeheader()

        for line in csv_reader:
            csv_writer.writerow(line)


# writing csv file using dictionary and deleting unwanted columns - here I am deleting email column
# with open('csvwrite.csv', 'r') as csv_file:
#     csv_reader = csv.DictReader(csv_file)
#
#     with open('new1_csvwrite.csv','w')as new_file:
#         field_names= ['first_name','last_name']
#
#         csv_writer = csv.DictWriter(new_file, fieldnames='field_names', delimiter='\t',extrasaction='ignore')
#         csv_writer.writeheader()
#
#         for line in csv_reader:
#             del line['email']
#             csv_writer.writerow(line)

