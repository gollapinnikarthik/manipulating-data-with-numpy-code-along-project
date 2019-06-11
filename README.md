### Project Overview

 # Manipulating Data with NumPy

Problem Statement
We want to know as to what happens during an IPL match which raises several questions in our mind with our limited knowledge about the game called cricket on which it is based. This analysis is done to know as which factors led one of the team to win and how does it matter.

About the Dataset :
The Indian Premier League (IPL) is a professional T20 cricket league in India contested during April-May of every year by teams representing Indian cities. It is the most-attended cricket league in the world and ranks sixth among all the sports leagues. It has teams with players from around the world and is very competitive and entertaining with a lot of close matches between teams.


### Learnings from the project

Reading data using numpy module.
Using numpy unique and shape function.
Subsetting numpy data using [:] methods.
Using conditional filtering using slicing and indexing in numpy.


### Approach taken to solve the problem

 Read the data using numpy module using np.genfromtxt function. 
Calculated the unique no. of matches in the provided dataset  using np.unique().
Found the set of all unique teams that played in the matches in the data set by slicing the numpy array and storing in different variables for two innings teams. Used union of these two sets to find all unique teams. 
Found sum of all extras in all deliveries in all matches in the dataset by slicing the numpy array and used int type casting for calculating the sum of the all extras variable.
Got the array of all delivery numbers when a given player got out along with wicket type. Used condition filtering and later subsetted the data using that condition filter. 
Created a filter that filters only those records where the batsman scored 6 runs and who has scored the maximum no. of sixes overall  was displayed. Created a variable for extracting sixes from runs column for all matches in the dataset by slicing the numpy array and used int type casting. Used counter function to count the maximum sixes hit along with the player. 


