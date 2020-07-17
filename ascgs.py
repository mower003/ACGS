#! python3

import subprocess

#Automated Street Coordinate Gathering Script
#=================================================================IMPORTANT!!=====================================================================
#Users MUST install miniconda, osmnx, and papermill + their dependencies for the program to work.
#A description and links of the installation are provided on GitHub.
#You must also have the accompanying file 'osmnxgetcoords.ipynb' and reference it appropriately in the cmdString below.
#using jupyter-client 6.1.3 (most recent), and most recent install of papermil. However, because of something with asnycio within the 
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


location = input("Enter a city name to query in for format of: City, State, Country e.g. Carlsbad, California, USA:   ")
locationList = location.split(",")
city = locationList[0].title().strip()
state = locationList[1].title().strip()
country = locationList[2].upper().strip()

cmdString = 'conda activate ox && papermill C://Users/User/osmnxgetcoords.ipynb C://Users/User/osmnxgetcoordsout.ipynb -p city ' + city + ' -p state ' + state + ' -p country ' + country + ' && conda deactivate'

subprocess.run(cmdString, shell=True)

