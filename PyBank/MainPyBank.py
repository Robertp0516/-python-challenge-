#import modules
import os
import csv

#set starting directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

#Set file path
budget_file = os.path.join("../PyBank","budget_data.csv")
input("Run PyBank Calculations?")

#Lists/Variables to Store Data from CSV
Date = []
pnl_list = []
daily_change = []
daily_change2 = []
max_change = 0
min_change = 0
max_change_date = ""
min_change_date = ""
total_pnl = 0
data_length = 0
max_date = ""
max_pnl = -999999999
min_date = ""
min_pnl = 9999999999

# Method 2: Improved Reading using CSV module
with open(budget_file, encoding='utf-8') as budget_data:
  csvreader = csv.reader(budget_data, delimiter=",")

  #skip header
  budget_header = next(budget_data) 

  #calculate total months & total pnl and create Date & pnl lists
  for row in csvreader:
    daily_pnl = int(row[1])
    todays_date = str(row[0])
    total_pnl += daily_pnl
    data_length += 1
    pnl_list.append(int(row[1]))
    Date.append(str(row[0]))

  #calculate max & min changes dates & values
  for i in range(0, len(pnl_list)):
    daily_change.append(pnl_list[i] - pnl_list[i-1])
    max_change = max(daily_change)
    min_change = min(daily_change)
    max_change_date = str(Date[daily_change.index(max(daily_change))])
    min_change_date = str(Date[daily_change.index(min(daily_change))])
  
  #calculate avg change from 2nd daily change list
  for i in range(1, len(pnl_list)):
    daily_change2.append(pnl_list[i] - pnl_list[i-1])
  avg_change = sum(daily_change2) / len(daily_change2)

  #print results of analysis
Results = (
print("Financial Analysis"),
print("----------------------------"),
print("Total months: " + str(data_length) + ""),
print("Total: $" + str(total_pnl) + ""),
print("Average change: $" + str(round(avg_change,2))),
print("Greatest Increase in Profits: " + str(max_change_date) + " ($" + str(max_change) + ")"),
print("Greatest Decrease in Profits: " + str(min_change_date) + " ($" + str(min_change) + ")")
)


