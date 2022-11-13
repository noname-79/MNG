import re
import csv
tab = [[],[],[],[],[],[],[]]
# tab[0] = no
# tab[1] = vol
# tab[2] = article_no
# tab[3] = pages_in_range
# tab[4] = publisher_location
# tab[5] = publisher_year
# tab[6] = publisher_name
def complement_data(data:object) -> str:
    if data == None:
        return " "
    else:
        return data.group()

def no(row:list):
    for dane in row:
        x = re.search("((nr|Nr)|(no|No)|(iss)\.\s(?P<s>\d{1,3}))", dane)
        tab[0].append(complement_data(x))

    buffer = tab[0].copy()
    tab[0].clear()
    for dane in buffer:
        y = re.search("\d{1,3}",dane)
        tab[0].append(complement_data(y))
    buffer.clear()

def vol(row:list):
    for dane in row:

        x = re.search("((vol|Vol)\.\s(?P<vol>\d{1,3}))", dane)
        tab[1].append(complement_data(x))

    buffer = tab[1].copy()
    tab[1].clear()
    for dane in buffer:
        y = re.search("\d{1,3}",dane)
        tab[1].append(complement_data(y))
    buffer.clear()

def article_no(row:list):
    for dane in row:
        x = re.search("((art)\.\s(?P<s>e\d{1,5}))", dane)
        tab[2].append(complement_data(x))

def pages_in_range(row:list):
    for dane in row:
        x = re.search("(?P<pages>(S\.|s\.)\s\d{1,5}[-]\d{1,5})", dane)
        tab[3].append(complement_data(x))

    buffer = tab[3].copy()
    tab[3].clear()
    for dane in buffer:
        y = re.search("\d{1,5}[-]\d{1,5}", dane)
        tab[3].append(complement_data(y))
    buffer.clear()

def publisher_location(row:list):
    for dane in row:
        x = re.search("(?P<city>[a-zA-Z-żźćńółęąśŻŹĆĄŚĘŁÓŃ]+\s:)", dane)
        tab[4].append(complement_data(x))

def publisher_year(row:list):
    for dane in row:
        x = re.search("(?P<year>\d{4})", dane) #+
        tab[5].append(complement_data(x))

def publisher_name(row:list):
    for dane in row:
        x = re.search("((?P<name>[a-zA-Z-żźćńółęąśŻŹĆĄŚĘŁÓŃ]+\s)*[a-zA-Z-żźćńółęąśŻŹĆĄŚĘŁÓŃ]+,)", dane)
        tab[6].append(complement_data(x))

row0 = []
row1 = []
with open('details.csv', 'r', encoding="utf8") as file:
    reader = csv.reader(file)
    for rows in reader:
        row0.append(rows[0])
        row1.append(rows[1])

no(row1)
vol(row1)
article_no(row1)
pages_in_range(row1)
publisher_name(row0)
publisher_year(row0)
publisher_location(row0)

with open("new.csv","w",encoding="utf8",newline="\n") as file:
    file.write("no" + "$" + "vol" + "$" + "article_no" + "$" + "pages_in_range" + "$" + "publisher_name" + "$" + "publisher_location" + "$" + "publisher_year" + "\n")
    for value in range(0,700):
        file.write(tab[0][value] + "$" + tab[1][value] + "$" + tab[2][value] + "$" + tab[3][value] + "$" + tab[4][value] + "$" + tab[5][value] + "$" + tab[6][value] + "\n")

