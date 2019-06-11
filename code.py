# --------------
import numpy as np
from collections import Counter
# Not every data format will be in csv there are other file formats also.
# This exercise will help you deal with other file formats and how to read it.

data = np.genfromtxt(path, dtype = 'str', delimiter = ',', skip_header=1)
print(data.shape)
# Number of unique matches 
number_of_unique_matches = len(np.unique(data[0]))
print("No.of unique matches played:- ", number_of_unique_matches)

 # How many matches were held in total we need to know so that we can analyze further statistics keeping that in mind.
total_number_of_matches = data[:, 3].shape
print("Total Number of matches played:- ", total_number_of_matches[0])

# Number of unique teams
set_1_teams = set(data[:, 3])
set_2_teams = set(data[:, 4])
set_of_unique_teams = set_1_teams.union(set_2_teams)
print("Set of unique teams:- ", set_of_unique_teams)
 
# this exercise deals with you getting to know that which are all those six teams that   played in the tournament.

# Sum of all extras
sum_of_all_extras = data[:, 17].astype('int16').sum()
print("Sum of all extras:- ", sum_of_all_extras)
 # An exercise to make you familiar with indexing and slicing up within data.

# Delivery number when a given player got out

 # Get the array of all delivery numbers when a given player got out. Also mention the wicket type.
wicket_filter = (data[:, 20] == 'SR Tendulkar')
wickets_arr = data[wicket_filter]
wickets_arr[:, 11]
 

# Number of times Mumbai Indians won the toss
Mi_team_toss_win =  data[data[:, 5] == 'Mumbai Indians']
unique_matches = len(set(Mi_team_toss_win[:, 0]))
print('Number of times Mumbai Indians won the toss: ', unique_matches)

 # this exercise will help you get the statistics on one particular team

# Filter record where batsman scored six and player with most number of sixes
sixes = data[data[:, 16].astype(np.int16) == 6]
most_sixes = Counter(sixes[:, 13],).most_common(1)
print('Player with maximum sixes: ', most_sixes)


 # An exercise to know who is the most aggresive player or maybe the scoring player 







