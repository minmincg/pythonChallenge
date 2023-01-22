First I imported the necessary files to be able to open the csv file and write the output in a txt file.
I created the path to read csv file with data and wrote the output path to print output in a txt file. 

I used next function to skip first row that contained header and shouldn't be considered for the analysis, just as reference as to what I'm analysing.

<img width="571" alt="Screenshot 2023-01-22 at 16 23 40" src="https://user-images.githubusercontent.com/64171430/213943559-8e857a84-3660-4e7a-afdc-d5bb893b233a.png">
Then, theres various variables, lists and dictionaries declared on top, you may skip them for now... I'll explain step by step why I used each of them.
<img width="388" alt="Screenshot 2023-01-22 at 16 25 19" src="https://user-images.githubusercontent.com/64171430/213943637-dd873d59-32d0-4a7c-968c-617296f5849d.png">

I started iterating through each of the data rows with a for loop
Every time the iterator does a loop:
  1.- it adds 1 to the rows counter(how many total votes there are independently of who they voted for)
  2.-I declared the value candidate that was in index 3 of each row.
  3.-I added a conditional where if the candidate variable was not already in the candidates_list (which would be my summary dictionary later on) it would append it to the list (so the candidates_list in this case ended up being charles casper, diana degette and raymon anthony.
  4.-then I started my summary dictionary 
  5.- after the conditional it would add to the counter if it was a vote for diana, raymond, or charles, depending on the candidate variable that it had stored for each iteration in the previous conditional. finished the loop
  6.- Next I did another for loop to go through my different candidates in candidates_dictionary ("summary table")
  7.-  I got the counter for each candidate, I got the percentage relative to the total votes.
  8.- I printed out how many votes for each candidate and what percentage relative to the total votes.
  9.-Appended VOTES to a different list to be able to run the max function and know who was the winner.
  10.- Used .index to see what candidate corresponded to this said winning value (max value)
  11.- printed out missing information. 

  <img width="525" alt="Screenshot 2023-01-22 at 16 41 15" src="https://user-images.githubusercontent.com/64171430/213944224-90b28b43-5c13-49d6-9c80-ba0c9dea50e5.png">
