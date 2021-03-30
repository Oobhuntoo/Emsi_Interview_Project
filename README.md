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
The main idea behind this project is that a user enters one or more words supposedly from the given poem, and then the program returns
the line from the poem that contains those words. The filename of the poem is passed to the Python program as an argument through argv.
The lines of the poem are read in from the file, and for each line, the program checks to see if each word from the user input is in the line.
Then, for each line, a sum is created that equals the number of search words which occur in that line, and it is appended to a list called frequency_list.
Thus, the ith element of freq_list is the number of search words from the user input that occurs in the ith line of the poem. The maximum value of frequency_list
is found, and the line of the poem that it corresponds to is printed.

Now, what happens if a user enters two words from line 12 and two words from line 45?
Should the program return both lines 12 and 45, or should it return just one of them? The goal of this project is to help the customer
identify the line they are remembering from the poem, so I believe it is more helpful to return multiple lines if the user remembered 
the same number of words from each. The program does this by returning a list of lines which contain the same number of words in the user input.
This list is formed via Python's conditional list comprehension feature to identify the lines whose frequency count is equal to the max frequency
count of words from the user input.

Another potential issue that could arise is if the user enters a word such as "house", but in the poem, it is represented adjacent to a punctuation
symbol, such as "house!" The lines of the poem are broken into lists of words, to ensure that a given search word actually occurs in the line,
and is not just a substring of another word. Thus, the program could not detect the word "house" in the list of words of a line, if it is written as
"house!" in the poem, since the words of the line are delimited by space via Python's split function. To solve this problem, I chose to use the Python
regex library to go through each word in the user input and each word of each line of the poem and remove punctuation symbols. This guarantees that only
alphanumeric characters are being compared during the search process.
Here is the documentation for the regex library: https://docs.python.org/3/library/re.html
In the source code, on Line 10, punctuation symbols are identified and replaced with the empty string using regular expression syntax [^\w\s]. the '^' characters
means 'exclude' and the '\s' character means any UNICODE char usually in strings i.e. alphanumeric, and the '\w' means whitespace characters.
Thus, this command detects any non-alphanumeric character i.e. punctuation and replaces it with the empty string. That is how punctuation symbols are removed
from all words in the user input and poem file. However, before these symbols are removed, a copy of the poem is made and it the corresponding lines
from this copy are what actually get returned, so that the user can see the original punctuation from the poem.
