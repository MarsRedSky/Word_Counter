import re, csv, argparse

def counts_words(dyad, master_l, jeff):
    # recieves dyad from argparse
    # opens dyad as file
    # deletes comments in dyad
    text = comment_deleter(open_file(dyad))
    # opens master list
    ml = open_file(master_l)
    #checks for jeffersonian
    if args.j:
        # clean to jeff specifications
        text = clean_jeff(text)
        # mark overlaps and elongations
        step = polish_jeff(text, ml)
        #seperate input from wanted
        input = step[0]
        wanted = step[1]
    else:
        # clean to nonjeff specifications
        input = clean(text)
        wanted = ml
    # counts words
    # sends results to csv writer
    csver(word_counter(input,wanted),dyad)



    # csver(final_count(word_counter(input), clean_jeff(wanted)),dyad)

def open_file(dyad):
    #opens file, reads and lowers
    with open(dyad, "r") as file:
        file = file.read().lower()
    return file

def comment_deleter(file):
    # delete comments surrounded by []
    file = re.sub("[\[].*?[\]]", " ", file)
    # delete comments surrounded by ()
    file = re.sub("[\(].*?[\)]", " ", file)
    return file

def clean(text):
    # deletes undesired characters
    text_1 = text.replace("*", "").replace(":", "").replace("?", "").replace(".", "").replace("\xe2\x80\x99", "'")
    return text_1

def clean_jeff(text):
    # deletes undesired characters
    # leaves characters important to Jeffersonian conventions
    text_1 = text.replace("?", "").replace(".", "").replace("\xe2\x80\x99", "'")
    return text_1

def polish_jeff(text,master_list):
    # checks input words for overlap and elongation
    # adds equivalent to wanted
    ls = text.split()
    ls_2 = master_list.split()
    ls_1 = []
    text_1 = ""
    text_2 = ""
    overlap = 0
    # handles words with * and :
    for word in ls:
        if word.startswith("*") and word.endswith("*") ==0:
            x = word[1:]
            x_1 = x.replace(":", "")
            word = "*"+x+"*"
            ls_1.append(word)
            overlap = 1
            if x_1 in ls_2 and word not in ls_2:
                ls_2.append(word)
        elif word.endswith("*") and word.startswith("*") ==0:
            x = word[:-1]
            x_1 = x.replace(":","")
            word = "*"+x+"*"
            ls_1.append(word)
            overlap = 0
            if x_1 in ls_2 and word not in ls_2:
                ls_2.append(word)
        elif overlap == 1:
            x = word
            x_1 = x.replace(":","")
            if x_1 in ls_2 and word not in ls_2:
                ls_2.append(word)
            word = "*"+x+"*"
            ls_1.append(word)
            if x in ls_2 and word not in ls_2:
                ls_2.append(word)
        elif word.startswith("*") and word.endswith("*"):
            x = word[1:-1]
            x_1 = x.replace(":","")
            word = "*"+x+"*"
            ls_1.append(word)
            if x_1 in ls_2 and word not in ls_2:
                ls_2.append(word)
        else:
            x = word
            x_1 = x.replace(":","")
            if x_1 in ls_2 and word not in ls_2:
                ls_1.append(word)
                ls_2.append(word)
            else:
                ls_1.append(word)
    for word in ls_1:
        text_1 += word + " "
    for word_1 in ls_2:
        text_2+= word_1 +" "

    return text_1, text_2

def word_counter(text,wanted):
    # counts occurences of words in input
    # increases count of wanted dict
    dict = {}
    input = text.split()
    wanted = wanted.split()
    for target in wanted:
        dict[target] = 0
    for word in input:
        if word in dict:
            dict[word]+=1
    # "alphabetical" results
    results = sorted(list(dict.items()))
    return results

def csver(data,filename):
    # creates csv file named after dyad
    csv_file = filename+".csv"
    with open(csv_file, "w") as csv_file:
        fieldnames = ["word", "occurrences"]
        writer  = csv.writer(csv_file)
        writer.writerow(fieldnames)
        # writes rows of word and occurences
        for row in data:
            writer.writerow(row)

parser = argparse.ArgumentParser()
parser.add_argument('filename')
parser.add_argument('-j', action='store_true')
args = parser.parse_args()
counts_words(args.filename,"master_list",args.j)


