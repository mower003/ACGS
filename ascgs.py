#! python3

import subprocess
import sys

#Automated Street Coordinate Gathering Script
#=================================================================IMPORTANT!!=====================================================================
#Users MUST install miniconda, osmnx, and papermill + their dependencies for the program to work.
#A description and links of the installation are provided on GitHub.
#You must also have the accompanying file 'osmnxgetcoords.ipynb' and reference it appropriately in the cmdString below.
#using jupyter-client 6.1.9 (most recent), and most recent install of papermill. However, because of something with asnycio within the 
# /tornado/platform (part of jupyter notebook)
#the python file asyncio.py located in 'miniconda3\envs\ox\Lib\site-packages\tornado\platform' had to be altered with the insertion of the following line:
#if sys.platform == 'win32':
#    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy()) 
#located just after the main imports.
#=================================================================IMPORTANT!!=====================================================================
#Takes input from a user in the form of city,state,country
#Passes that input into a miniconda3 virtual environment where osmNX and Papermill are installed
#This runs a Jupyter Notebook that queries OpenStreetMaps for the coordinates of all the streets within the queried city.
#Output of the script produces a folder on users Desktop called 'osmnxOutputFiles'
#This folder contains a JSON file with all the street names and their coordinates, a png of the street network, and any cached files from osmNX.
#=================================================================================================================================================
#used conda install papermill so that I could execute .ipynb files with parameters (used to pass city,state,country to osmnxcoords.ipynb)
#project dependencies so far include: Miniconda, Jupyter Notebook, osmNX, and Papermill
#https://geoffboeing.com/2017/02/python-getting-started/ 
#https://docs.conda.io/en/latest/miniconda.html
#https://github.com/nteract/papermill
#===================================================================NOTES=========================================================================
#It is possible for execution to timeout or for the notebook to fail when retrieving Shapely data.
#I am unable to reliably reproduce the error but clearing the OSMNX cache files, and retrying the query has seemed to work in most cases.

def cleanAndRun(args):

    city = args[0].title().strip()
    state = args[1].title().strip()
    country = args[2].upper().strip()

    cmdString = 'conda activate ox && papermill C://Users/User/osmnxgetcoords.ipynb C://Users/User/osmnxgetcoordsout.ipynb -p city ' + city + ' -p state ' + state + ' -p country ' + country + ' && conda deactivate'
    try:
        print("Running Program using" + city + " " + state + " " + country)
        subprocess.run(cmdString, shell=True)
    except:
        print("An error has occured. Try again or re-run the script.")

def runWithCommandLineArguments():
    if len(sys.argv) < 4 or len(sys.argv) > 4:
        print("Invalid number of command line inputs. Accepted format: py ascgs.py city state country. If your arguments contain spaces please use py ascgs.py \"San Marcos\" \"California\" \"USA\"")
    else:
        arguments = sys.argv[1:]
        cleanAndRun(arguments)
        
def runWithoutCommandLineArguments():
    while True:
        location = input("Enter a city name to query in for format of: City, State, Country e.g. Carlsbad, California, USA:   ")
        locationList = location.split(",")
        if len(locationList) == 3:
            break
        else:
            print("Invalid input declaration! Enter a city name to query in for format of: City, State, Country.")

    cleanAndRun(locationList)

if len(sys.argv) > 1:
    runWithCommandLineArguments()
else:
    runWithoutCommandLineArguments()


