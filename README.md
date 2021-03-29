# Election_Analysis

## Project Overview 
### Overview of Election Audit
The Colorado Board of Elections employee has given you the following tasks to complete the election audit of a recent local congressional election

1. Calculate the total number of votes cast
2. Get a complete list of candidates who received votes
3. Calculate the total number of votes each candidate received
4. Calculate the percentage of votes each candidate won
5. Determine the winner of the election based on popular vote

## Resources
- DataSource: election_results.csv
- Software: Python 3.9.2 , Visual Studio Code, 1.54.3

### Election-Audit Results 
The analysis of the election show that: (Include image links)
- There were "369,711" votes cast in the election.
- The candidates were:
  - Candidate 1: Charles Casper Stockham
  - Candidate 2: Diana Degette
  - Candidate 3: Raymon Anthony Doane
- The candidate results were:
  - Candidate 1 received "23.0%" of the vote and "85,213" number of votes.
  - Candidate 2 received "73.8%" of the vote and "272,892" number of votes.
  - Candidate 3 received "3.1%" of the vote and "11,606" number of votes.
- The winner of the election was:
  - Candidate 2: Diana Degette, who received "73.8%" of the vote and "272,892" number of votes.

Results are shown here:
![]Election_photos/election_terminal_results.png


## Challenge Summary
### Election Audit Summary 

In summary to the Election Audit that we have just performed, the python script provided can easily be modified for the individual who is not well versed with the python program itself in order to obtain the same results. 

On first glance such an idea might be intimidating, but with a bit of minor tweaking, the script can and will work for any election that comes about. To do this, two major items to ensure all things align is:

1. Make sure that the .csv file containing each ballot is properly formatted. The first three columns should contain the "Ballot ID, County, and Candidate" in that specific order. The code is scalable to any number of candidates and any number of counties *as long as* the .csv files follows that order of information within its columns, as you can see below:

![]Election_photos/election_ballot_format.png


2. Make sure that the .csv and .txt files are located and identified properly in order to be read and written properly.
This means that the .txt and .csv files being read and written are placed in the exact same location (with its own name) as its file matching counterparts. In other words, place the .txt file you have in the same location as the current election's .txt file, and place the .csv file in the same location as the current election's .csv file. From there, be sure to adjust the "file_to_load" and "file_to_save" files on lines 9 and 11 to match your new file names. In other words, for those more familiar with python and paths, the paths in the code (as you will see in an example) must align with the location of the reader and text files. From here, the ballot counting and the result writing will take care of itself!

The following photo shows the locations of the reader (.csv) file and the writer (.txt) file in the VS Code.
![]Election_photos/election_file_location.png

This photo is a visual of the location of the reader (.csv) file:
![]Election_photos/election_reader_location.png

This photo is another visual of the location of the writing (.txt) file:
![]Election_photos/election_writer_location.png

Below is the script used to read and write the election information that must be updated for new files. As you can see, the path reflections the locations demonstrated above. Best practice to always use the same locations for each new file of its own type and make sure those paths are always reflected in the script:
![]Election_photos/election_file_script.png

As the easiest and QUICKEST method to obtain quick reading and results of an election, this method is sure to be a promising one. 


Happy Election Counting!
