# mTSP
Multiple Travelling Salesman Problem (MTSP) is an extension of the famous 
Travelling Salesman Problem (TSP) that visiting each city exactly once with 
no sub-tours. MTSP involves assigning m orders to n vehicles, and each city
must be visited by a salesman while requiring a minimum duration time.

This script finds the routes that minimizes the total delivery duration.No
external libraries used in this algorithm, only built-in libraries were used.

There were seven job location and 5040 possible routes. In the given input
data, there were vehicle information, order information, and duration matrix.

In the duration matrix, element(i,j) indicates the amount of seconds it takes
to travel from location index i to location index j. Location of vehicles and
jobs were given in the json file.

Algorithm investigates the distances between vehicles and job location first.
But it also loops over every possible vehicle-route matchings. Indexes of
vehicles were determined as [0, 1, 2] and the job locations as
[3, 4, 5, 6, 7, 8, 9]. Job index 3 asks the vehicles for who is the closest one.
When decision is done, same procedure applied for every job location. When the
shortest path will be determined, loop continues with 4, 5, 6, 7, 8, 9. This
looping creates a permutation. Number of 5040 refers to that permutation.
