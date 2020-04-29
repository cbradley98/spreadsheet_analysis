import csv

parliament_rep = []

no_rep = 0

with open('gender_inequality.csv', 'r') as csv_file:
    spreadsheet = csv.DictReader(csv_file)
    for row in spreadsheet:
        rep_string = row['Percent Representation in Parliament']
        if rep_string == '..':
            rep_string = '0'
            no_rep = no_rep + 1
        rep = float(rep_string)
        parliament_rep.append(rep)

total_rep = sum(parliament_rep)
average_rep = total_rep / len(parliament_rep)

print('Average Percent Representation in Parliament {}'.format(average_rep))
print('Number of countries without data representation: {}'.format(no_rep))
