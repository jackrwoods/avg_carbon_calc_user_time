##****************************************************************************##
## Program Filename: avg_carbon_calc_user_time.py
## Author: Jack Woods
## Date: 10.10.17
## Description: Parse user data from CSV and calculate the average time a user
##              spends on the calculator.
## How To Run: Execute the application with a file name as an argument
##****************************************************************************##

import sys # To access command line arguments.
import time # To calculate elapsed time during calculation, and conversions.

elapsed_time = time.clock()

print("Welcome to Jack's Average Session Time Calculator!\n")

filename = ""

if len(sys.argv) == 1:
    print("Remember: You can enter a custom filename using a command line\n")
    print("          argument. IE: python3 avg_carbon_calc_user_time data.csv\n")
    print("Since no file was specified, the default data.csv will be used.\n")
    filename = "data.csv"
else:
    filename = sys.argv[1]

f = open(filename, r) # Open data file for reading.

# A user is assumed to be 1 IP Address. This will be optimized later for
# increased accuracy.

# The script iterates over every IP address in the list. For each IP address
# found, a new entry is made in a 2-D array, user_total_time.

# user_total_time contains a running total of each user's time spent on the
# Carbon Calculator, and the most recent data/time the user accessed the
# Carbon Calculator.
user_total_time = [][] # Create empty list array.

for line in f:
    if user_total_time.index(line[23:line[23].index(",")]): # Search array for
        # Inside Loop                                       # IP Address
    # Time is saved in this format: XX Month/XX Day/XXXX Year,Hour (12):Min:Sec(pm/am)
    time.strptime(line[:23], "%b/%d/%y,%I:%M:%S%p")
    if
