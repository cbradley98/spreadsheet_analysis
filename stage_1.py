import csv

monthly_sales = []

with open('sales.csv', 'r') as csv_file:
    spreadsheet = csv.DictReader(csv_file)
    for row in spreadsheet:
        sales = int(row['sales'])
        monthly_sales.append(sales)

total_sales = 0
for month in monthly_sales:
    total_sales = total_sales + month

print('Total sales: {}'.format(total_sales))
