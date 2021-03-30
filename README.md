# Emsi_Interview_Project

## Introduction
This project consists of a Python program that reads in a poem from a text file,
and then prompts the user to enter words that are found in one of the lines 
of the poem. The program performs a search and prints the line that best matches
the search words provided by the user.

This project folder also contains a sample poem "lepanto.txt" and a screenshot
demonstrating a successful test case for the Python program.

## Installation
This project was designed to run on Debian Buster, which already has Python installed.
Some of the packages below that the user is instructed to install may already be on the
system, if that is the case, they will receive a message saying "already installed" etc.
Thus, to install this project, perform the following steps, keeping in mind it may be
necessary to elevate to root privileges to do some of them:

1. Login to your Debian system and use the terminal to navigate to a desired folder
2. Install pip by running the following command:   sudo apt install python-pip
3. Verify installation success by checking software version with this command: pip --version
4. Install Python Regex library with the following command: pip install regex

5. Install git with the following command:   sudo apt install git
6. Verify installation success by checking software version with this command:  git --version
7. To download the project from Github, run this command: git clone https://github.com/Oobhuntoo/Emsi_Interview_Project.git
8. Navigate to the new folder called Emsi_Interview_Project, you are now ready to run the program!

## Usage
After finishing the installation process described above, the user should now be in the folder called Emsi_Interview_Project

1. Select a poem to search, there should already be one named "lepanto.txt" in the current folder. Add another poem to the current folder if needed
2. Run the following command:   python poem_search.py lepanto.txt                [ or the textfile name of some other poem ]
3. In the following prompt, enter a list of words surrounded by double quotes that are contained in a line from the poem [ example: type "Raymond gate" into prompt ]
4. After pressing ENTER, the user should now see the line from the poem that best matches the search words provided!

## Design Ideas


