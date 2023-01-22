import os
import csv

csvpath = os.path.join("Resources","budget_data.csv")
output_file = os.path.join("analysis","election_analysis.txt")
with open(output_file, "w") as txt_file:

    with open(csvpath) as csvfile:
        csv_reader=csv.reader(csvfile, delimiter = ',')

        csv_header=next(csv_reader)
        amount_mon=1
        first_row=next(csv_reader)
        this_month=0
        last_month=float(first_row[1])
        profits_list=[float(first_row[1])]
        changes_list=[]
        month_list=[]

        for row in csv_reader:
            amount_mon+=1
            profits_list.append(float(row[1]))
            this_month=(float(row[1]))
            changes_list.append((this_month)-(last_month))
            month_list.append(row[0])
            last_month=this_month
            
        total=sum(profits_list)
        average=(sum(changes_list)/(amount_mon-1))
        max_val=max(changes_list) 
        min_val=min(changes_list)

        max_index= changes_list.index(max_val)
        min_index= changes_list.index(min_val)

       
        str1=('Financial Analysis\n')
        print(str1)
        txt_file.write(str1)
        str2=("------------------\n")
        print(str2)
        txt_file.write(str2)
        str3=(f'Total months: {amount_mon}\n')
        print(str3)
        txt_file.write(str3)
        str4=(f'Total net profit: {total}\n')
        print(str4)
        txt_file.write(str4)
        str5=(f'Average change: {average}\n')
        print(str5)
        txt_file.write(str5)
        str6=(f'Greatest increase in profits: {month_list[max_index]} {max_val}\n')
        print(str6)
        txt_file.write(str6)
        str7=(f'Greatest decrease in profits: {month_list[min_index]} {min_val}\n')
        print(str7)
        txt_file.write(str7)

    



    


    


   
    