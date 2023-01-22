import os
import csv
csvpath=os.path.join("Resources","election_data.csv")
output_file = os.path.join("analysis","election_analysis.txt")
with open(output_file, "w") as txt_file:
    with open (csvpath) as csvfile:
        csv_reader=csv.reader(csvfile,delimiter=',')
        csv_header=next(csv_reader)
        str1="election analysis\n"
        print(str1)
        txt_file.write(str1)
        str2=("------------------\n")
        print(str2)
        txt_file.write(str2)
        total_votes=0
        candidates_list = []
        votes_dict={}
        votes2 = 0
        votes_count=[]

        for row in csv_reader:
            total_votes+=1
            candidate=(str(row[2]))
            if candidate not in candidates_list:
                candidates_list.append(candidate)
                votes_dict[candidate]=0
            votes_dict[candidate]+=1
        print(total_votes)
        
        txt_file.write(str(total_votes))
        txt_file.write("\n")
        print('------------------')
        txt_file.write(str2)

        for candidate in votes_dict:
            votes = votes_dict.get(candidate)
            vote_percentage = (votes/total_votes)*100
            candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
            print(candidate_results)
            txt_file.write(candidate_results)
            votes_count.append(votes)

        
        winner_val=max(votes_count)
        winner_index=votes_count.index(winner_val)
        
        txt_file.write(str2)
        print('------------------')
        final_winner=(f'The winner is {candidates_list[winner_index]}')
        print(final_winner)
        txt_file.write(final_winner)



        