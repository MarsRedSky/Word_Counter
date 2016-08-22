import re 
from collections import Counter
import csv

from sys import argv

script, filename = argv


print "Would you like a Jeffersonian analysis? \n Type 1 for yes. \n Type 2  for no."
jeff = int(raw_input())


#opens file entered by user


file_1 = open(filename , "r" )

#cleans file, eliminates unwanted punctuation 
#eliminates text within brackets or parenthesis 
#including the brackets or parathesis

text = file_1.read().lower().replace("?","").replace(".","")
text = re.sub("[\[].*?[\]]","", text)
text = re.sub("[\(].*?[\)]","",text)

if jeff != 1: 
	text= text.replace("*","").replace(":","")



file_1.close()


# puts dyad words on file in a list 

input = text.split()


#replaces educated apostrophe with straight apostrophe

i_list = []

for i in input:
	i_list.append(i.replace("\xe2\x80\x99","'"))

input = i_list
 



#opens master list

file = open ("master_list.txt" , "r")
master = file.read().lower()
file.close()



#adds master list to a list

wanted = master.split()

# replaces educated apostrophe with straight apostrophe

w_list = []

for w in wanted:
	w_list.append(w.replace("\xe2\x80\x99","'"))

wanted = w_list



#counts occurrences of the master list words in dyad words 

cnt = Counter()

for item_wanted in wanted:
	cnt [item_wanted] = 0	
	for input_item in input: 
		
		if item_wanted == input_item: 
			cnt[item_wanted] += 1 

print cnt



#write to CSV 
   
csver = filename.replace(".txt",".csv")

with open(csver,"wb") as csvfile:
    fieldnames=["word","occurrences"] 
    writer=csv.writer(csvfile)
    writer.writerow(fieldnames)
    
    for key, value in cnt.items():
        writer.writerow([key] + [value]) 
