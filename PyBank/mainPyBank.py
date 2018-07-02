import csv
import os

file = os.path.join('raw_data', 'budget_data_'+ str(file_num) +'.csv')


months = []
revenue = []


with open(file, 'r') as csvfile:
    csvread = csv.reader(csvfile)
    
    next(csvread, None)

    for row in csvread:
        months.append(row[0])
        revenue.append(int(row[1]))


total_months = len(months)


greatest_inc = revenue[0]
greatest_dec = revenue[0]
total_revenue = 0


for r in range(len(revenue)):
    if revenue[r] >= greatest_inc:
        greatest_inc = revenue[r]
        great_inc_month = months[r]
    elif revenue[r] <= greatest_dec:
        greatest_dec = revenue[r]
        great_dec_month = months[r]
    total_revenue += revenue[r]


average_change = round(total_revenue/total_months, 2)


output_dest = os.path.join('Output','pybank_output_' + str(file_num) + '.txt')

print("Financial Analysis")
print("----------------------------")    
print("Total Months: " + int(total_months)
print("Total: " + "$" + int(total_revenue)
print("Average Change: " + int(average_change))
print("Greatest Increase in Profits: " + great_inc_month + int(great_inc_month)
print("Greatest Decrease in Profits: " + great_dec_month + int(great_dec_month))	


with open(output_dest, 'r') as readfile:
    print(readfile.read())
