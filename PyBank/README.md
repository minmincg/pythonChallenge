# Pybank
First I imported the necessary files to be able to open the csv file and write the output in a txt file. I created the path to read csv file with data and wrote the output path to print output in a txt file.

I used next function to skip first row that contained header and shouldn't be considered for the analysis, just as reference as to what I'm analysing
.<img width="437" alt="Screenshot 2023-01-22 at 16 55 40" src="https://user-images.githubusercontent.com/64171430/213944800-8f7264d0-87a2-4fd9-bbe7-4f7f2356e095.png">

Then I declared various variables that I'll explain to you as I explain the funcionality of each one, so you can skip or ignore them for now...

<img width="232" alt="Screenshot 2023-01-22 at 16 56 53" src="https://user-images.githubusercontent.com/64171430/213944852-c78b3ff6-605d-48f5-98ec-02795746c5be.png">

I created a for loop to iterate through each of the rows in the csv file.
In each iteration:
  1.-we add one to the total months counter amount_mon (basically just count how many rows you have in the csv file.
  2.- Created a profits list to be able to use the sum function later on. I just appended whatever value it had in each of the rows in index 1
  3.- I declared a variable = this_month which would store and keep the value of this row's profit to be used later on in the next iteration last month starts with the INITIAL value of the index 1 before the iteration starts so that it can be used in the first iteration as well. (So the first change in profit would be zero)
  4.-the changes_list uses this month's profit and subtracts it to last month's profit value. ( In the first iteration last month's value starts being the same value as this month's value so the answer to the first change will ALWAYS be zero. 
  5.- At the end of the iteration we store this month's value in last month's value to be able to subtract it to the next iteration's "This month's value"
  <img width="398" alt="Screenshot 2023-01-22 at 17 04 43" src="https://user-images.githubusercontent.com/64171430/213945171-2dfb308c-3f68-41df-86f5-7901553f4b8e.png">

  6.- Closed the for loop
  7.- used mathematical built in functions to obtain the different values I was asked. I subtracted minus 1 to the amount of months I used to calculate percentage since there was no value for the first iteration of CHANGE ( as we stated in ponit number 4, the first value of change will be zero by default.
  
  <img width="323" alt="Screenshot 2023-01-22 at 17 05 27" src="https://user-images.githubusercontent.com/64171430/213945213-4bf1b622-6dc0-45f3-8c98-c197f3d3315d.png">
  8.- I used the .index function to relate whatever the maximum value was (obtained with max built in function) with the month it corresponded to (month_ list was a list created with just the "month's column" by appending all of the string values in row[0]) and stored it in a variable to be used later on when I printed the maximum value with its corresponding month
<img width="289" alt="Screenshot 2023-01-22 at 17 09 41" src="https://user-images.githubusercontent.com/64171430/213945373-a06676da-f4b2-427e-87ac-45033fd599fe.png">
