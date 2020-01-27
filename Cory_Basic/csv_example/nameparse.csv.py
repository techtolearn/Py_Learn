# https://www.youtube.com/watch?v=bkpLhQd6YQM&index=29&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU
# Real World Example - Parsing Names From a CSV to an HTML List
import csv

html_output = ''
names =[]

with open('namePatron.csv', 'r') as data_file:

# Below code used for parsiing csv file in the form of html tag using csv.reader

#   csv_data = csv.reader(data_file)
#    # print(list(csv_data))
#   next(csv_data)  #skip the current line and go to next line
#   next(csv_data)
#   for line in csv_data:
#         if line[0] == 'No Reward':
#             break
#         names.append(f'{line[0]} {line[1]}')
# # for name in names:
# #     print(name)
#
# html_output += f'<p> there are currently {len(names)} public contributors. thank you! </p> '
#
# html_output += '\n<ul>'
# for name in names:
#     html_output += f'\n\t<li>{name}</li>'
# html_output += '\n<ul>'
# print(html_output)

# Below same code used for parsiing csv file in the form of html tag using csv.DictReader method

  csv_data = csv.DictReader(data_file)

  next(csv_data)  #skip the current line and go to next line to avoid bad data

  for line in csv_data:
        if line['FirstName'] == 'No Reward':
            break
        names.append(f"{line['FirstName']} {line['LastName']}")
# for name in names:
#     print(name)

html_output += f'<p> there are currently {len(names)} public contributors. thank you! </p> '

html_output += '\n<ul>'
for name in names:
    html_output += f'\n\t<li>{name}</li>'
html_output += '\n<ul>'
print(html_output)
