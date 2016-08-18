import re 
from collections import Counter
import csv

from sys import argv

script, filename = argv

#opens file entered by user

file_1 = open(filename , "r" )

text = file_1.read().lower()
file_1.close()

# replaces every character that isn't a-z, 0-9, -, :, ?, 'or * with a space

#print text 


text = re.sub("[^a-z 0-9 \-  \:  \?  \' \*\‘ ]+", " ", text)

#print text

# puts dyad words on file in a list 

#input = text.split()

input = list(text.split())

#print input 


#opens master list

file = open ("master_list.txt" , "r")
master = file.read().lower()
file.close()

master = re.sub("[^a-z 0-9 \-  \:  \?  \' \*\ ]+", " ", master)


#adds master list to a list

wanted = list(master.split())


#counts occurrences of the master list words in dyad words 

cnt = Counter()

for item_wanted in wanted:
	cnt [item_wanted] = 0	
	for input_item in input: 
		
		if item_wanted == input_item: 
			cnt[item_wanted] += 1 

print cnt



#write to CSV 
   
with open("dyad_data.csv","wb") as csvfile:
    fieldnames=["word","occurrences"] 
    writer=csv.writer(csvfile)
    writer.writerow(fieldnames)
    
    for key, value in cnt.items():
        writer.writerow([key] + [value]) 
