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

def findIPInFile(lineNum, f, oldTime):
    newTime = oldTime # newTime is the most recent time found. Δt will be
                      # found with: newTime-oldTime
    f.seek(line_offset[lineNum]) # Seek to specific line number
    line = f.readline()
    ip = line[23:line[23].index(",")] # Retrieve this line's IP address
    while (strptime(line[:23], "%b/%d/%y,%I:%M:%S%p") - oldTime <= 15 minutes):
        if line[23:line[23].index(",")] == ip:
            newTime = strptime(line[:23], "%b/%d/%y,%I:%M:%S%p")
            # Can't delete line because that would require rebuilding line_offset
    return newTime

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

#################From StackOverflow#########################
# Read in the file once and build a list of line offsets
line_offset = []
offset = 0
for line in f:
    line_offset.append(offset)
    offset += len(line)
f.seek(0)

# Now, skip to first line.
f.seek(line_offset[0])
#################End StackOverflow Code#####################


lineNum = 0 # Count lines to get the current line number
for line in f: # Iterate over all lines in CSV

    i = line[23:line[23].index(",")])
    if (i): # Search array for IP Address
        # Time is saved in this format: XX Month/XX Day/XXXX Year,Hour (12):
        # Min:Sec(pm/am)
        currentTime = user_total_time[i][1]
        newTime = strptime(line[:23], "%b/%d/%y,%I:%M:%S%p")


    lineNum++ #increment to new line number.
# End of Loop
