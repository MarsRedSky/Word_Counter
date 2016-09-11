import re
from collections import Counter
import csv
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('filename') 
parser.add_argument('-j', action='store_true')
args = parser.parse_args()

file = open(args.filename, 'r') 
file = file.read().lower()

#deletes comments from dyads
file = re.sub("[\[].*?[\]]"," ", file)
file = re.sub("[\(].*?[\)]"," ", file)

#Jeffersonian 
if args.j:	
	text = file.replace("?","").replace(".","")
	print text

#non-Jeffersonian
else:
	#deletes text surrounded by *s
	file = re.sub("[\*].*?[\*]", "", file)
	text = file.replace("*","").replace(":","").replace("?","").replace(".","")
	print text



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

csver = args.filename.replace(".txt",".csv")

with open(csver,"wb") as csvfile:
    fieldnames=["word","occurrences"]
    writer=csv.writer(csvfile)
    writer.writerow(fieldnames)

    for key, value in cnt.items():
        writer.writerow([key] + [value])
