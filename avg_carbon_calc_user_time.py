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

# findIPInFile finds the last entry for this user session, and returns the time the entry was created.
def findIPInFile(lineNum, lines, oldTime):
    newTime = oldTime # newTime is the most recent time found.
    ip = lines[lineNum][23:line[23].index(",")] # Retrieve this line's IP address.

    while lineNum < len(lines):
        if line[0] != 'z':
            # If it has been more than 15 minutes, exit the loop (session has ended already).
            if time.mktime(strptime(line[:23], "%b/%d/%y,%I:%M:%S%p")) - time.mktime(newTime) <= 900): # 900 seconds is fifteen minutes, and time.mktime outputs seconds since epoch.
                if line[23:line[23].index(",")] == ip: # Check that current line is an entry for the current IP.
                    newTime = strptime(line[:23], "%b/%d/%y,%I:%M:%S%p") # Update most recent time.
                    line[lineNum][0] = 'z' # Mark that this line has been counted already.
            else:
                break
        lineNum = lineNum + 1 # Select the next line.
    return newTime
# End of findIPInFile.

def main():
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
    lines = f.readlines() # Save CSV in memory.
    f.close() # Close file.


    lineNum = 0 # Count lines to get the current line number
    totalTime = 0; # totalTime/totalSessions = average session time.
    totalSessions = 0;
    for i in range(0, len(lines)): # Iterate over all lines in CSV
        if lines[i][0] != 'z': # A Z is added to the beginning of every line that's already counted.
            currentTime = strptime(line[:23], "%b/%d/%y,%I:%M:%S%p")
            newTime = findIPInFile(i, lines, currentTime)
            totalSessions = totalSessions + 1
            totalTime = totalTime + (newTime-oldTime)
        lineNum = linenum + 1 #increment to new line number.
    # End of Loop.

    print("The average session time is " + (totalTime/totalSessions/60) + " minutes per session.") # Divide by 60 to convert seconds to minutes.
# End of main.
main() # Call main function.
