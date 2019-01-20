**********************************************************************
		TRIANGULATIONS GENERATOR
		
	Author: Emilija Zdilar
	Version: 1.0.0
	Date: 24.01.2018.

	This project is a Computational Geometry course assignment, 
	written in Python. It is a recursive algorithm that, for a 
	given simple polygon, calculates all triangulations and saves
	them as images to output folder.
  
**********************************************************************

Getting Started:

- Download and open project
- Create and activate virtual environment, as per your preference.
- pip install -r requirements.txt
- Open MySQL and create database schema triangulation;
- Import triangulation.sql
- set username and password in utils/constants.py
- Navigate to project root folder
- python main.py

**********************************************************************

Tips:
- The number of possible triangulations for a n-sided simple polygon
  is given by Catalan number C<sub>n-2</sub>. Hence, the algorithm
  finishes in a reasonable amount of time for small inputs.
- In-depth explanation is found in .pdf file
  
 
 Example of the decagon triangulations: 
  
<img src="results/n=10.gif" width="300">

**********************************************************************

Prerequisites:
- MySQL 8.0.13
- Python 3.6.5
- Peewee 3.8.2
- Pillow 5.4.1

**********************************************************************

Acknowledgments:
- Paško Zdilar

**********************************************************************
