## A new Simple version for Python 3.x is available. Please try it first if you have Python 3.x
#Prerequisites
Python 3.x (download from https://www.python.org/)
Pandas library: Install using pip at terminal/command prompt
            

#####   SYSTEM REQUIREMENTS  #####

# Requires Python 3.x (download from https://www.python.org/)

# Required Libraries : pandas Install using Command (pip install pandas)
Standard libraries like datetime, os, and zipfile are part of Python, so no additional installation is required.

#Visual Studio Code  

# internet connection

##### FILES INCLUDED #####

#attendance_summary.py: The main script to process CSV files and generate the report.

#attendance_dummy_data.zip: The ZIP file containing the attendance CSV files.

#README.txt: This file.


##### INSTUCTION FOR USE #####

1.ZIP File Extraction: The script will extract the CSV files from the ZIP archive specified in the zip_path variable. By default, this path is set to: C:/Users/User/source/repos/CE2709/miniProject/attendance_dummy_data.zip

2.Running the Script: To run the script, open a terminal/command prompt, navigate to the project directory, and execute: python attendance_summary.py

3.Attendance Processing: The script will:
  #Extract the CSV files into the attendance_data folder.
  #Read and process the CSV files.
  #Generate a report summarizing the number of attended, absent, and late sessions for each student.

4.Configuring Class Time and Late Threshold: You can configure the class start time, end time, and the threshold for marking a student as late by modifying the following variables in the main() function:
class_start = time(9, 0)  # Class starts at 9:00 AM
class_end = time(10, 30)  # Class ends at 10:30 AM
late_threshold = time(9, 10)  # Mark late if joined after 9:10 AM

5.Generated Report: The report will be generated as attendance_summary_report.csv in the current directory. It contains the following columns:
#Student Name: The name of the student.
#ID/E-mail: The student’s email or ID.
#Attended Sessions: Number of sessions attended.
#Absent Sessions: Number of sessions missed.
#Late Sessions: Number of sessions where the student was late.


##### ERROR HANDLING #####

#PermissionError: If the script encounters a permission error when generating the report, it will output the error message.

#General Errors: Any other exceptions that occur during report generation will be printed to the console.



