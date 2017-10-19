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
import urllib.request # To download CSV files from our webserver.

elapsed_time = time.clock()

# findIPInFile finds the last entry for this user session, and returns the time the entry was created.
def findIPInFile(lineNum, lines, oldTime):
    newTime = oldTime # newTime is the most recent time found.
    line = lines[lineNum]
    ip = line[21:line[21].index(",")] # Retrieve this line's IP address.

    while lineNum < len(lines):
        line = lines[lineNum]
        if line[0] != 'z':
            # If it has been more than 15 minutes, exit the loop (session has ended already).
            # 900 seconds is fifteen minutes, and time.mktime outputs seconds since epoch.
            if time.mktime(time.strptime(line[:21], "%m/%d/%Y,%I:%M:%S%p")) - time.mktime(newTime) <= 900:
                if line[21:line[21].index(",")] == ip: # Check that current line is an entry for the current IP.
                    newTime = time.strptime(line[:21], "%m/%d/%Y,%I:%M:%S%p") # Update most recent time.
                    lines[lineNum] = 'z' # Mark that this line has been counted already.
            else:
                break
        lineNum = lineNum + 1 # Select the next line.
    return time.mktime(newTime)
# End of findIPInFile.

# downloadCSV downloads the most current data.csv file from our webserver.
def downloadCSV():
    url = "http://carbon.campusops.oregonstate.edu/php/data.csv"
    urllib.request.urlretrieve(url, "data.csv")
# End downloadCSV

def main():
    print("Welcome to Jack's Average Session Time Calculator!\n")

    filename = ""

    if len(sys.argv) == 1:
        print("Remember: You can enter a custom filename using a command line\n")
        print("          argument. IE: python3 avg_carbon_calc_user_time data.csv\n")
        print("Since no file was specified, the default data.csv will be downloaded and used.\n")
        filename = "data.csv"
    else:
        filename = sys.argv[1]

    downloadCSV()

    f = open(filename, 'r') # Open data file for reading.
    lines = f.readlines() # Save CSV in memory.
    f.close() # Close file.


    lineNum = 0 # Count lines to get the current line number
    totalTime = 0; # totalTime/totalSessions = average session time.
    totalSessions = 0;
    for i in range(0, len(lines)): # Iterate over all lines in CSV
        if lines[i][0] != 'z' and lines[i][0] != '\n': # A Z is added to the beginning of every line that's already counted.
            line = lines[i]
            currentTime = time.strptime(line[:21], "%m/%d/%Y,%I:%M:%S%p")
            newTime = findIPInFile(i, lines, currentTime)
            totalSessions = totalSessions + 1
            totalTime = totalTime + (newTime-time.mktime(currentTime))
        lineNum = lineNum + 1 #increment to new line number.
    # End of Loop.
    print("The average session time is " + str(totalTime/totalSessions/60) + " minutes per session.") # Divide by 60 to convert seconds to minutes.
# End of main.
main() # Call main function.
