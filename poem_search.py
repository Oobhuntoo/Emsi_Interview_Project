# title: poem_search.py
# author: Matthew Mills
# date: 03/29/2021
# purpose: this program takes a poem .txt file as input, prompts the user to enter words from the poem, and then prints the line from the poem that best matches the user's input
import re
import sys

# function 'clean_list' removes punctuation from input string using regex library, returns list of words from input string
def clean_list(str_list):
    new_sublist = [ re.sub(r'[^\w\s]','',str_) for str_ in str_list.split(" ") ]
    return new_sublist

# function 'find_line' takes filename of poem and search words as input, returns line from poem that best matches search words
def find_line(filename, word_list_str):
    with open(filename, "r") as f:
        line_list = f.read().split('\n')
        line_list_copy = list(line_list)  #copy is made to preserve punctuation for return value
		
    freq_list = []
    word_list = clean_list(word_list_str)
    line_list = list(map(clean_list , line_list))
    # check to see if user input is empty or just contained punctuation symbols
    if "" in word_list:
        return "Please enter valid search words"
		
    # each line produces integer count of how many words from user input occur in it, this count is added to frequency list 'freq_list'
    for line in line_list:
        count = 0
        for word in word_list:
            if word in line:
                count += 1
        freq_list.append(count)
   
    # index of line with most words from user input found via max function, used to return corresponding line from the copy of the poem's text which still has punctuation symbols
    max_freq = max(freq_list)
    max_idx = freq_list.index(max_freq)
    return line_list_copy[max_idx]      

if __name__ == "__main__":
    poem_file = sys.argv[1]
    search_words = input()
    line_ = find_line(poem_file, search_words)
    print(line_)  