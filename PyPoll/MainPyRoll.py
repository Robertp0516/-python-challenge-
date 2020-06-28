#import modules
import os
import csv
import collections as ct

#set starting directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

#Set file path
election_file = os.path.join("../PyPoll","election_data.csv")
input("Run PyPoll Calculations?")

Total_votes = 0
votes_dict = {}
votes = []
# Method 2: Improved Reading using CSV module
with open(election_file, encoding='utf-8') as election_data:
  csvreader = csv.reader(election_data, delimiter=",")

  #Skip Header
  election_header = next(election_data)
  
  #Calculate total votes
  for row in csvreader:

    Total_votes += 1
    votes.append(str(row[2]))

  
  #build dictionary with candidates' vote totals

  for vote in votes:
    if vote in votes_dict:
      votes_dict[vote] += 1
    else:
      votes_dict[vote] = 1
    
  
  #build lists to for percent calculations + deciding winner in dictionary

  vote_totals = list(votes_dict.values())
  names = list(votes_dict.keys())
  winner = max(votes_dict, key=votes_dict.get)

  #print(str(winner))
  #print(vote_totals)
  #print(names)

#calculate percentages from vote total list

Khan_percent = round(((int(vote_totals[0])) / int(Total_votes) * 100),0)
Correy_percent = round(((int(vote_totals[1])) / int(Total_votes) * 100),0)
Li_percent = round(((int(vote_totals[2])) / int(Total_votes) * 100),0)
OTooley_percent = round(((int(vote_totals[3])) / int(Total_votes) * 100),0)
  
#Election Results Format 
Results = (
print("Election Results Format"),
print("-------------------------"),   
print("Total Votes: " +  str(Total_votes)),
print("-------------------------"),   
print(str(names[0]) + " " + str(Khan_percent) + "% (" + str(vote_totals[0]) + ")"),
print(str(names[1]) + " " + str(Correy_percent) + "% (" + str(vote_totals[1]) + ")"),
print(str(names[2]) + " " + str(Li_percent) + "% (" + str(vote_totals[2]) + ")"),
print(str(names[3]) + " " + str(OTooley_percent) + "% (" + str(vote_totals[3]) + ")"),
print("-------------------------"),
print("Winner: " + str(winner)),
print("-------------------------")
)
