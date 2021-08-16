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
