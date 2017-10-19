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

def findIPInFile(lineNum, line_offset, f, oldTime):
    newTime = oldTime # newTime is the most recent time found.
    f.seek(line_offset[lineNum]) # Seek to specific line number.
    line = f.readline()
    ip = line[23:line[23].index(",")] # Retrieve this line's IP address.






    
    # Move to the next line in the file.
    f.seek(line_offset[lineNum + 1])
    line = f.readline()
    while (time.mktime(strptime(line[:23], "%b/%d/%y,%I:%M:%S%p")) - time.mktime(oldTime) <= 900) && (line[23:line[23].index(",")] == ip): # 900 seconds is fifteen minutes, and time.mktime outputs seconds since epoch
        # If it has been more than 15 minutes, consider it a new session.
        if (line[23:line[23].index(",")] == ip) and (!(ip in ipDict) or (oldTime - ipDict[ip] > 15 minutes)):
            newTime = strptime(line[:23], "%b/%d/%y,%I:%M:%S%p") # Update most recent time
            ipDict[ip] = newTime; # Add new key to dictionary or replace old value
    return newTime
# End findIPInFile

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
totalTime = 0; # totalTime/totalSessions = average session time.
totalSessions = 0;
for line in f: # Iterate over all lines in CSV
    if line[0] != 'z': # A Z is added to the beginning of every line that's already counted.
        currentTime = strptime(line[:23], "%b/%d/%y,%I:%M:%S%p")
        newTime = findIPInFile(linenum, line_offset, f, currentTime)



    lineNum = linenum + 1 #increment to new line number.
# End of Loop
